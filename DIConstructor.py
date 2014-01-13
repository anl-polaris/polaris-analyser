from data_item_constructor import Ui_DIConstructor
from PyQt4 import QtGui, QtCore
class DIConstructor(QtGui.QDialog, Ui_DIConstructor): 
    sql = None
    name = None
    def __init__(self, conn):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.addButton.clicked.connect(self.add)
        self.conn = conn
        self.whereText.setPlainText("type where statement here...")
        
        QtCore.QObject.connect(self.comboDB, QtCore.SIGNAL("currentIndexChanged(QString)"), self.populate_tables)
        QtCore.QObject.connect(self.comboTable, QtCore.SIGNAL("currentIndexChanged(QString)"), self.populate_xy)

        #get all of the databases in the connection
        res = self.conn.execute('PRAGMA database_list')
        ind = 0
        for item in res:
            self.comboDB.insertItem(ind,item[1])
            ind += 1
        if self.comboDB.count > 0:
            self.comboDB.setCurrentIndex(0)
    def populate_tables(self, db_name):
        #get all of the table names
        res = self.conn.execute('SELECT name FROM \'%s\'.sqlite_master WHERE type=\'table\' and rootpage < 10000 and rootpage!=0 and name NOT LIKE (\'sqlite%%\') order by name'%(str(db_name),)).fetchall()
        self.comboTable.clear()
        ind = 0
        for item in res:
            self.comboTable.insertItem(ind,item[0])
            ind += 1
    def populate_xy(self, table):
        if str(table) =="":
            return
        res = self.conn.execute('pragma table_info(%s)'%table).fetchall()
        ind = 0
        self.comboX.clear()
        self.comboY.clear()
        for item in res:
            if item[2] not in ["INTEGER", "REAL"]:
                continue
            self.comboX.insertItem(ind, item[1])
            self.comboY.insertItem(ind, item[1])
            ind += 1

    def add(self):
        xcol = self.comboX.currentText()
        ycol = self.comboY.currentText()
        table = self.comboTable.currentText()
        if str(self.whereText.toPlainText())=="type where statement here...":
            self.sql = 'select %s, %s from %s'%(xcol, ycol, table)
        else:
            self.sql = 'select %s, %s from %s where %s'%(xcol, ycol, table, str(self.whereText.toPlainText()))
        self.name = self.nameTextEdit.toPlainText ()
        self.close()
    @staticmethod
    def getValues(conn):
        dlg = DIConstructor(conn)
        res = dlg.exec_()
        return (dlg.sql, dlg.name, res == QtGui.QDialog.Accepted)