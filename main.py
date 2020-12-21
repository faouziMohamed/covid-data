import sys

from PyQt5 import QtWidgets, QtCore

# noinspection PyUnresolvedReferences
import src.generated.resources_rc
from src.dataView import CovidView


def read_stylesheet(file_name: str = ':/style.qss') -> str:
    style_file = QtCore.QFile(file_name)
    style_file.open(QtCore.QIODevice.ReadOnly)
    sheet = QtCore.QTextStream(style_file)
    return sheet.readAll()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    style_sheet = read_stylesheet()
    app.setStyleSheet(style_sheet)
    view = CovidView()
    view.show()
    sys.exit(app.exec_())
