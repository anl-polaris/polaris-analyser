# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pa.ui'
#
# Created: Mon Dec 16 19:18:48 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(766, 539)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/polaris/icons/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainVLayout = QtGui.QVBoxLayout()
        self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout.addWidget(self.treeWidget)
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.horizontalLayout.addLayout(self.plotLayout)
        self.mainVLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.mainVLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPopulate = QtGui.QAction(MainWindow)
        self.actionPopulate.setObjectName(_fromUtf8("actionPopulate"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuProject.addAction(self.actionConnect)
        self.menuProject.addAction(self.actionPopulate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Polaris Analyser", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuProject.setTitle(_translate("MainWindow", "Project", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionPopulate.setText(_translate("MainWindow", "Populate", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))

import resources_rc
