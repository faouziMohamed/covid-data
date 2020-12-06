import sys

from PyQt5.QtCore import QFile, QIODevice, QTextStream
from PyQt5.QtWidgets import QApplication

from src.dataView import CovidView
# noinspection PyUnresolvedReferences
import src.ressource.ressources_rc

if __name__ == '__main__':
    style_file = QFile(':/style.qss')
    style_file.open(QIODevice.ReadOnly)
    sheet = QTextStream(style_file)
    style_sheet = sheet.readAll()
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    view = CovidView()
    view.show()
    sys.exit(app.exec_())
