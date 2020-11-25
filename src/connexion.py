import os

from PyQt5.QtSql import QSqlQuery, QSqlDatabase
import pandas as pd
from pandas import DataFrame as DtFrame
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtCore import QObject


def create_connection(df: pd.DataFrame, db_name: str):
    db = QSqlDatabase.addDatabase("QSLITE")
    db.setDatabaseName(db_name)

    tr = QObject.tr
    message = "Unable to establish a database connection.\n" \
              "This example needs SQLite support.\n\n Click Cancel to exit."
    if not db.open():
        QMessageBox.critical(QWidget(), tr("Cannot open database"), tr(message),
                             QMessageBox.cancel)
    bd_exist = os.path.exists(db_name)
    if not bd_exist:
        create_db()


def create_db():
    QSqlQuery('''PRAGMA foreign_keys = ON;''')
    QSqlQuery('''CREATE TABLE continent(idc INTEGER PRIMARY KEY,
                continent VARCHAR(20) NOT NULL);
                
                CREATE TABLE countries(idl INTEGER PRIMARY KEY,
                country VARCHAR(30) NOT NULL, 
                idc INTEGER NOT NULL,
                FOREIGN KEY (idc) 
                REFERENCES continent (idc) 
                ON DELETE RESTRICT 
                ON UPDATE CASCADE );
                
                CREATE TABLE cases(id INTEGER PRIMARY KEY,
                idl INTEGER NOT NULL,
                dates TEXT NOT NULL,
                new_tests REAL NOT NULL,
                new_cases REAL NOT NULL,
                total_deaths REAL NOT NULL);
                ''')


def create_table_for(col_name: str, df: pd.DataFrame) -> pd.DataFrame:
    data = df[col_name].unique()
    table = pd.DataFrame(data)
    table = table.rename(columns={0: col_name})
    table = table.sort_values(col_name)
    table['id'] = sorted(table[col_name].argsort())
    table = table[['id', col_name]]
    return table


def create_continent_table(df: pd.DataFrame) -> pd.DataFrame:
    continent = create_table_for('continent', df)
    return continent


# DtFrame is pd.DataFrame

def create_country_table(df: pd.DataFrame, continent: pd.DataFrame) -> DtFrame:
    columns = ['idl', 'location', 'continent']
    countries = df[columns[1:]]
    countries = countries.set_index(columns[1:])
    unique_rows = list(countries.index.unique())
    countries = pd.DataFrame(unique_rows, columns=columns[1:])
    countries['idl'] = sorted(countries.location.argsort())
    countries = countries[columns]
    countries = countries.rename(columns={'continent': 'idc'})
    countries = countries.replace(list(continent.continent), continent.id)
    return countries


def create_cases_table(df: pd.DataFrame, countries: pd.DataFrame) -> DtFrame:
    cases = df[['location', 'date', 'new_tests', 'new_cases', 'total_deaths']]
    cases = cases.replace(list(countries.location), countries.idc)
    cases = cases.rename(columns={'location': 'idl'})
    cases['id'] = cases.index
    cases = cases[['id']+list(cases.columns[:-1])]
    cases = cases.sort_index()
    return cases
