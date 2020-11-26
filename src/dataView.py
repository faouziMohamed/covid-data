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
