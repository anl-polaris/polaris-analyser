# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_db_plot.ui'
#
# Created: Tue Dec 17 15:44:48 2013
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

class Ui_DBPlot(object):
    def setupUi(self, DBPlot):
        DBPlot.setObjectName(_fromUtf8("DBPlot"))
        DBPlot.resize(636, 643)
        self.verticalLayout = QtGui.QVBoxLayout(DBPlot)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sqlText = QtGui.QPlainTextEdit(DBPlot)
        self.sqlText.setMaximumSize(QtCore.QSize(16777215, 60))
        self.sqlText.setObjectName(_fromUtf8("sqlText"))
        self.horizontalLayout.addWidget(self.sqlText)
        self.plotButton = QtGui.QPushButton(DBPlot)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout.addWidget(self.plotButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DBPlot)
        QtCore.QMetaObject.connectSlotsByName(DBPlot)

    def retranslateUi(self, DBPlot):
        DBPlot.setWindowTitle(_translate("DBPlot", "Form", None))
        self.plotButton.setText(_translate("DBPlot", "Plot", None))

