from PyQt5 import QtCore
from PyQt5.QtCore import (QModelIndex, Qt, QVariant, QObject)

from src.connexion import DbConnexion
from src.resources import utils
from src.resources.constant import DB_NAME


class ModelCovidData(QtCore.QAbstractTableModel):
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

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
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

    @property
    def db(self):
        return self._db

    @property
    def database(self):
        return self.db


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent: QObject):
        super(SortFilterProxyModel, self).__init__(parent)
        self.filter_by_date = True
        self.filter_by_country = False
        self.filter_by_continent = False
        self.date = utils.today(as_string=True)
        self.country = "Morocco"
        self.continent = 'Africa'

    def sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder):
        self.sourceModel().sort(column, order)
        # self.dataChanged.emit(QModelIndex(), QModelIndex())

    def filterAcceptsRow(self, source_row: int,
                         source_parent: QModelIndex) -> bool:
        if self.filter_by_date:
            return self.filter_by(self.date, source_parent, source_row, 0)
        elif self.filter_by_continent:
            return self.filter_by(self.continent, source_parent, source_row, 1)
        else:  # filter country
            return self.filter_by(self.country, source_parent, source_row, 2)

    def filter_by(self, by, source_parent, source_row, source_column) -> bool:
        model, index = self.sourceModel(), self.sourceModel().index
        item_index = index(source_row, source_column, source_parent)
        print(f"filter by {by}--- {model.data(item_index)}")
        return model.data(item_index) == by
