from collections import namedtuple

from PyQt5.QtCore import (QAbstractTableModel)
import pandas as pd
from sqlalchemy import (create_engine)

DB_PATH = '../assets/db/'
SQLITE_FILE = 'db.sqlite'
LOCAL_DB = SQLITE_FILE
CSV_FILE = 'covid19-data.csv'
SQLITE_DB_FILE = 'covid19-data.sql'
JSON_FILE = 'covid19-data.json'
URL_CSV_FILE = 'https://raw.githubusercontent.com/owid/covid-19-data/master' \
               '/public/data/owid-covid-data.csv'

Covid = namedtuple("Covid", ('continent', 'location', 'date', 'new_tests',
                             'new_cases', 'new_deaths', 'total_tests',
                             'total_deaths'))


class ModelCovidData(QAbstractTableModel):
    def __init__(self):
        super(ModelCovidData, self).__init__()
        self.df = pd.read_csv(URL_CSV_FILE)
        self.cols = ['continent', 'location', 'date', 'new_tests', 'new_cases',
                     'new_deaths', 'total_tests', 'total_deaths']
        self.prepare_data()
        tr = self.tr
        self.columnTitles = [tr('Continent'), tr('Country'), tr('Date'),
                             tr('New tests'), tr('New cases'), tr('New deaths'),
                             tr('Total tests'), tr('Total deaths')]

    # Prepare local database
    def prepare_data(self):
        self.save_data_to_local()
        self.df = self.df[self.cols].fillna(0)
        self.df = self.df[self.df.continent != 0]
        self.df = self.df.sort_index('date', ascending=False)

    def save_data_to_local(self):
        FILE = DB_PATH + SQLITE_DB_FILE
        TABLE_NAME = "covid_data"
        sqlite_db_engine = create_engine('sqlite:///' + FILE, echo=False)
        self.df.to_csv(DB_PATH + CSV_FILE)
        self.df.to_json(DB_PATH + JSON_FILE)
        self.df.to_sql(TABLE_NAME, con=sqlite_db_engine, if_exists='replace')
