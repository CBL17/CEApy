# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchBox = QtWidgets.QPlainTextEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBox.sizePolicy().hasHeightForWidth())
        self.searchBox.setSizePolicy(sizePolicy)
        self.searchBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.searchBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchBox.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.searchBox.setObjectName("searchBox")
        self.verticalLayout.addWidget(self.searchBox)
        self.elementList = QtWidgets.QListWidget(self.widget)
        self.elementList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.elementList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.elementList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.elementList.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.elementList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.elementList.setObjectName("elementList")
        self.verticalLayout.addWidget(self.elementList)
        self.horizontalLayout_2.addWidget(self.widget)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.moleculeName = QtWidgets.QPlainTextEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moleculeName.sizePolicy().hasHeightForWidth())
        self.moleculeName.setSizePolicy(sizePolicy)
        self.moleculeName.setMaximumSize(QtCore.QSize(100, 25))
        self.moleculeName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.moleculeName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.moleculeName.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.moleculeName.setObjectName("moleculeName")
        self.horizontalLayout.addWidget(self.moleculeName)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.moleculeDescription = QtWidgets.QPlainTextEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moleculeDescription.sizePolicy().hasHeightForWidth())
        self.moleculeDescription.setSizePolicy(sizePolicy)
        self.moleculeDescription.setMaximumSize(QtCore.QSize(16777215, 25))
        self.moleculeDescription.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.moleculeDescription.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.moleculeDescription.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.moleculeDescription.setObjectName("moleculeDescription")
        self.horizontalLayout.addWidget(self.moleculeDescription)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.line_9 = QtWidgets.QFrame(self.groupBox)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_2.addWidget(self.line_9)
        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.elem1name = QtWidgets.QComboBox(self.widget_3)
        self.elem1name.setMinimumSize(QtCore.QSize(60, 0))
        self.elem1name.setEditable(False)
        self.elem1name.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.elem1name.setObjectName("elem1name")
        self.horizontalLayout_3.addWidget(self.elem1name)
        self.elem1amnt = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.elem1amnt.setDecimals(4)
        self.elem1amnt.setMaximum(99999.0)
        self.elem1amnt.setObjectName("elem1amnt")
        self.horizontalLayout_3.addWidget(self.elem1amnt)
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.elem2name = QtWidgets.QComboBox(self.widget_3)
        self.elem2name.setMinimumSize(QtCore.QSize(60, 0))
        self.elem2name.setEditable(False)
        self.elem2name.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.elem2name.setObjectName("elem2name")
        self.horizontalLayout_3.addWidget(self.elem2name)
        self.elem2amnt = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.elem2amnt.setDecimals(4)
        self.elem2amnt.setMaximum(99999.0)
        self.elem2amnt.setObjectName("elem2amnt")
        self.horizontalLayout_3.addWidget(self.elem2amnt)
        self.line_2 = QtWidgets.QFrame(self.widget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.elem3name = QtWidgets.QComboBox(self.widget_3)
        self.elem3name.setMinimumSize(QtCore.QSize(60, 0))
        self.elem3name.setEditable(False)
        self.elem3name.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.elem3name.setObjectName("elem3name")
        self.horizontalLayout_3.addWidget(self.elem3name)
        self.elem3amnt = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.elem3amnt.setDecimals(4)
        self.elem3amnt.setMaximum(99999.0)
        self.elem3amnt.setObjectName("elem3amnt")
        self.horizontalLayout_3.addWidget(self.elem3amnt)
        self.line_4 = QtWidgets.QFrame(self.widget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_3.addWidget(self.line_4)
        self.elem4name = QtWidgets.QComboBox(self.widget_3)
        self.elem4name.setMinimumSize(QtCore.QSize(60, 0))
        self.elem4name.setEditable(False)
        self.elem4name.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.elem4name.setObjectName("elem4name")
        self.horizontalLayout_3.addWidget(self.elem4name)
        self.elem4amnt = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.elem4amnt.setDecimals(4)
        self.elem4amnt.setMaximum(99999.0)
        self.elem4amnt.setObjectName("elem4amnt")
        self.horizontalLayout_3.addWidget(self.elem4amnt)
        self.line_5 = QtWidgets.QFrame(self.widget_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_3.addWidget(self.line_5)
        self.elem5name = QtWidgets.QComboBox(self.widget_3)
        self.elem5name.setMinimumSize(QtCore.QSize(60, 0))
        self.elem5name.setEditable(False)
        self.elem5name.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.elem5name.setObjectName("elem5name")
        self.horizontalLayout_3.addWidget(self.elem5name)
        self.elem5amnt = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.elem5amnt.setDecimals(4)
        self.elem5amnt.setMaximum(99999.0)
        self.elem5amnt.setObjectName("elem5amnt")
        self.horizontalLayout_3.addWidget(self.elem5amnt)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.line_8 = QtWidgets.QFrame(self.groupBox)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.widget_5 = QtWidgets.QWidget(self.groupBox)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.condensedBox = QtWidgets.QCheckBox(self.widget_5)
        self.condensedBox.setObjectName("condensedBox")
        self.horizontalLayout_5.addWidget(self.condensedBox)
        self.line_7 = QtWidgets.QFrame(self.widget_5)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_5.addWidget(self.line_7)
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.baseTempBox = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.baseTempBox.setMinimum(10.0)
        self.baseTempBox.setMaximum(99999.0)
        self.baseTempBox.setProperty("value", 298.15)
        self.baseTempBox.setObjectName("baseTempBox")
        self.horizontalLayout_5.addWidget(self.baseTempBox)
        self.line_3 = QtWidgets.QFrame(self.widget_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.molWeightBox = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.molWeightBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.molWeightBox.setDecimals(7)
        self.molWeightBox.setObjectName("molWeightBox")
        self.horizontalLayout_5.addWidget(self.molWeightBox)
        self.line_6 = QtWidgets.QFrame(self.widget_5)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_5.addWidget(self.line_6)
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.heatFormationBox = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.heatFormationBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.heatFormationBox.setDecimals(3)
        self.heatFormationBox.setSingleStep(1.0)
        self.heatFormationBox.setObjectName("heatFormationBox")
        self.horizontalLayout_5.addWidget(self.heatFormationBox)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.line_10 = QtWidgets.QFrame(self.groupBox)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_2.addWidget(self.line_10)
        spacerItem = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.widget_4 = QtWidgets.QWidget(self.groupBox)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveButton = QtWidgets.QPushButton(self.widget_4)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.clearButton = QtWidgets.QPushButton(self.widget_4)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_4.addWidget(self.clearButton)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCompile = QtWidgets.QAction(MainWindow)
        self.actionCompile.setObjectName("actionCompile")
        self.actionElements_Alphabetical_Order = QtWidgets.QAction(MainWindow)
        self.actionElements_Alphabetical_Order.setCheckable(True)
        self.actionElements_Alphabetical_Order.setObjectName("actionElements_Alphabetical_Order")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionCompile)
        self.menuView.addAction(self.actionElements_Alphabetical_Order)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchBox.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.groupBox.setTitle(_translate("MainWindow", "Edit Molecule"))
        self.label.setText(_translate("MainWindow", "Molecule Name"))
        self.moleculeName.setPlaceholderText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Molecule Description"))
        self.moleculeDescription.setPlaceholderText(_translate("MainWindow", "Description"))
        self.label_3.setText(_translate("MainWindow", "Elements:"))
        self.elem1name.setPlaceholderText(_translate("MainWindow", "Element"))
        self.elem2name.setPlaceholderText(_translate("MainWindow", "Element"))
        self.elem3name.setPlaceholderText(_translate("MainWindow", "Element"))
        self.elem4name.setPlaceholderText(_translate("MainWindow", "Element"))
        self.elem5name.setPlaceholderText(_translate("MainWindow", "Element"))
        self.condensedBox.setToolTip(_translate("MainWindow", "Chcek if the molecule is in condensed phase (liquid/solid). Unchecked if in gaseous phase."))
        self.condensedBox.setText(_translate("MainWindow", "Is Condensed?"))
        self.label_4.setToolTip(_translate("MainWindow", "The temperature that these properties are defined at. Valid use is +- 10K of this temperature"))
        self.label_4.setText(_translate("MainWindow", "Defined Temp (K):"))
        self.baseTempBox.setToolTip(_translate("MainWindow", "The temperature that these properties are defined at. Valid use is +- 10K of this temperature"))
        self.label_5.setText(_translate("MainWindow", "Molecular Weight (g/mol): "))
        self.label_6.setText(_translate("MainWindow", "Heat of Formation (J/mol):"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open Other"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCompile.setText(_translate("MainWindow", "Compile"))
        self.actionElements_Alphabetical_Order.setText(_translate("MainWindow", "Elements Alphabetical Order"))
