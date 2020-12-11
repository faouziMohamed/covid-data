import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtCore import (QModelIndex, Qt, QVariant)

from src.connexion import DbConnexion
from src.resources.constant import DB_NAME


class ModelCovidData(QtCore.QAbstractTableModel):
    FIRST_ROW = 0

    def __init__(self):
        super(ModelCovidData, self).__init__()
        tr = self.tr
        self.columnTitles = [tr('Date'), tr('Continent'), tr('Country'),
                             tr('New tests'), tr('New cases'), tr('New deaths'),
                             tr('Total tests'), tr('Total cases'),
                             tr('Total deaths')]

        self._db = DbConnexion(DB_NAME)

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = ...):
        if (role == Qt.DisplayRole) and (orientation == Qt.Horizontal):
            return self.tr(self.columnTitles[section])
        return QVariant()

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.TextAlignmentRole and index.isValid():
            if index.column() > 2:
                return Qt.AlignVCenter + Qt.AlignRight
        if (role == Qt.DisplayRole) and index.isValid():
            data = self._db.view.iloc[index.row(), index.column()]
            data = int(data) if index.column() > 2 else self.tr(data)
            return data
        return QVariant()

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self._db.view.shape[1]

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self._db.view.shape[0]

    def sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder):
        col = self._db.view.columns[column]
        sort_order = True if order == Qt.DescendingOrder else False
        self._db.view.sort_values(by=col, ascending=sort_order, inplace=True)
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def filter_by_date(self, a_date: str) -> pd.DataFrame:
        self.beginResetModel()
        new_data = self._db.filter_data_by_date(a_date)
        self.endResetModel()
        return new_data

    def filter_by_continent(self, a_continent: str) -> pd.DataFrame:
        self.beginResetModel()
        new_data = self._db.filter_data_by_continent(a_continent)
        self.endResetModel()
        return new_data

    @property
    def db(self):
        return self._db

    @property
    def database(self):
        return self.db
