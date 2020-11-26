import sys

from PyQt5.QtWidgets import QApplication

from src.dataView import CovidView


def main():
    app = QApplication(sys.argv)
    view = CovidView()
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
