from PyQt4 import QtGui
import os.path
import utils
import sqlite3
import ui_project_properties
class Project(object):
    str = None
    proj_file = ""
    db_paths = []
    ri_paths = []
    conn = None
    """description of class"""
    def __init__(self):
        ud = os.path.expanduser('~')
        self.str = """"
        Name = New Report Project
        MyLocation = %s
        MasterDB =   %s
        AttachDB =   %s
        AttachDB =   %s
        ReportItem = reportitem1.txt
        ReportItem = reportitem2.txt
        ReportItem = reportitem3.txt
        ReportItem = reportitem4.txt
        ReportItem = reportitem5.txt
        """%(ud,ud+'/db.sqlite',ud+'/db1.sqlite', ud+'/db2.sqlite')
        self.PopulateFromString()
    def Reset(self):
        self.proj_file = ""
        self.proj_file = ""
        self.db_paths = []
        self.ri_paths = []
        conn = None
    def PopulateFromString(self):
        self.Reset()
        (k,v) = utils.FromString(self.str)
        for i in utils.Indeces(k,'reportitem'):
            self.ri_paths.append(v[i])
        i = k.index('masterdb')
        self.db_paths.append(v[i])
        for i in utils.Indeces(k,'attachdb'):
            self.db_paths.append(v[i])
    def Connect(self):
        if len(self.db_paths) == 0:
            raise Exception("No Master databse specified for the project.")
        #check that all of the databases exist 
        for item in self.db_paths:
            if not os.path.exists(item):
                raise Exception("The specified database file %s does not exist."%item)
        #connect the master database
        conn = sqlite3.connect(self.db_paths[0])
        attached_db = []
        for item in self.db_paths[1:]:
            db_name = os.path.basename(item).split('.')[0] 
            conn.execute("ATTACH DATABASE '%s' as '%s'"%(item, db_name))
            atatched_db.append(db_name)
        self.conn = (conn, attached_db)







class ProjectWidget(QtGui.QWidget): 
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = ui_project_properties.Ui_Form()
        self.ui.setupUi(self)
    def SetText(self, text):
        self.ui.textEdit.setText(text) 