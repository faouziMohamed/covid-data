import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QModelIndex, QItemSelectionModel, QItemSelection
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow

from src.generated.mainwindow import Ui_MainWindow
from src.model import ModelCovidData
from src.resources import utils


class CovidView(QMainWindow, Ui_MainWindow):
    FIRST_ROW, FIRST_OPTION = 0, 0
    Today, Yesterday, Other_day = "Today", "Yesterday", "Other day"

    def __init__(self, parent=None):
        super(CovidView, self).__init__(parent)
        self.setupUi(self)
        self.model = ModelCovidData()
        self.colsCount = self.model.columnCount()
        self.dateEdit_is_connected = False
        self.__setup_treeview()
        self.initialize_fields(is_first_load=True)
        self.__setup_event_handler(is_first_load=True)
        self.resize(1030, 654)

    def __setup_treeview(self):
        self.treeView.setModel(self.model)
        self.resize_header_data()
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setRootIsDecorated(False)

    def resize_header_data(self):
        header = self.treeView.header()
        for section, size in zip([0, 1, 2], [100, 120, 170]):
            header.resizeSection(section, size)

    def __setup_event_handler(self, is_first_load: bool = True):
        # model = self.model
        self.treeView.selectionModel().selectionChanged.connect(
            self.on_treeview_selectionChanged
        )

        if is_first_load:
            self.dateEdit.dateChanged.connect(self.on_date_edit_dateChanged)

            self.continent_box.currentIndexChanged.connect(
                self.on_continentBox_currentIndexChanged
            )

            self.country_box.currentIndexChanged.connect(
                self.on_countryBox_currentIndexChanged
            )

    def initialize_fields(self, is_first_load: bool = True):
        if is_first_load:
            self.print_data_columns_to_console()
            self.__fill_country_continent_combobox()
            calendar = self.dateEdit.calendarWidget()
            calendar.setGridVisible(True)
            calendar.setContentsMargins(0, 0, 0, 0)
            today_tuple = utils.today(as_string=False)
            for date_edit in (self.dateEdit, self.dateEdit_text):
                date_edit.setMaximumDate(QDate(*today_tuple))

        try:  # handle the case where the view table is empty
            self.__display_details_about(CovidView.FIRST_ROW)
            self.select_first_row()
        except IndexError:
            for box in (self.country_box, self.continent_box):
                box.setCurrentIndex(CovidView.FIRST_OPTION)
            self.__display_dates_fields(utils.today())
            self.__display_numerical_fields(self.model.db.empty_view)

    def __fill_country_continent_combobox(self):
        countries = list(self.model.db.countries.location)
        continents = list(self.model.db.continents.continent)

        continents_completer = QtWidgets.QCompleter(continents)
        countries_completer = QtWidgets.QCompleter(countries)
        for completer in (continents_completer, countries_completer):
            completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            completer.setFilterMode(QtCore.Qt.MatchContains)

        for combobox in (self.continent_box, self.country_box):
            combobox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)

        self.country_box.addItems(countries)
        self.continent_box.addItems(continents)

        self.country_box.setCompleter(countries_completer)
        self.continent_box.setCompleter(continents_completer)

    def __display_details_about(self, row_index: int):
        view = self.model.db.view
        row = view.iloc[row_index]
        self.__set_current_country(str(row.location))
        self.__set_current_continent(str(row.continent))
        self.__display_dates_fields(str(row.date))
        self.__display_numerical_fields(row)

        self.print_selectedRow_to_console(row)

    def select_first_row(self):
        index = self.model.index(
            CovidView.FIRST_ROW, self.colsCount - 1, QModelIndex()
        )
        selection_model = self.treeView.selectionModel()
        selection_model.select(
            index, QItemSelectionModel.Select | QItemSelectionModel.Rows
        )

    def __display_dates_fields(self, the_date: str):
        a_date_tuple = utils.year_mon_day(the_date)
        selected_date = QDate(*a_date_tuple)
        for date_edit in (self.dateEdit, self.dateEdit_ro, self.dateEdit_text):
            date_edit.setDate(selected_date)

        if the_date == utils.today():
            day_option = CovidView.Today
        elif the_date == utils.yesterday():
            day_option = CovidView.Yesterday
        else:
            day_option = CovidView.Other_day
        self.day_edit.setText(day_option)

    def __display_numerical_fields(self, row: pd.Series):
        fields = (
            self.newTest_spin,
            self.newCases_spin,
            self.newDeaths_spin,
            self.totalTests_spin,
            self.totalCases_spin,
            self.totalDeaths_spin,
        )
        values = (
            row.new_tests,
            row.new_cases,
            row.new_deaths,
            row.total_tests,
            row.total_cases,
            row.total_deaths,
        )
        for field, value in zip(fields, values):
            field.setValue(int(value))

    def __set_current_country(self, location: str):
        country_id = self.model.db.get_country_id(location)
        self.country_box.setCurrentIndex(country_id + 1)
        self.country_edit.setText(location)

    def __set_current_continent(self, continent: str):
        continent_id = self.model.db.get_continent_id(continent)
        self.continent_box.setCurrentIndex(continent_id + 1)
        self.continent_edit.setText(continent)

    # Reimplemented functions and event handlers
    def on_treeview_selectionChanged(
        self, selected: QItemSelection, deselected: QItemSelection
    ):
        utils.ignore(deselected)
        if len(selected.indexes()) == 0:
            return
        selected_row = selected.indexes()[0].row()
        self.beginFilteringRows()
        self.__display_details_about(selected_row)
        self.endFilteringRows()

    def on_date_edit_dateChanged(self, new_date: QDate):
        calendar = self.dateEdit.calendarWidget()
        calendar.setCurrentPage(new_date.year(), new_date.month())
        self.beginFilteringRows()
        self.echo_to_console("date", new_date.toString("yyyy-MM-dd"))
        self.model.filter_by_date(new_date.toString("yyyy-MM-dd"))
        self.initialize_fields(is_first_load=False)
        self.resize_header_data()
        self.endFilteringRows()

    def on_continentBox_currentIndexChanged(self, index: int) -> None:
        if index > 0:
            a_continent = self.continent_box.itemText(index)
            self.echo_to_console("Continent", a_continent)
            self.beginFilteringRows()
            self.model.filter_by_continent(a_continent)
            self.initialize_fields(is_first_load=False)
            self.resize_header_data()
            self.endFilteringRows()

    def on_countryBox_currentIndexChanged(self, index: int) -> None:
        if index > 0:
            a_country = self.country_box.itemText(index)
            self.echo_to_console("Country", a_country)
            self.beginFilteringRows()
            self.model.filter_by_country(a_country)
            self.initialize_fields(is_first_load=False)
            self.resize_header_data()
            self.endFilteringRows()

    def disconnect_dateEdit_connection(self, must_disconnect):
        if must_disconnect:
            self.dateEdit.dateChanged.disconnect(self.on_date_edit_dateChanged)
            self.dateEdit_is_connected = False
        else:
            self.dateEdit.dateChanged.connect(self.on_date_edit_dateChanged)
            self.dateEdit_is_connected = True

    def disconnect_continentBox_connection(self, must_disconnect):
        if must_disconnect:
            self.continent_box.currentIndexChanged.disconnect(
                self.on_continentBox_currentIndexChanged
            )
        else:
            self.continent_box.currentIndexChanged.connect(
                self.on_continentBox_currentIndexChanged
            )

    def disconnect_countryBox_connection(self, must_disconnect):
        if must_disconnect:
            self.country_box.currentIndexChanged.disconnect(
                self.on_countryBox_currentIndexChanged
            )
        else:
            self.country_box.currentIndexChanged.connect(
                self.on_countryBox_currentIndexChanged
            )

    def disconnect_treeView_connection(self, must_disconnect):
        if must_disconnect:
            self.treeView.selectionModel().selectionChanged.disconnect(
                self.on_treeview_selectionChanged
            )
        else:
            self.treeView.selectionModel().selectionChanged.connect(
                self.on_treeview_selectionChanged
            )

    def beginFilteringRows(self, dt=True, ct=True, cr=True, tree=True):
        self.disconnect_dateEdit_connection(dt)
        self.disconnect_continentBox_connection(ct)
        self.disconnect_countryBox_connection(cr)
        self.disconnect_treeView_connection(tree)

    def endFilteringRows(self, dt=False, ct=False, cr=False, tree=False):
        self.beginFilteringRows(dt, ct, cr, tree)

    def print_data_columns_to_console(self):
        print(
            "Date, Continent, Country, New Tests, New cases,",
            "New Deaths, Total tests, Total cases, Total deaths",
        )

    def echo_to_console(self, text: str, value):
        print(f"-------|| The {text} is {value} ||--------")

    def print_selectedRow_to_console(self, row):
        data = [
            self.dateEdit_text.text(),
            row.continent,
            row.location,
            int(row.new_tests),
            int(row.new_cases),
            int(row.new_deaths),
            int(row.total_tests),
            int(row.total_cases),
            int(row.total_deaths),
        ]
        for value in data[:-1]:
            print(f"{value}, ", end="")
        print(data[-1])

    def closeEvent(self, a0: QCloseEvent) -> None:
        a0.accept()
