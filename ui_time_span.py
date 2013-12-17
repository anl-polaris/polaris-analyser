# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_time_span.ui'
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

class Ui_timeSpanDialog(object):
    def setupUi(self, timeSpanDialog):
        timeSpanDialog.setObjectName(_fromUtf8("timeSpanDialog"))
        timeSpanDialog.resize(254, 95)
        timeSpanDialog.setSizeGripEnabled(False)
        timeSpanDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(timeSpanDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.timeStart = QtGui.QTimeEdit(timeSpanDialog)
        self.timeStart.setTime(QtCore.QTime(7, 0, 0))
        self.timeStart.setObjectName(_fromUtf8("timeStart"))
        self.gridLayout.addWidget(self.timeStart, 0, 1, 1, 1)
        self.timeEnd = QtGui.QTimeEdit(timeSpanDialog)
        self.timeEnd.setTime(QtCore.QTime(8, 0, 0))
        self.timeEnd.setObjectName(_fromUtf8("timeEnd"))
        self.gridLayout.addWidget(self.timeEnd, 1, 1, 1, 1)
        self.label = QtGui.QLabel(timeSpanDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(timeSpanDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(timeSpanDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(timeSpanDialog)
        QtCore.QMetaObject.connectSlotsByName(timeSpanDialog)

    def retranslateUi(self, timeSpanDialog):
        timeSpanDialog.setWindowTitle(_translate("timeSpanDialog", "TimeSpan", None))
        self.label.setText(_translate("timeSpanDialog", "Start Time", None))
        self.label_2.setText(_translate("timeSpanDialog", "End Time", None))

