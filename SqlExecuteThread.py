from PyQt4 import QtCore, QtGui


class SqlExecuteThread(QtCore.QThread):
    partDone = QtCore.pyqtSignal(int)
    allDone =  QtCore.pyqtSignal()
    def __init__(self, conn, script):
        QtCore.QThread.__init__(self)
        self.n = 1000
        self.count = 0
        self.conn = conn
        self.script = script
    def status(self):
        self.count += 1
        self.partDone.emit(self.count*self.n)
    def run(self):
        QtGui.QMessageBox.about(None, "Scrip", self.script)
        self.partDone.emit(0)        
        self.conn.set_progress_handler(self.status,  self.n)        
        self.conn.executescript(self.script)        
        self.conn.commit()        
        self.allDone.emit()
        return

