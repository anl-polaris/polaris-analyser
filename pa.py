import os, sys
from PyQt4 import QtGui, QtCore
import ui_pa, ui_data_widget
import ReportItem2D
import Project
progname = os.path.basename(sys.argv[0])
progversion = "0.1"

class DataWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = ui_data_widget.Ui_Form()
        self.ui.setupUi(self)
        

class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_pa.Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.actionNew, QtCore.SIGNAL("triggered()"), self.new)
    def clear(self):
        for i in range(self.ui.plotLayout.count()): self.ui.plotLayout.itemAt(i).widget().close()
    def new(self):
        self.clear()
        pr = Project.Project()
        pw = Project.ProjectWidget()
        pw.SetText(pr.xml_string)
        aw.ui.plotLayout.addWidget(pw)
        
        
qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
plot2d = ReportItem2D.DBPlot()
aw.ui.plotLayout.addWidget(plot2d)
plot2d.add_xy([1,2,3],[5,6,7])
aw.show()
sys.exit(qApp.exec_())
