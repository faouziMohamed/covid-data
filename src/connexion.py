import os
from operator import or_

import pandas as pd
import sqlalchemy
from sqlalchemy import (create_engine, MetaData, Table, select)

from src.resources import utils
from src.resources.constant import (DB_NAME, CSV_FILE, URL_CSV_FILE, SQL_FILE,
                                    JSON_FILE, FILE_NAME, DB_PATH)
from src.resources.sqlalchemy_declarative import (create_database)


class DbConnexion:
    def __init__(self, db_name: str = DB_NAME):
        self._df = ...  # type: pd.DataFrame
        self._continents = ...  # type: pd.DataFrame
        self._countries = ...  # type: pd.DataFrame
        self._cases = ...  # type: pd.DataFrame
        self._view = ...  # type: pd.DataFrame
        self._engine = ...  # type: sqlalchemy.engine.base.Engine
        self._metadata = ...  # type: MetaData
        self.cols = ['date', 'location', 'new_tests', 'new_cases', 'new_deaths',
                     'total_tests', 'total_cases', 'total_deaths', 'continent']
        utils.ignore(db_name)
        self._db_name = DB_NAME
        self.get_online_data(CSV_FILE)
        self.__config_database()

    def get_online_data(self, url: str = URL_CSV_FILE):
        self._df = pd.read_csv(url, usecols=self.cols)
        return self.__prepare_data(save_data=True)

    # Prepare local database

    def __prepare_data(self, save_data: bool = True):
        if save_data:
            self.save_data_to_local()
        self._df = self._df.fillna(0)
        row_filter = (self._df.location == 'World') | (self._df.continent != 0)
        self._df = self._df.loc[row_filter]
        self._df.loc[self._df.continent == 0, ['continent']] = 'Earth'
        return self.dataframe

    def save_data_to_local(self):
        sqlite_db_engine = create_engine('sqlite:///' + SQL_FILE, echo=False)
        self._df.to_csv(f'{CSV_FILE}')
        self._df.to_json(f'{JSON_FILE}')
        self._df.to_sql(FILE_NAME, con=sqlite_db_engine, if_exists='replace')

    def __config_database(self):
        os.makedirs(DB_PATH, exist_ok=True)
        os.remove(self._db_name)
        db_exists = os.path.exists(self._db_name)

        if not db_exists:
            self.__create_new_db()
        self.__insert_data_for_first_time()
        self.__create_modelView_and_table()

    def __create_new_db(self):
        self._engine = create_database(self._db_name)

    def get_table(self, t_name: str, meta: MetaData) -> Table:
        return Table(t_name, meta, autoload=True, autoload_with=self._engine)

    def __create_modelView_and_table(self):
        with self._engine.connect() as con:
            con.execute("""
                CREATE VIEW model_view AS
                SELECT date, continent, location, new_tests, new_cases,
                       new_deaths,total_tests, total_cases, total_deaths
                FROM continents, countries, cases
                WHERE cases.idl = countries.idl AND 
                      countries.idc = continents.idc
                ORDER BY 
                    date DESC , 
                    total_cases DESC, 
                    total_deaths DESC;
                """)
            model_view = self.get_table('model_view', MetaData())
            select_query = select([model_view])
            today, yesterday = utils.today(), utils.yesterday()
            select_query = select_query.where(
                or_(model_view.columns.date == today,
                    model_view.columns.date == yesterday)
            )
        self._view = pd.read_sql_query(select_query, con=self._engine)
        return self.view

    def __insert_data_for_first_time(self):
        """
        Inserting data for the first time using the sqlalchemy API
        """
        self._continents = self.__create_continents_table()
        self._countries = self.__create_countries_table(self._continents)
        self._cases = self.__create_cases_table(countries=self._countries)

        engine = self._engine
        self._continents.to_sql('continents', con=engine, if_exists='append')
        self._countries.to_sql('countries', con=engine, if_exists='append')
        self._cases.to_sql('cases', con=engine, if_exists='append')

    def __create_table_for(self, col_name: str, id_name='id') -> pd.DataFrame:
        df = self._df
        data = df.loc[:, col_name].unique()
        table = pd.DataFrame(data)
        table = table.rename(columns={0: col_name})
        table = table.sort_values(col_name)
        table.index = sorted(table[col_name].argsort())
        table.index.name = id_name
        return table

    def __create_continents_table(self) -> pd.DataFrame:
        continent = self.__create_table_for('continent', id_name='idc')
        return continent

    def __get_countries_by_continent(self) -> pd.DataFrame:
        cols = ['location', 'continent']
        countries = self._df.loc[:, cols]
        countries = countries.set_index(cols)
        unique_rows = list(countries.index.unique())
        return pd.DataFrame(unique_rows, columns=cols)

    def __create_countries_table(self, continent: pd.DataFrame) -> pd.DataFrame:
        index_name = 'idl'
        countries = self.__get_countries_by_continent()

        # creating index (the id of the relational table)
        index_id_location = sorted(countries.location.argsort())
        countries.index = index_id_location
        countries.index.name = index_name

        countries = countries.rename(columns={'continent': 'idc'})
        cont = list(continent.continent)
        countries = countries.replace(cont, continent.index)
        return countries

    def __create_cases_table(self, countries: pd.DataFrame) -> pd.DataFrame:
        columns = ['location', 'date', 'new_tests', 'new_cases', 'new_deaths',
                   'total_tests', 'total_cases', 'total_deaths']
        cases = self._df.loc[:, columns]
        cases = cases.replace(list(countries.location), countries.index)
        cases = cases.rename(columns={'location': 'idl'})
        cases = cases.sort_values(['date', 'total_cases', 'total_deaths'],
                                  ascending=False)
        cases = cases.reset_index(drop=True)
        cases.index.name = 'id'
        return cases

    def get_country_id(self, country: str) -> int:
        countries = self._countries
        query = (countries.location == country)
        return int(countries.loc[query].index[0])

    def get_continent_id(self, continent: str) -> int:
        continents_df = self._continents
        query = (continents_df.continent == continent)
        return int(continents_df.loc[query].index[0])

    def filter_data_by(self, by: str, rows_pattern: str) -> pd.DataFrame:
        """
        Get data in the view 'model_view' filtered in the column `by`
        where rows are equal to `rows_pattern`. This will make a select query
        with these parameter.

        Example: Filter in the column Country and the country to get results is
        'Comoros'. so by = 'country' and rows_pattern = 'Comoros'
        and this perform the select query :
        SELECT 'country' FROM model_view WHERE country = 'Comoros'

        :param by: column in the database
        :param rows_pattern: The pattern to search in the database
        :return: Pandas.DataFrame Table
        """
        model_view = self.get_table('model_view', MetaData())
        select_query = select([model_view]).where(
            model_view.columns[by] == rows_pattern)
        self._view = pd.read_sql_query(select_query, con=self._engine)
        return self._view

    @property
    def continents(self):
        return self._continents

    @property
    def countries(self):
        return self._countries

    @property
    def cases(self):
        return self._cases

    @property
    def view(self):
        return self._view

    @property
    def dataframe(self):
        return self._df

    @property
    def df(self):
        return self.dataframe

    @property
    def empty_view(self):
        """
        This property return a pandas series that contains only zeros
        and index are the columns of the view table
        :return: Pandas series containing only zeros values
        """
        keys = tuple(self.view.columns)
        return pd.Series(0, index=keys[3:])
