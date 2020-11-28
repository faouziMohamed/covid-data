# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 565)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(900, 568))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeView = QtWidgets.QTreeView(self.splitter)
        self.treeView.setMinimumSize(QtCore.QSize(0, 0))
        self.treeView.setObjectName("treeView")
        self.treeView.header().setCascadingSectionResizes(False)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.countryLabel = QtWidgets.QLabel(self.groupBox)
        self.countryLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.countryLabel.setObjectName("countryLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.countryLabel)
        self.hlayout1 = QtWidgets.QHBoxLayout()
        self.hlayout1.setObjectName("hlayout1")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setMinimumSize(QtCore.QSize(160, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.hlayout1.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.hlayout1.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole,
                                  self.hlayout1)
        self.testsLabel = QtWidgets.QLabel(self.groupBox)
        self.testsLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.testsLabel.setObjectName("testsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.testsLabel)
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.testSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.testSpinBox.setMinimumSize(QtCore.QSize(160, 30))
        self.testSpinBox.setWrapping(False)
        self.testSpinBox.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.testSpinBox.setAccelerated(True)
        self.testSpinBox.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.testSpinBox.setProperty("showGroupSeparator", True)
        self.testSpinBox.setMaximum(999999999)
        self.testSpinBox.setStepType(
            QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.testSpinBox.setObjectName("testSpinBox")
        self.hLayout2.addWidget(self.testSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(68, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.hLayout2.addItem(spacerItem1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole,
                                  self.hLayout2)
        self.casesLabel = QtWidgets.QLabel(self.groupBox)
        self.casesLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.casesLabel.setObjectName("casesLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.casesLabel)
        self.hLayout3 = QtWidgets.QHBoxLayout()
        self.hLayout3.setObjectName("hLayout3")
        self.casesSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.casesSpinBox.setMinimumSize(QtCore.QSize(160, 30))
        self.casesSpinBox.setWrapping(False)
        self.casesSpinBox.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.casesSpinBox.setAccelerated(True)
        self.casesSpinBox.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.casesSpinBox.setProperty("showGroupSeparator", True)
        self.casesSpinBox.setMaximum(999999999)
        self.casesSpinBox.setObjectName("casesSpinBox")
        self.hLayout3.addWidget(self.casesSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.hLayout3.addItem(spacerItem2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole,
                                  self.hLayout3)
        self.deathsLabel = QtWidgets.QLabel(self.groupBox)
        self.deathsLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.deathsLabel.setObjectName("deathsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.deathsLabel)
        self.hLayout4 = QtWidgets.QHBoxLayout()
        self.hLayout4.setObjectName("hLayout4")
        self.deathsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.deathsSpinBox.setMinimumSize(QtCore.QSize(160, 30))
        self.deathsSpinBox.setWrapping(False)
        self.deathsSpinBox.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.deathsSpinBox.setAccelerated(True)
        self.deathsSpinBox.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.deathsSpinBox.setProperty("showGroupSeparator", True)
        self.deathsSpinBox.setMaximum(999999999)
        self.deathsSpinBox.setObjectName("deathsSpinBox")
        self.hLayout4.addWidget(self.deathsSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(68, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.hLayout4.addItem(spacerItem3)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole,
                                  self.hLayout4)
        self.dateLabel = QtWidgets.QLabel(self.groupBox)
        self.dateLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                  self.dateLabel)
        self.hLayout5 = QtWidgets.QHBoxLayout()
        self.hLayout5.setObjectName("hLayout5")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setEnabled(True)
        self.dateEdit.setMinimumSize(QtCore.QSize(160, 30))
        self.dateEdit.setMouseTracking(True)
        self.dateEdit.setAutoFillBackground(True)
        self.dateEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateEdit.setWrapping(True)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setSpecialValueText("")
        self.dateEdit.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dateEdit.setKeyboardTracking(True)
        self.dateEdit.setProperty("showGroupSeparator", True)
        self.dateEdit.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2020, 11, 23), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(2019, 9, 30))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(2020, 11, 23))
        self.dateEdit.setObjectName("dateEdit")
        self.hLayout5.addWidget(self.dateEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.hLayout5.addItem(spacerItem4)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole,
                                  self.hLayout5)
        self.verticalLayout.addWidget(self.splitter)
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setObjectName("btnHLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.btnHLayout.addItem(spacerItem5)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.btnHLayout.addWidget(self.newButton)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.btnHLayout.addWidget(self.saveButton)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.btnHLayout.addWidget(self.removeButton)
        self.verticalLayout.addLayout(self.btnHLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 20))
        self.menubar.setObjectName("menubar")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menuDownload = QtWidgets.QMenu(self.menu_edit)
        self.menuDownload.setObjectName("menuDownload")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.saveAction = QtWidgets.QAction(MainWindow)
        self.saveAction.setObjectName("saveAction")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.closeAction = QtWidgets.QAction(MainWindow)
        self.closeAction.setObjectName("closeAction")
        self.actionSaveChanges = QtWidgets.QAction(MainWindow)
        self.actionSaveChanges.setObjectName("actionSaveChanges")
        self.actionSaveCSV = QtWidgets.QAction(MainWindow)
        self.actionSaveCSV.setObjectName("actionSaveCSV")
        self.actionSaveJson = QtWidgets.QAction(MainWindow)
        self.actionSaveJson.setObjectName("actionSaveJson")
        self.menuDownload.addAction(self.actionSaveCSV)
        self.menuDownload.addAction(self.actionSaveJson)
        self.menu_edit.addSeparator()
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menuDownload.menuAction())
        self.menu_edit.addAction(self.actionSaveChanges)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.closeAction)
        self.menubar.addAction(self.menu_edit.menuAction())
        self.countryLabel.setBuddy(self.comboBox)
        self.testsLabel.setBuddy(self.testSpinBox)
        self.casesLabel.setBuddy(self.casesSpinBox)
        self.deathsLabel.setBuddy(self.deathsSpinBox)
        self.dateLabel.setBuddy(self.dateEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BiblioApp"))
        self.groupBox.setTitle(_translate("MainWindow", "Details"))
        self.countryLabel.setText(_translate("MainWindow", "Cou&ntry"))
        self.comboBox.setItemText(0,
                                  _translate("MainWindow", "Select a country"))
        self.testsLabel.setText(_translate("MainWindow", "New &Tests"))
        self.casesLabel.setText(_translate("MainWindow", "New &cases"))
        self.deathsLabel.setText(_translate("MainWindow", "New &Deaths"))
        self.dateLabel.setText(_translate("MainWindow", "Da&te"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.newButton.setText(_translate("MainWindow", "&New"))
        self.saveButton.setText(_translate("MainWindow", "Sa&ve"))
        self.removeButton.setText(_translate("MainWindow", "&Remove"))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.menuDownload.setTitle(
            _translate("MainWindow", "Download all entries"))
        self.openAction.setText(_translate("MainWindow", "&Open"))
        self.openAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveAction.setText(_translate("MainWindow", "&Save"))
        self.saveAction.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.closeAction.setText(_translate("MainWindow", "&Close"))
        self.closeAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSaveChanges.setText(
            _translate("MainWindow", "&Save changes"))
        self.actionSaveCSV.setText(_translate("MainWindow", "To CSV format"))
        self.actionSaveJson.setText(_translate("MainWindow", "To Json Format"))
