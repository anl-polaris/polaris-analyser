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
    filename = None
    """description of class"""
    def __init__(self):
        ud = os.path.expanduser('~')
        self.control_data = OrderedDict()
        self.control_data['name'] = "New Report Project"
        self.control_data['master_db'] = ud+'/db.sqlite'
        self.control_data['attach_db'] = [[ud+'/db1.sqlite','db1'], [ud+'/db2.sqlite','db2']]
        self.control_data['intmed_db'] = ud+'/intmed.sqlite'
        self.control_data['sql_path'] = ud+'/reports'
        self.str = json.dumps(self.control_data, indent=2, separators=(',',': '))
    def PopulateFromString(self, str):
        self.control_data = json.loads(str)
        self.str = str
        self.conn = None
    def SatisfiedItems(self):
        if self.conn is None:
            return None
        else:
            i =  self.conn.execute("select name from intmed.req where satisfied=1").fetchall()
            return [x[0] for x in i] 
    def AddSatisfiedItems(self,name):
        self.conn.execute("insert into intmed.req values (?,?)",(str(name), True))

    # returns (flag, message)
    def Connect(self):
        db_paths = []
        db_paths.append(self.control_data['master_db'])
        db_paths +=  self.control_data['attach_db']
        db_paths.append(self.control_data['intmed_db'])
        if len(db_paths) == 0:
            return (False, "No Master databse specified for the project.")
        #check that all of the databases exist but the intmed_db
        n = len(db_paths)
        for item in db_paths[:n-1]:
            if not os.path.exists(item):
                return (False, "The specified database file %s does not exist."%item)
        try:
            #connect the master database
            print "Connecting to: %s"%db_paths[0]
            self.conn = sqlite3.connect(db_paths[0], check_same_thread=False)
            self.conn.enable_load_extension(1)
            self.conn.load_extension('libspatialite-4.dll')
            for item in db_paths[1:n-1]:
                db_name = os.path.basename(item).split('.')[0] 
                print "ATTACH DATABASE '%s' as '%s'"%(item, db_name)
                self.conn.execute("ATTACH DATABASE '%s' as '%s'"%(item, db_name))
            print "ATTACH DATABASE '%s' as '%s'"%(db_paths[n-1], "intmed")
            self.conn.execute("ATTACH DATABASE '%s' as '%s'"%(db_paths[n-1], "intmed"))
            self.conn.execute("create table if not exists intmed.req (name text, satisfied bool)")
                #atatched_db.append(db_name)
            return (True, "OK")
        except Exception as ex:
            return (False, ex.message)