import pandas as pd
from PyQt5.QtCore import QDate, QModelIndex, QItemSelectionModel
from PyQt5.QtCore import (QItemSelection)
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (QMainWindow)

from src.ressource import utils
from src.design.mainwindow import Ui_MainWindow
from src.model import ModelCovidData


class CovidView(QMainWindow, Ui_MainWindow):
    LAST_ROW, FIRST_ROW = -1, 0
    FIRST_OPTION, COLUMNS_COUNT = 0, 0
    TODAY, YESTERDAY, OTHER_DAY = 1, 2, 3

    def __init__(self, parent=None):
        super(CovidView, self).__init__(parent)
        self.setupUi(self)
        self.model = ModelCovidData()
        CovidView.COLUMNS_COUNT = self.model.columnCount()
        self.setup_treeview()
        self.initialize_fields(is_first_load=True)
        self.setup_event_handler()
        self.resize(991, 654)

    def initialize_fields(self, is_first_load: bool = True):
        db = self.model.db
        if is_first_load:
            countries = db.countries
            continents = db.continents
            today_tuple = utils.today(as_string=False)
            for date_edit in (self.dateEdit, self.dateEdit_text):
                date_edit.setMaximumDate(QDate(*today_tuple))

            combo = (self.country_box, self.continent_box)
            values = (list(countries.location), list(continents.continent))
            for combo_box, items in zip(combo, values):
                combo_box.addItems(items)
        # handle the case where the view table is empty
        try:
            self.__display_details_about(CovidView.FIRST_ROW)
            index = self.model.index(0, CovidView.COLUMNS_COUNT, QModelIndex())
            selectionModel = self.treeView.selectionModel()
            selectionModel.select(index,
                                  QItemSelectionModel.ClearAndSelect |
                                  QItemSelectionModel.Rows)
        except IndexError:
            for box in (self.country_box, self.continent_box):
                box.setCurrentIndex(CovidView.FIRST_OPTION)
            self.__display_dates_fields(utils.today())
            self.__display_numerical_fields(db.view_row_with_zeros)

    def setup_event_handler(self):
        selectionChanged = self.treeView.selectionModel().selectionChanged
        selectionChanged.connect(self.on_treeView_selectionChanged)

        index_changed = self.date_box_2.currentIndexChanged
        index_changed.connect(self.on_dateBox2_currentIndexChanged)

        index_changed2 = self.date_box.currentIndexChanged
        index_changed2.connect(self.on_dateBox_currentIndexChanged)

        date_changed = self.dateEdit.dateChanged
        date_changed.connect(self.on_date_edit_dateChanged)

    def setup_treeview(self):
        self.treeView.setModel(self.model)
        self.treeView.setSortingEnabled(True)
        for this_column_number in (0, 1, 3, 4, 5, 6, 7, 8):
            self.treeView.resizeColumnToContents(this_column_number)

    def closeEvent(self, a0: QCloseEvent) -> None:
        a0.accept()

    def on_treeView_selectionChanged(self, selected: QItemSelection,
                                     deselected: QItemSelection):
        if len(selected.indexes()) == 0:
            return
        selected_row = selected.indexes()[0].row()
        self.__display_details_about(selected_row)

    def __display_details_about(self, row_index: int):
        print(self.dateEdit_text.text())
        view = self.model.db.view
        row = view.iloc[row_index]
        self.__set_current_country(str(row.location))
        self.__set_current_continent(str(row.continent))
        self.__display_dates_fields(str(row.dates))
        self.__display_numerical_fields(row)

    def __set_current_country(self, location: str):
        country_id = self.model.db.get_country_id(location)
        self.country_box.setCurrentIndex(country_id + 1)
        self.country_edit.setText(location)

    def __set_current_continent(self, continent: str):
        continent_id = self.model.db.get_continent_id(continent)
        self.continent_box.setCurrentIndex(continent_id + 1)
        self.continent_edit.setText(continent)

    def __display_dates_fields(self, a_date: str):
        a_date_tuple = utils.year_mon_day(a_date)
        selected_date = QDate(*a_date_tuple)
        for date_edit in (self.dateEdit, self.dateEdit_text):
            date_edit.setDate(selected_date)

        if a_date == utils.today():
            day_option = CovidView.TODAY
        elif a_date == utils.yesterday():
            day_option = CovidView.YESTERDAY
        else:
            day_option = CovidView.OTHER_DAY

        self.date_box.setCurrentIndex(day_option)
        self.date_box_2.setCurrentIndex(day_option)

    def __display_numerical_fields(self, row: pd.Series):
        fields = (self.newTest_spin, self.newCases_spin,
                  self.newDeaths_spin, self.totalTests_spin,
                  self.totalCases_spin, self.totalDeaths_spin)
        values = (row.new_tests, row.new_cases, row.new_deaths,
                  row.total_tests, row.total_cases, row.total_deaths)
        for field, value in zip(fields, values):
            field.setValue(int(value))

    def on_dateBox_currentIndexChanged(self, index: int) -> None:
        print(f'Box : Ok changed, new index : {index}, {type(index)}')

    def on_dateBox2_currentIndexChanged(self, index: int) -> None:
        if index in [1, 2]:
            self.dateEdit.setCalendarPopup(False)
            self.dateEdit.setReadOnly(True)
            new_date = utils.today() if index == 1 else utils.yesterday()
            new_date_tuple = utils.year_mon_day(new_date)
            self.on_date_edit_dateChanged(QDate(*new_date_tuple))
        else:
            self.dateEdit.setCalendarPopup(True)
            self.dateEdit.setReadOnly(False)

    def on_date_edit_dateChanged(self, new_date: QDate):
        self.model.db.filter_data_by_date(new_date.toString('yyyy-MM-dd'))
        self.treeView.setModel(self.model)
        self.treeView.reset()
        self.initialize_fields(is_first_load=False)

    # def on_date_edit_dateChanged(self, new_date: QDate):
