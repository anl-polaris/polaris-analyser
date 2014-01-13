# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_item_constructor.ui'
#
# Created: Mon Jan 13 01:05:04 2014
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

class Ui_DIConstructor(object):
    def setupUi(self, DIConstructor):
        DIConstructor.setObjectName(_fromUtf8("DIConstructor"))
        DIConstructor.resize(346, 268)
        self.horizontalLayout = QtGui.QHBoxLayout(DIConstructor)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(DIConstructor)
        self.groupBox.setEnabled(True)
        self.groupBox.setMaximumSize(QtCore.QSize(350, 250))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.comboX = QtGui.QComboBox(self.groupBox)
        self.comboX.setMinimumSize(QtCore.QSize(200, 0))
        self.comboX.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboX.setObjectName(_fromUtf8("comboX"))
        self.gridLayout_2.addWidget(self.comboX, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.nameTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.nameTextEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.nameTextEdit.setObjectName(_fromUtf8("nameTextEdit"))
        self.gridLayout_2.addWidget(self.nameTextEdit, 4, 1, 1, 1)
        self.whereText = QtGui.QPlainTextEdit(self.groupBox)
        self.whereText.setMinimumSize(QtCore.QSize(0, 60))
        self.whereText.setMaximumSize(QtCore.QSize(16777215, 60))
        self.whereText.setMaximumBlockCount(0)
        self.whereText.setObjectName(_fromUtf8("whereText"))
        self.gridLayout_2.addWidget(self.whereText, 5, 1, 1, 1)
        self.addButton = QtGui.QPushButton(self.groupBox)
        self.addButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout_2.addWidget(self.addButton, 7, 1, 1, 1)
        self.comboY = QtGui.QComboBox(self.groupBox)
        self.comboY.setMinimumSize(QtCore.QSize(200, 0))
        self.comboY.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboY.setObjectName(_fromUtf8("comboY"))
        self.gridLayout_2.addWidget(self.comboY, 3, 1, 1, 1)
        self.comboTable = QtGui.QComboBox(self.groupBox)
        self.comboTable.setMinimumSize(QtCore.QSize(200, 0))
        self.comboTable.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboTable.setObjectName(_fromUtf8("comboTable"))
        self.gridLayout_2.addWidget(self.comboTable, 1, 1, 1, 1)
        self.comboDB = QtGui.QComboBox(self.groupBox)
        self.comboDB.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboDB.setObjectName(_fromUtf8("comboDB"))
        self.gridLayout_2.addWidget(self.comboDB, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(DIConstructor)
        QtCore.QMetaObject.connectSlotsByName(DIConstructor)

    def retranslateUi(self, DIConstructor):
        DIConstructor.setWindowTitle(_translate("DIConstructor", "Form", None))
        self.label.setText(_translate("DIConstructor", "Table", None))
        self.label_3.setText(_translate("DIConstructor", "Y", None))
        self.label_4.setText(_translate("DIConstructor", "Name", None))
        self.label_2.setText(_translate("DIConstructor", "X", None))
        self.whereText.setDocumentTitle(_translate("DIConstructor", "Where Statement", None))
        self.addButton.setText(_translate("DIConstructor", "Add", None))
        self.label_5.setText(_translate("DIConstructor", "Database", None))
        self.label_6.setText(_translate("DIConstructor", "WHERE", None))

