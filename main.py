import sys

from PyQt5.QtWidgets import QApplication

from src.dataView import CovidView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = CovidView()
    view.show()
    sys.exit(app.exec_())
