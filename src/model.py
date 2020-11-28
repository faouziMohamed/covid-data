from PyQt5.QtCore import (QAbstractTableModel, QModelIndex, Qt, QVariant)

from src.connexion import DbConnexion
from src.constant import DB_NAME


class ModelCovidData(QAbstractTableModel):
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

    def data(self, index: QModelIndex, role: int = ...) -> [QVariant, str]:
        if (role == Qt.DisplayRole) and index.isValid():
            data = self._db.view.iloc[index.row(), index.column()]
            return str(data)
        return QVariant()

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self._db.view.shape[1]

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self._db.view.shape[0]

    @property
    def db(self):
        return self._db

    @property
    def database(self):
        return self.db
