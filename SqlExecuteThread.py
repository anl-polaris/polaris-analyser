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
        #QtGui.QMessageBox.about(None, "Scrip", self.script)
        print "Executing %s"%self.script
        self.partDone.emit(0)        
        self.conn.set_progress_handler(self.status,  self.n)        
        try:
            self.conn.executescript(self.script)
        except Exception as ex:
            QtGui.QMessageBox.warning(None, "Error Executing Script", ex.message)
            self.partDone.emit(-1)
            return False
        self.conn.commit() 
        print "Commited to DB"       
        self.allDone.emit()
        return True

class GenericThread(QtCore.QThread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def __del__(self):
        self.wait()
    def run(self):
        self.function(*self.args,**self.kwargs)
        return