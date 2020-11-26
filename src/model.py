import pandas as pd
from PyQt5.QtCore import (QAbstractTableModel, QModelIndex, Qt, QVariant)
from sqlalchemy import (create_engine)

from src.connexion import DbConnexion

DB_PATH = 'assets/db'
FILE_NAME = 'covid19-data'
CSV_FILE = f'{DB_PATH}/{FILE_NAME}.csv'
JSON_FILE = f'{DB_PATH}/{FILE_NAME}.json'
SQL_FILE = f'{DB_PATH}/{FILE_NAME}.sql'
DB_NAME = f'{DB_PATH}/{FILE_NAME}.sqlite'
URL_CSV_FILE = 'https://raw.githubusercontent.com/owid/covid-19-data/master' \
               '/public/data/owid-covid-data.csv'


class ModelCovidData(QAbstractTableModel):
    def __init__(self):
        super(ModelCovidData, self).__init__()
        # self.df = pd.read_csv(URL_CSV_FILE)
        self.df = pd.read_csv(CSV_FILE)

        self.cols = ['date', 'location', 'new_tests', 'new_cases', 'new_deaths',
                     'total_tests', 'total_cases', 'total_deaths', 'continent']
        self.prepare_data()
        tr = self.tr
        self.columnTitles = [tr('Date'), tr('Continent'), tr('Country'),
                             tr('New tests'), tr('New cases'), tr('New deaths'),
                             tr('Total tests'), tr('Total cases'),
                             tr('Total deaths')]

        self._db = DbConnexion(self.df, DB_NAME)
        # covid_data = Covid

    # Prepare local database

    def prepare_data(self):
        self.save_data_to_local()
        self.df = self.df[self.cols].fillna(0)
        self.df = self.df[self.df.continent != 0]

    def save_data_to_local(self):
        FILE = f'{SQL_FILE}'
        TABLE_NAME = "covid_data"
        sqlite_db_engine = create_engine('sqlite:///' + FILE, echo=False)
        self.df.to_csv(f'{CSV_FILE}')
        self.df.to_json(f'{JSON_FILE}')
        self.df.to_sql(TABLE_NAME, con=sqlite_db_engine, if_exists='replace')

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = ...):
        if (role == Qt.DisplayRole) and (orientation == Qt.Horizontal):
            return self.tr(self.columnTitles[section])
        return QVariant()

    def data(self, index: QModelIndex, role: int = ...) -> [QVariant, str]:
        if (role == Qt.DisplayRole) and index.isValid():
            data = self._db.cases.iloc[index.row(), index.column()]
            return str(data)
        return QVariant()

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self._db.cases.shape[1]

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self._db.cases.shape[0]

    @property
    def db(self):
        return self._db
