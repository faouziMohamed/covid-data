import sys

from PyQt5.QtCore import QFile, QIODevice, QTextStream
from PyQt5.QtWidgets import QApplication

from src.dataView import CovidView
# noinspection PyUnresolvedReferences
import src.generated.resources_rc


def read_stylesheet(file_name: str = ':/style.qss') -> str:
    style_file = QFile(file_name)
    style_file.open(QIODevice.ReadOnly)
    sheet = QTextStream(style_file)
    return sheet.readAll()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    style_sheet = read_stylesheet()
    app.setStyleSheet(style_sheet)
    view = CovidView()
    view.show()
    sys.exit(app.exec_())
