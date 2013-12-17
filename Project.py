from PyQt4 import QtGui
import os.path
import utils
import sqlite3
import ui_project_properties
from collections import OrderedDict
import json

class Project(object):
    str = None
    conn = None
    control_data = None
    """description of class"""
    def __init__(self):
        ud = os.path.expanduser('~')
        self.control_data = OrderedDict()
        self.control_data['name'] = "New Report Project"
        self.control_data['master_db'] = ud+'/db.sqlite'
        self.control_data['attach_db'] = (ud+'/db1.sqlite', ud+'/db2.sqlite')
        self.control_data['intmed_db'] = ud+'/intmed.sqlite'
        self.control_data['sql_path'] = ud+'/reports'
        self.str = json.dumps(self.control_data, indent=2, separators=(',',': '))
    def PopulateFromString(self, str):
        self.control_data = json.loads(str)
        self.str = str
        self.conn = None
    # returns (flag, message)
    def Connect(self):
        db_paths = []
        db_paths.append(self.control_data['master_db'])
        db_paths +=  self.control_data['attach_db']
        db_paths.append(self.control_data['intmed_db'])
        if len(db_paths) == 0:
            return (False, "No Master databse specified for the project.")
        #check that all of the databases exist but the intmed_db
        for item in db_paths[:len(db_paths)-1]:
            if not os.path.exists(item):
                return (False, "The specified database file %s does not exist."%item)
        try:
            #connect the master database
            conn = sqlite3.connect(db_paths[0])
            for item in db_paths[1:]:
                db_name = os.path.basename(item).split('.')[0] 
                conn.execute("ATTACH DATABASE '%s' as '%s'"%(item, db_name))
                #atatched_db.append(db_name)
            return (True, "OK")
        except Exception as ex:
            return (False, ex.message)