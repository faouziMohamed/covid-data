import os

import sqlalchemy
from PyQt5.QtSql import (QSqlQuery, QSqlDatabase)
import pandas as pd
from PyQt5.QtWidgets import (QMessageBox, QWidget)
from PyQt5.QtCore import (QTranslator)


class DbConnexion:
    def __init__(self, data_frame: pd.DataFrame, db_name: str):
        self.df = data_frame
        self.db_name = db_name
        self.config_database()

    def config_database(self):
        db_exists = os.path.exists(self.db_name)
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.db_name)

        if not db.open():
            self.show_warning()
        if not db_exists:
            self.create_new_db()
        self.insert_data_for_first_time()

    @staticmethod
    def show_warning():
        tr = QTranslator.tr
        message = "Unable to establish a database connection.\n" \
                  "This example needs SQLite support.\n\n Click Cancel to exit."
        QMessageBox.critical(QWidget(), tr(QWidget(), "Cannot open database"),
                             tr(QWidget(), message))

    def create_new_db(self):
        QSqlQuery('''PRAGMA foreign_keys = ON;''')
        QSqlQuery('''CREATE TABLE continents(
                    idc INTEGER PRIMARY KEY,
                    continent VARCHAR(20) NOT NULL);''')

        QSqlQuery('''CREATE TABLE countries(
                    idl INTEGER PRIMARY KEY,
                    location VARCHAR(30) NOT NULL, 
                    idc INTEGER NOT NULL,
                    FOREIGN KEY (idc) 
                        REFERENCES continents (idc) 
                        ON DELETE RESTRICT 
                        ON UPDATE CASCADE );''')

        QSqlQuery('''CREATE TABLE cases(
                    id INTEGER PRIMARY KEY,
                    idl INTEGER NOT NULL,
                    dates TEXT NOT NULL,
                    new_tests FLOAT NOT NULL,
                    new_cases FLOAT NOT NULL,
                    new_deaths FLOAT NOT NULL,
                    total_deaths FLOAT NOT NULL,
                    FOREIGN KEY (idl) 
                        REFERENCES countries(idl)
                        ON DELETE RESTRICT 
                        ON UPDATE CASCADE);''')

    def insert_data_for_first_time(self):
        """
        Inserting data for the first time using the sqlalchemy API,
        then insert using the PyQt5 API
        """
        db_name = self.db_name
        continents = self.create_continents_table()
        countries = self.create_countries_table(continent=continents)
        cases = self.create_cases_table(countries=countries)

        engine = sqlalchemy.create_engine('sqlite:///' + db_name, echo=False)
        continents.to_sql('continents', con=engine, if_exists='append')
        countries.to_sql('countries', con=engine, if_exists='append')
        cases.to_sql('cases', con=engine, if_exists='append', chunksize=1000)

    def create_table_for(self, col_name: str, id_name='id') -> pd.DataFrame:
        df = self.df
        data = df[col_name].unique()
        table = pd.DataFrame(data)
        table = table.rename(columns={0: col_name})
        table = table.sort_values(col_name)
        table.index = sorted(table[col_name].argsort())
        table.index.name = id_name
        return table

    def create_continents_table(self) -> pd.DataFrame:
        continent = self.create_table_for('continent', id_name='idc')
        return continent

    # DtFrame is pd.DataFrame

    def get_countries_by_continent(self, cols: [str]) -> pd.DataFrame:
        countries = self.df[cols]
        countries = countries.set_index(cols)
        unique_rows = list(countries.index.unique())
        return pd.DataFrame(unique_rows, columns=cols)

    def create_countries_table(self, continent: pd.DataFrame) -> pd.DataFrame:
        index_name, columns = 'idl', ['location', 'continent']
        countries = self.get_countries_by_continent(columns)

        # creating index (the id of the relational table)
        index_id_location = sorted(countries.location.argsort())
        countries.index = index_id_location
        countries.index.name = index_name

        countries = countries.rename(columns={'continent': 'idc'})
        cont = list(continent.continent)
        countries = countries.replace(cont, continent.index)
        return countries

    def create_cases_table(self, countries: pd.DataFrame) -> pd.DataFrame:
        columns = ['location', 'date', 'new_tests', 'new_cases',
                   'new_deaths', 'total_tests', 'total_deaths']
        cases = self.df[columns]
        cases = cases.replace(list(countries.location), countries.idc)
        cases = cases.rename(columns={'location': 'idl', 'date': 'dates'})
        cases.index.name = 'id'
        return cases
