import os, sys
from PyQt4 import QtGui, QtCore
import ui_pa, ui_data_widget
import ReportItem2D
import Project
progname = os.path.basename(sys.argv[0])
progversion = "0.1"
import tree_manipulations
from QSEditor import QSEditor

class DataWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = ui_data_widget.Ui_Form()
        self.ui.setupUi(self)
        

class ApplicationWindow(QtGui.QMainWindow):
    proj_path = ""
    proj = None
    connected = False
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_pa.Ui_MainWindow()
        self.ui.setupUi(self)
        self.editor = QSEditor()
        self.ui.mainVLayout.addWidget(self.editor)
        self.status_message = QtGui.QLabel("")
        self.status_message.setMinimumSize(QtCore.QSize(80,20))
        self.ui.statusbar.addWidget(self.status_message)
        QtCore.QObject.connect(self.ui.actionNew, QtCore.SIGNAL("triggered()"), self.new)
        QtCore.QObject.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.save)
        QtCore.QObject.connect(self.ui.actionConnect, QtCore.SIGNAL("triggered()"), self.connect)
        QtCore.QObject.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.open)
    def update_status(self):
        self.status_message.setText("Project file: %s    Connected: %s"%(self.proj_path, str(self.connect)))
        self.ui.statusbar.reformat()
    def clear(self):
        for i in range(self.ui.plotLayout.count()): self.ui.plotLayout.itemAt(i).widget().close()
    def new(self):
        #self.clear()
        self.proj_path = ""
        self.connect = False
        self.update_status()
        self.proj = Project.Project()
        self.editor.setText(self.proj.str)
        tree_manipulations.setup_tree(self.ui.treeWidget)
        tree_manipulations.populate_tree(self.proj, self.ui.treeWidget)
    def save(self):
        self.proj.PopulateFromString(str(self.editor.text()))
        if self.proj_path == "":
            self.proj_path = QtGui.QFileDialog.getSaveFileName(self, 'Save file', os.path.expanduser('~'),".pr")
        with open(self.proj_path,'w') as fh:
            fh.write(self.proj.str)
        self.update_status()
    def connect(self):
        if self.proj is None:
            return
        conn_ok, message = self.proj.Connect()
        if not conn_ok:
            QtGui.QMessageBox.warning(None, 'Connection Error', message)
        else:
            self.connect = True
        self.update_status()
    def open(self):
        if self.proj is None:
            self.proj = Project.Project()
        self.proj_path = QtGui.QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser('~'),".pr")
        with open(self.proj_path) as fh:
            self.proj.PopulateFromString(fh.read())
        self.editor.setText(self.proj.str)
        self.connect = False
        self.update_status()






qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
plot2d = ReportItem2D.DBPlot()
aw.ui.plotLayout.addWidget(plot2d)
plot2d.add_xy([1,2,3],[5,6,7])
aw.show()
sys.exit(qApp.exec_())
