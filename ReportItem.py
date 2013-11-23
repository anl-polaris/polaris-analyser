class ReportItem(object):
    """Represents a single item to be used for data analysis, such as 2D plot, table, bar chart or a single number"""
    #conn = (sqlite3.connection, [db1, db2, ..., dbn]), here db1, ..., dbn are attached databases
    def __init__(self, sql, conn):
        self.sql = sql
        self.requirements = []
        self.requiremnts_checked = False
        self.data_cashed = False
        self.conn = conn
    def add_requirement(self,req):
        self.requirements.append(req)
    def check_requirement(self,req):
        #get names of all of the tables
        tables = []
        if self.conn[0] == None:
            raise AttributeError('Database object basses to check_appy_requirements function is None')
        c = self.conn[0]
        tables = c.execute("SELECT tbl_name FROM sqlite_master WHERE type='table'").fetchall()
        for db in self.conn[1]:
            tables+=c.execute("SELECT tbl_name FROM %s.sqlite_master WHERE type='table'"%db).fetchall()
        #flatten the tables list
        tables = [item.lower() for sublist in tables for item in sublist] 
        table_required = req[0]
        columns_required = req[1]
        if (table_required.lower() not in tables):
            return False
        cols = c.execute('pragma table_info(%s)'%table_required).fetchall()
        #get the columns names
        cols =  zip(*cols)[1] 
        cols = [item.lower() for item in cols]
        for col in columns_required:
            if col.lower() not in cols:
                return False
        return True

    def apply_requirements(self):
        for req in self.requirements:  
            if not self.check_requirement(req) and req[2] != '':
                #apply necessary sql statement
                self.conn[0].execute(req[2])
                self.conn[0].commit()
            if not self.check_requirement(req):
                raise Exception("The statement specified %s does not generate necessary table %s and column column % to satisfy the requirement"%(req[2],req[1],req[0]))





