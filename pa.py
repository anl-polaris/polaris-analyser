import os, sys
from PyQt4 import QtGui, QtCore
import ui_pa, ui_data_widget
import ReportItem2D
import Project
progname = os.path.basename(sys.argv[0])
progversion = "0.1"
import tree_manipulations
from QSEditor import QSEditor
from SqlExecuteThread import *

class DataWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = ui_data_widget.Ui_Form()
        self.ui.setupUi(self)
        

class ApplicationWindow(QtGui.QMainWindow):
    proj = None
    connected = False
    partDone = QtCore.pyqtSignal(int)
    allDone =  QtCore.pyqtSignal()
    message =  QtCore.pyqtSignal(str, str)
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_pa.Ui_MainWindow()
        self.ui.setupUi(self)
        self.editor = QSEditor()
        self.ui.mainVLayout.addWidget(self.editor)
        self.status_message = QtGui.QLabel("")
        self.db_status_message = QtGui.QLabel("")
        self.status_message.setMinimumSize(QtCore.QSize(80,20))
        self.db_status_message.setMinimumSize(QtCore.QSize(120,20))
        self.ui.statusbar.addWidget(self.status_message)
        self.ui.statusbar.addWidget(self.db_status_message)
        QtCore.QObject.connect(self.ui.actionNew, QtCore.SIGNAL("triggered()"), self.new)
        QtCore.QObject.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.save)
        QtCore.QObject.connect(self.ui.actionConnect, QtCore.SIGNAL("triggered()"), self.connect)
        QtCore.QObject.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.open)
        self.ui.treeWidget.itemClicked.connect(self.tree_clicked)
        self.ui.treeWidget.itemDoubleClicked.connect(self.tree_double_clicked)
        self.editor.textChanged.connect(self.editor_text_changed)
        self.load_from_file("c:\\users\\vsokolov\\test.pr")
    def update_status(self):
        self.status_message.setText("Project file: %s    Connected: %s"%(self.proj.filename, str(self.connect)))
        self.ui.statusbar.reformat()
    def update_db_status_done(self):
        self.db_status_message.setText("Done")
        self.ui.statusbar.reformat()
    def update_db_status(self, n):
        self.db_status_message.setText("Records Processed: %s"%str(n))
        self.ui.statusbar.reformat()
    def clear(self):
        for i in range(self.ui.plotLayout.count()): self.ui.plotLayout.itemAt(i).widget().close()
    def new(self):
        #self.clear()
        self.connect = False
        self.update_status()
        self.proj = Project.Project()
        self.editor.setText(self.proj.str)
        tree_manipulations.setup_tree(self.ui.treeWidget)
        tree_manipulations.populate_tree(self.proj, self.ui.treeWidget)
    def save_tree_item(self, item):
        if item.data(0,QtCore.Qt.UserRole+1).toString() != "":
            with open(str(item.data(0,QtCore.Qt.UserRole+1).toString()),'w') as fh:
                fh.write(str(item.data(0,QtCore.Qt.UserRole).toString()))
        for i in range(item.childCount()):
            self.save_tree_item(item.child(i))
    def save(self):
        tw = self.ui.treeWidget
        for i in range(tw.topLevelItemCount()):
            self.save_tree_item(tw.topLevelItem(i))

        #self.proj.PopulateFromString(str(self.editor.text()))
        #if self.proj.filename is None:
        #    self.proj.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save file', os.path.expanduser('~'),".pr")
        #with open(self.proj.filename,'w') as fh:
        #    fh.write(self.proj.str)
        #self.update_status()
    def connect(self):
        if self.proj is None:
            return
        conn_ok, message = self.proj.Connect()
        if not conn_ok:
            QtGui.QMessageBox.warning(None, 'Connection Error', message)
        else:
            self.connect = True
        self.update_status()
    def load_from_file(self, filename):
        if self.proj is None:
            self.proj = Project.Project()
        self.proj.filename = filename
        with open(self.proj.filename) as fh:
            self.proj.PopulateFromString(fh.read())
        self.editor.setText(self.proj.str)
        self.connect()
        tree_manipulations.populate_tree(self.proj, self.ui.treeWidget)
        self.connect = False
        self.update_status()
    def open(self): 
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser('~'),   "Project (*.pr)")
        if filename == "":
            return
        self.load_from_file(filename)
    def tree_clicked(self,item, column):
        self.editor.setText(item.data(0,QtCore.Qt.UserRole).toString())
    def tree_double_clicked(self,item,column):
        if item.parent().data(0,0).toString() == "Requirements":
            script = str(item.data(0,QtCore.Qt.UserRole).toString())
            self.update_db_status(0)
            name = item.data(0,0).toString()
            #print "Executing\n%s"%script
            #self.proj.conn.executescript(script)
            #print "Executed!"            
            self.th = GenericThread(self.apply_requirement, name, script)
            #QtCore.QObject.connect(th, QtCore.SIGNAL("finished ()"), self.update_requirements_status)
            #self.partDone.disconnect(self.update_db_status)
            self.partDone.connect(self.update_db_status)
            #self.allDone.disconnect(self.update_db_status_done)
            self.allDone.connect(self.update_db_status_done)
            self.message.connect(self.show_thread_message)
            self.th.start()
    def show_thread_message(self,head, msg):
        QtGui.QMessageBox.warning(None, head, msg)
    def update_requirements_status(self, name):
            self.proj.AddSatisfiedItems(name)
            tree_manipulations.colorize_requireents(self.proj, self.ui.treeWidget)
    def editor_text_changed(self):
        current_item =  self.ui.treeWidget.selectedItems()[0]
        current_item.setData(0, QtCore.Qt.UserRole,  self.editor.text())
    def status(self):
        self.count += 1
        self.partDone.emit(self.count*10000)    
    def apply_requirement(self,name, script):
        print "Executing %s"%script
        self.partDone.emit(0)        
        self.proj.conn.set_progress_handler(self.status,  10000)        
        try:
            print 1
            self.proj.conn.executescript(script)
            print 2
            self.update_requirements_status(name)
        except Exception as ex:
            self.message.emit("Script Execution Error", ex.message)
            self.partDone.emit(-1)
            return
        self.proj.conn.commit() 
        print "Commited to DB"       
        self.allDone.emit()
        return


qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
#aw.setWindowTitle("%s" % progname)
plot2d = ReportItem2D.DBPlot()
aw.ui.plotLayout.addWidget(plot2d)
plot2d.add_xy([1,2,3],[5,6,7])
aw.show()
sys.exit(qApp.exec_())
