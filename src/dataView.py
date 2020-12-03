from PyQt5.QtCore import QDate
from PyQt5.QtCore import (QItemSelection)  # pyqtSlot as Slot
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (QMainWindow)

from src import utils
from src.mainwindow import Ui_MainWindow
from src.model import ModelCovidData
import pandas as pd


class CovidView(QMainWindow, Ui_MainWindow):
    LAST_ROW, FIRST_ROW = -1, 0,
    FIRST_OPTION = 0
    TODAY, YESTERDAY, OTHER_DAY = 1, 2, 3

    def __init__(self, parent=None):
        super(CovidView, self).__init__(parent)
        self.setupUi(self)
        self.model = ModelCovidData()
        self.initialize_fields()
        self.setup_treeview()
        self.setup_event_handler()
        self.resize(991, 654)

    def initialize_fields(self):
        db = self.model.db
        countries = db.countries
        continents = db.continents
        self.country_box.addItems(list(countries.location))
        self.continent_box.addItems(list(continents.continent))

        # handle the case where the view table is empty
        try:
            self.__display_details_about(CovidView.FIRST_ROW)
        except IndexError:
            for box in (self.country_box, self.continent_box):
                box.setCurrentIndex(CovidView.FIRST_OPTION)
            self.__display_dates_fields(utils.today())
            self.__display_numerical_fields(db.view_row_with_zeros)

    def setup_event_handler(self):
        selectionChanged = self.treeView.selectionModel().selectionChanged
        selectionChanged.connect(self.on_treeview_selectionChanged)

    def setup_treeview(self):
        self.treeView.setModel(self.model)
        self.treeView.setSortingEnabled(True)
        for this_column_number in (0, 1, 3, 4, 5, 6, 7, 8):
            self.treeView.resizeColumnToContents(this_column_number)

    def closeEvent(self, a0: QCloseEvent) -> None:
        a0.accept()

    def on_treeview_selectionChanged(self, selected: QItemSelection,
                                     deselected: QItemSelection):
        if len(selected.indexes()) == 0:
            return
        selected_row = selected.indexes()[0].row()
        self.__display_details_about(selected_row)

    def __display_details_about(self, row_index: int):
        view = self.model.db.view
        row = view.iloc[row_index]
        self.__set_current_country(str(row.location))
        self.__set_current_continent(str(row.continent))
        self.__display_dates_fields(str(row.dates))
        self.__display_numerical_fields(row)

    def __set_current_country(self, location: str):
        country_id = self.model.db.get_country_id(location)
        self.country_box.setCurrentIndex(country_id + 1)

    def __set_current_continent(self, continent):
        continent_id = self.model.db.get_continent_id(str(continent))
        self.continent_box.setCurrentIndex(continent_id + 1)

    def __display_dates_fields(self, a_date: str):
        a_date_tuple = utils.year_mon_day(a_date)
        selected_date = QDate(*a_date_tuple)
        for date_edit in (self.dateEdit, self.dateEdit_text):
            date_edit.setDate(selected_date)

        if a_date == utils.today():
            self.date_box.setCurrentIndex(CovidView.TODAY)
        elif a_date == utils.yesterday():
            self.date_box.setCurrentIndex(CovidView.YESTERDAY)
        else:
            self.date_box.setCurrentIndex(CovidView.OTHER_DAY)

    def __display_numerical_fields(self, row: pd.Series):
        fields = (self.newTest_spin, self.newCases_spin,
                  self.newDeaths_spin, self.totalTests_spin,
                  self.totalCases_spin, self.totalDeaths_spin)
        values = (row.new_tests, row.new_cases, row.new_deaths,
                  row.total_tests, row.total_cases, row.total_deaths)
        for field, value in zip(fields, values):
            field.setValue(int(value))
