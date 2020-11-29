from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (QMainWindow)

from src.mainwindow import Ui_MainWindow
from src.model import ModelCovidData


class CovidView(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CovidView, self).__init__(parent)
        self.setupUi(self)
        self.model = ModelCovidData()
        countries = self.model.db.countries
        self.comboBox.addItems(list(countries.location))
        self.treeView.setModel(self.model)
        self.treeView.setSortingEnabled(True)
        self.resize(930, 218)

    def closeEvent(self, a0: QCloseEvent) -> None:
        a0.accept()

