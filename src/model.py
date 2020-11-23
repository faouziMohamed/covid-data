from PyQt5.QtCore import QAbstractTableModel

class ModelCovidData(QAbstractTableModel):
    def __init__(self):
        super(ModelCovidData, self).__init__()
