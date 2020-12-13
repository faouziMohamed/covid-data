# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(982, 589)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 1000))
        font = QtGui.QFont()
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("/*QWidget {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QWidget#centralwidget {\n"
"    background: qlineargradient(x1:0, y1:0.1, x2:0.5, y2:1,\n"
"            stop: 0 rgb(0, 1, 59),\n"
"            stop: 0.5 rgba(2, 27, 37, 0.931),\n"
"            stop: 1 rgb(8, 47, 25));\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid rgb(37, 90, 81);\n"
"    border-radius: 9px;\n"
"    margin-top: 10px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #00521b,\n"
"            stop: 0.5 #FFFFFF);\n"
"}\n"
"\n"
"QGroupBox>QLabel {\n"
"    color: #96cccc;\n"
"}\n"
"\n"
"QComboBox {\n"
"    combobox-popup: 0;\n"
"    color: rgb(0, 2, 33);\n"
"    background-color:rgb(221, 235, 239);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(147, 149, 148);\n"
"    border-radius: 0px 5px;\n"
"    color: rgb(0, 17, 17);\n"
"    background-color:rgb(221, 235, 239);\n"
"    selection-color: rgb(0, 0, 80);\n"
"    selection-background-color: rgb(51, 175, 93);\n"
"}\n"
"\n"
"QComboBox,\n"
"QLineEdit,\n"
"QSpinBox,\n"
"QDateEdit {\n"
"    border:2px double darkgray;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit,\n"
"QSpinBox {\n"
"    selection-color: rgb(0, 0, 80);\n"
"    selection-background-color: rgb(0, 175, 26);\n"
"    background-color:  rgb(226, 241, 199);\n"
"}\n"
"\n"
"QComboBox::drop-down,\n"
"QDateEdit::drop-down\n"
" {\n"
"    border:unset;\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
" {\n"
"    border:1px solid rgb(143, 173, 223);\n"
"    background-color:rgb(154, 184, 239);\n"
"}\n"
"\n"
"QComboBox::down-arrow,\n"
"QDateEdit::drop-down {\n"
"    image: url(\":/arrow_down.svg\");\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QDateEdit::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 6px 8px;\n"
"    border: 1px outset rgb(160, 171, 154);\n"
"    background: qlineargradient(x1: 0, y1: 0.1, x2: 1, y2: 0.5,\n"
"            stop: 0 #f6f7fa,\n"
"            stop: 1 rgb(0, 87, 127));\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    border-color: rgb(141, 141, 70);\n"
"    background: qlineargradient(x1: 0, y1: 0.1, x2: 1, y2: 0.5,\n"
"            stop: 0 #f6f7fa,\n"
"            stop: 0.8 rgb(42, 135, 71));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"            stop: 0 rgb(0, 161, 51),\n"
"            stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                        stop:0.5 rgb(10, 20, 50),\n"
"                        stop:0.8 rgb(1, 20, 70));\n"
"    color: rgb(222,230,255);\n"
"    height:19px;\n"
"    padding-top: 2px;\n"
"    padding-left: 4px;\n"
"    border: 1px solid rgb(20, 50, 100);\n"
"}\n"
"\n"
"QHeaderView::section:hover\n"
"{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                        stop:0.5 rgb(10, 30, 70),\n"
"                        stop: 0.8 rgb(10, 35, 100));\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"    image: url(\":/header_arrow_down.svg\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(\":/header_arrow_up.svg\");\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QTreeView {\n"
"    show-decoration-selected: 1;\n"
"    background-color: rgb(182, 182, 182);\n"
"    alternate-background-color: rgb(154, 154, 154);\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    margin-left: 0;\n"
"    border: 1px solid rgba(99, 124, 118, 0.795);\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #8ab6ce,\n"
"            stop: 0.9 #b2c0c2);\n"
"    border: 1px solid #bfcde4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    border: 1px solid #567dbc;\n"
"    selection-background-color: #3374ff;\n"
"    color: rgb(0, 12, 12);\n"
"}\n"
"\n"
"QTreeView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #6ea1f1,\n"
"            stop: 1 #567dbc);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #6b9be8,\n"
"            stop: 1 #577fbf);\n"
"}\n"
"*/")
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setEnabled(True)
        self.dateEdit.setMinimumSize(QtCore.QSize(170, 0))
        self.dateEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.dateEdit.setFont(font)
        self.dateEdit.setMouseTracking(True)
        self.dateEdit.setAutoFillBackground(True)
        self.dateEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dateEdit.setWrapping(True)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setSpecialValueText("")
        self.dateEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit.setKeyboardTracking(True)
        self.dateEdit.setProperty("showGroupSeparator", True)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 11, 23), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(2019, 9, 30))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(2020, 11, 23))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.continent_box = QtWidgets.QComboBox(self.centralwidget)
        self.continent_box.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        self.continent_box.setFont(font)
        self.continent_box.setEditable(True)
        self.continent_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.continent_box.setObjectName("continent_box")
        self.continent_box.addItem("")
        self.horizontalLayout_2.addWidget(self.continent_box)
        self.country_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_box.sizePolicy().hasHeightForWidth())
        self.country_box.setSizePolicy(sizePolicy)
        self.country_box.setMinimumSize(QtCore.QSize(0, 0))
        self.country_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.country_box.setFont(font)
        self.country_box.setStyleSheet("")
        self.country_box.setEditable(True)
        self.country_box.setMaxCount(99999)
        self.country_box.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.country_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.country_box.setFrame(True)
        self.country_box.setObjectName("country_box")
        self.country_box.addItem("")
        self.horizontalLayout_2.addWidget(self.country_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.treeView = QtWidgets.QTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(0, 260))
        font = QtGui.QFont()
        self.treeView.setFont(font)
        self.treeView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.treeView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeView.setAlternatingRowColors(False)
        self.treeView.setUniformRowHeights(False)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setAllColumnsShowFocus(True)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setCascadingSectionResizes(False)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filter1Box = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter1Box.sizePolicy().hasHeightForWidth())
        self.filter1Box.setSizePolicy(sizePolicy)
        self.filter1Box.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        self.filter1Box.setFont(font)
        self.filter1Box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filter1Box.setFlat(False)
        self.filter1Box.setCheckable(False)
        self.filter1Box.setObjectName("filter1Box")
        self.formLayout_4 = QtWidgets.QFormLayout(self.filter1Box)
        self.formLayout_4.setObjectName("formLayout_4")
        self.dateEdit_ro = QtWidgets.QDateEdit(self.filter1Box)
        self.dateEdit_ro.setEnabled(True)
        self.dateEdit_ro.setMinimumSize(QtCore.QSize(170, 33))
        self.dateEdit_ro.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.dateEdit_ro.setFont(font)
        self.dateEdit_ro.setMouseTracking(True)
        self.dateEdit_ro.setAutoFillBackground(True)
        self.dateEdit_ro.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dateEdit_ro.setWrapping(True)
        self.dateEdit_ro.setFrame(True)
        self.dateEdit_ro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEdit_ro.setReadOnly(False)
        self.dateEdit_ro.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_ro.setSpecialValueText("")
        self.dateEdit_ro.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit_ro.setKeyboardTracking(True)
        self.dateEdit_ro.setProperty("showGroupSeparator", True)
        self.dateEdit_ro.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 11, 23), QtCore.QTime(0, 0, 0)))
        self.dateEdit_ro.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit_ro.setMinimumDate(QtCore.QDate(2019, 9, 30))
        self.dateEdit_ro.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_ro.setCalendarPopup(False)
        self.dateEdit_ro.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_ro.setDate(QtCore.QDate(2020, 11, 23))
        self.dateEdit_ro.setObjectName("dateEdit_ro")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.dateEdit_ro)
        self.dateEdit_text = QtWidgets.QDateEdit(self.filter1Box)
        self.dateEdit_text.setEnabled(True)
        self.dateEdit_text.setMinimumSize(QtCore.QSize(170, 33))
        self.dateEdit_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.dateEdit_text.setFont(font)
        self.dateEdit_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEdit_text.setReadOnly(True)
        self.dateEdit_text.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_text.setProperty("showGroupSeparator", True)
        self.dateEdit_text.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit_text.setMinimumDate(QtCore.QDate(2019, 9, 30))
        self.dateEdit_text.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_text.setDate(QtCore.QDate(2020, 11, 23))
        self.dateEdit_text.setObjectName("dateEdit_text")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.dateEdit_text)
        self.day_edit = QtWidgets.QLineEdit(self.filter1Box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_edit.sizePolicy().hasHeightForWidth())
        self.day_edit.setSizePolicy(sizePolicy)
        self.day_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.day_edit.setStyleSheet("border:1px solid #666;\n"
"height:25px;\n"
"color:black;\n"
"padding-left:2px;\n"
"background:qlineargradient(x1:0.1, y1:0.3,x2:0.6,y2:1.1,\n"
"                    stop: 0 #888,\n"
"                    stop: 0.5 #aac,\n"
"                    stop: 1 #888);\n"
"text-align: center;")
        self.day_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.day_edit.setReadOnly(True)
        self.day_edit.setObjectName("day_edit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.day_edit)
        self.horizontalLayout.addWidget(self.filter1Box)
        self.queryBox = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queryBox.sizePolicy().hasHeightForWidth())
        self.queryBox.setSizePolicy(sizePolicy)
        self.queryBox.setMinimumSize(QtCore.QSize(0, 0))
        self.queryBox.setMaximumSize(QtCore.QSize(9999999, 16777215))
        font = QtGui.QFont()
        self.queryBox.setFont(font)
        self.queryBox.setObjectName("queryBox")
        self.formLayout = QtWidgets.QFormLayout(self.queryBox)
        self.formLayout.setObjectName("formLayout")
        self.countryLabel = QtWidgets.QLabel(self.queryBox)
        font = QtGui.QFont()
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.countryLabel)
        self.label = QtWidgets.QLabel(self.queryBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.country_edit = QtWidgets.QLineEdit(self.queryBox)
        self.country_edit.setMinimumSize(QtCore.QSize(170, 30))
        self.country_edit.setReadOnly(True)
        self.country_edit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.country_edit.setObjectName("country_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.country_edit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.continent_edit = QtWidgets.QLineEdit(self.queryBox)
        self.continent_edit.setMinimumSize(QtCore.QSize(170, 30))
        self.continent_edit.setReadOnly(True)
        self.continent_edit.setObjectName("continent_edit")
        self.verticalLayout_2.addWidget(self.continent_edit)
        self.run_sql_btn = QtWidgets.QPushButton(self.queryBox)
        self.run_sql_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.run_sql_btn.setObjectName("run_sql_btn")
        self.verticalLayout_2.addWidget(self.run_sql_btn)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.queryBox)
        self.dailyBox = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dailyBox.sizePolicy().hasHeightForWidth())
        self.dailyBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.dailyBox.setFont(font)
        self.dailyBox.setObjectName("dailyBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.dailyBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.tests_label = QtWidgets.QLabel(self.dailyBox)
        font = QtGui.QFont()
        self.tests_label.setFont(font)
        self.tests_label.setObjectName("tests_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tests_label)
        self.cases_label = QtWidgets.QLabel(self.dailyBox)
        font = QtGui.QFont()
        self.cases_label.setFont(font)
        self.cases_label.setObjectName("cases_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cases_label)
        self.deaths_label = QtWidgets.QLabel(self.dailyBox)
        font = QtGui.QFont()
        self.deaths_label.setFont(font)
        self.deaths_label.setObjectName("deaths_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.deaths_label)
        self.newTest_spin = QtWidgets.QSpinBox(self.dailyBox)
        self.newTest_spin.setMinimumSize(QtCore.QSize(170, 0))
        self.newTest_spin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.newTest_spin.setFont(font)
        self.newTest_spin.setWrapping(False)
        self.newTest_spin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.newTest_spin.setReadOnly(True)
        self.newTest_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.newTest_spin.setAccelerated(True)
        self.newTest_spin.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.newTest_spin.setProperty("showGroupSeparator", True)
        self.newTest_spin.setMaximum(999999999)
        self.newTest_spin.setObjectName("newTest_spin")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.newTest_spin)
        self.newCases_spin = QtWidgets.QSpinBox(self.dailyBox)
        self.newCases_spin.setMinimumSize(QtCore.QSize(170, 0))
        self.newCases_spin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.newCases_spin.setFont(font)
        self.newCases_spin.setWrapping(False)
        self.newCases_spin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.newCases_spin.setReadOnly(True)
        self.newCases_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.newCases_spin.setAccelerated(True)
        self.newCases_spin.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.newCases_spin.setProperty("showGroupSeparator", True)
        self.newCases_spin.setMaximum(999999999)
        self.newCases_spin.setObjectName("newCases_spin")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.newCases_spin)
        self.newDeaths_spin = QtWidgets.QSpinBox(self.dailyBox)
        self.newDeaths_spin.setMinimumSize(QtCore.QSize(170, 0))
        self.newDeaths_spin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.newDeaths_spin.setFont(font)
        self.newDeaths_spin.setWrapping(False)
        self.newDeaths_spin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.newDeaths_spin.setReadOnly(True)
        self.newDeaths_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.newDeaths_spin.setAccelerated(True)
        self.newDeaths_spin.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.newDeaths_spin.setProperty("showGroupSeparator", True)
        self.newDeaths_spin.setMaximum(999999999)
        self.newDeaths_spin.setObjectName("newDeaths_spin")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.newDeaths_spin)
        self.horizontalLayout.addWidget(self.dailyBox)
        self.cumulativeBox = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cumulativeBox.sizePolicy().hasHeightForWidth())
        self.cumulativeBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.cumulativeBox.setFont(font)
        self.cumulativeBox.setObjectName("cumulativeBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.cumulativeBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.totTests_label = QtWidgets.QLabel(self.cumulativeBox)
        font = QtGui.QFont()
        self.totTests_label.setFont(font)
        self.totTests_label.setObjectName("totTests_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.totTests_label)
        self.totalTests_spin = QtWidgets.QSpinBox(self.cumulativeBox)
        self.totalTests_spin.setMinimumSize(QtCore.QSize(0, 0))
        self.totalTests_spin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.totalTests_spin.setFont(font)
        self.totalTests_spin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalTests_spin.setReadOnly(True)
        self.totalTests_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.totalTests_spin.setProperty("showGroupSeparator", True)
        self.totalTests_spin.setMaximum(999999999)
        self.totalTests_spin.setObjectName("totalTests_spin")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.totalTests_spin)
        self.totCase_label = QtWidgets.QLabel(self.cumulativeBox)
        font = QtGui.QFont()
        self.totCase_label.setFont(font)
        self.totCase_label.setObjectName("totCase_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.totCase_label)
        self.totalCases_spin = QtWidgets.QSpinBox(self.cumulativeBox)
        self.totalCases_spin.setMinimumSize(QtCore.QSize(170, 0))
        self.totalCases_spin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.totalCases_spin.setFont(font)
        self.totalCases_spin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalCases_spin.setReadOnly(True)
        self.totalCases_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.totalCases_spin.setProperty("showGroupSeparator", True)
        self.totalCases_spin.setMaximum(999999999)
        self.totalCases_spin.setObjectName("totalCases_spin")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.totalCases_spin)
        self.totDeaths_label = QtWidgets.QLabel(self.cumulativeBox)
        font = QtGui.QFont()
        self.totDeaths_label.setFont(font)
        self.totDeaths_label.setObjectName("totDeaths_label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.totDeaths_label)
        self.totalDeaths_spin = QtWidgets.QSpinBox(self.cumulativeBox)
        self.totalDeaths_spin.setMinimumSize(QtCore.QSize(170, 0))
        self.totalDeaths_spin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        self.totalDeaths_spin.setFont(font)
        self.totalDeaths_spin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalDeaths_spin.setReadOnly(True)
        self.totalDeaths_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.totalDeaths_spin.setProperty("showGroupSeparator", True)
        self.totalDeaths_spin.setMaximum(999999999)
        self.totalDeaths_spin.setObjectName("totalDeaths_spin")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.totalDeaths_spin)
        self.horizontalLayout.addWidget(self.cumulativeBox)
        self.verticalLayout.addWidget(self.splitter)
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setObjectName("btnHLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btnHLayout.addItem(spacerItem1)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        self.removeButton.setFont(font)
        self.removeButton.setObjectName("removeButton")
        self.btnHLayout.addWidget(self.removeButton)
        self.verticalLayout.addLayout(self.btnHLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 20))
        self.menubar.setObjectName("menubar")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menuDownload = QtWidgets.QMenu(self.menu_edit)
        self.menuDownload.setObjectName("menuDownload")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.closeAction = QtWidgets.QAction(MainWindow)
        self.closeAction.setObjectName("closeAction")
        self.actionSaveCSV = QtWidgets.QAction(MainWindow)
        self.actionSaveCSV.setObjectName("actionSaveCSV")
        self.actionSaveJson = QtWidgets.QAction(MainWindow)
        self.actionSaveJson.setObjectName("actionSaveJson")
        self.actionHow_data_are_collected = QtWidgets.QAction(MainWindow)
        self.actionHow_data_are_collected.setObjectName("actionHow_data_are_collected")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menuDownload.addAction(self.actionSaveCSV)
        self.menuDownload.addAction(self.actionSaveJson)
        self.menu_edit.addSeparator()
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menuDownload.menuAction())
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.closeAction)
        self.menuHelp.addAction(self.actionHow_data_are_collected)
        self.menuHelp.addAction(self.action_About)
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.countryLabel.setBuddy(self.country_edit)
        self.label.setBuddy(self.continent_edit)
        self.tests_label.setBuddy(self.newTest_spin)
        self.cases_label.setBuddy(self.newCases_spin)
        self.deaths_label.setBuddy(self.newDeaths_spin)
        self.totTests_label.setBuddy(self.totalTests_spin)
        self.totCase_label.setBuddy(self.totalCases_spin)
        self.totDeaths_label.setBuddy(self.totalDeaths_spin)

        self.retranslateUi(MainWindow)
        self.continent_box.setCurrentIndex(0)
        self.country_box.setCurrentIndex(0)
        self.closeAction.triggered['bool'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid19 data - Fz"))
        self.label_2.setText(_translate("MainWindow", "Select a filter"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.continent_box.setItemText(0, _translate("MainWindow", "Select a continent"))
        self.country_box.setToolTip(_translate("MainWindow", "Select a country to show details"))
        self.country_box.setCurrentText(_translate("MainWindow", "Select a country"))
        self.country_box.setItemText(0, _translate("MainWindow", "Select a country"))
        self.filter1Box.setTitle(_translate("MainWindow", "Date"))
        self.dateEdit_ro.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.dateEdit_text.setDisplayFormat(_translate("MainWindow", "dddd dd MMMM yyyy"))
        self.day_edit.setText(_translate("MainWindow", "Today"))
        self.queryBox.setTitle(_translate("MainWindow", "Local"))
        self.countryLabel.setText(_translate("MainWindow", "Cou&ntry"))
        self.label.setText(_translate("MainWindow", "Cont&inent"))
        self.run_sql_btn.setText(_translate("MainWindow", "Or run a SQL query (SQLite)"))
        self.dailyBox.setTitle(_translate("MainWindow", "Daily Report"))
        self.tests_label.setText(_translate("MainWindow", "New &Tests"))
        self.cases_label.setText(_translate("MainWindow", "New &cases"))
        self.deaths_label.setText(_translate("MainWindow", "New &Deaths"))
        self.cumulativeBox.setTitle(_translate("MainWindow", "Cumulative Report"))
        self.totTests_label.setText(_translate("MainWindow", "T&otal Tests"))
        self.totCase_label.setText(_translate("MainWindow", "Total Ca&ses"))
        self.totDeaths_label.setText(_translate("MainWindow", "Tota&l Deaths"))
        self.removeButton.setText(_translate("MainWindow", "&Refresh"))
        self.menu_edit.setTitle(_translate("MainWindow", "O&ptions"))
        self.menuDownload.setTitle(_translate("MainWindow", "Download all entries"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.closeAction.setText(_translate("MainWindow", "&Close"))
        self.closeAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSaveCSV.setText(_translate("MainWindow", "To CSV format"))
        self.actionSaveJson.setText(_translate("MainWindow", "To Json Format"))
        self.actionHow_data_are_collected.setText(_translate("MainWindow", "&How data are collected?"))
        self.action_About.setText(_translate("MainWindow", "&About"))
