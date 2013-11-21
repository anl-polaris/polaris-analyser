from PyQt4 import QtCore, QtGui, QtSql
from ui_polaris import Ui_Polaris
from geo_tools import *
from  qgis.core import *
from  qgis.utils import *
import os
import matplotlib
import numpy as np
import pylab as P
import random
import math
import mpl
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
from db_plot import Ui_DBPlot
from db_plot1 import Ui_DBPlot1
from ui_time_span import Ui_timeSpanDialog
import re
class CreateLayerTread(QtCore.QThread):
    partDone = QtCore.pyqtSignal(int)
    allDone = QtCore.pyqtSignal()
    def __init__(self, db_path, start_time, end_time):
        QtCore.QThread.__init__(self)
        self.db_path = db_path
        self.n = 1000000
        self.count = 0
        self.start_time = start_time
        self.end_time = end_time
        QtGui.QMessageBox.about(None, "Generating Layer", "Start time: %s\nEnd time: %s"%(str(self.start_time), str(self.end_time)))
    def status(self):
        self.count += 1
        self.partDone.emit(self.count*self.n)
        #self.emit( QtCore.SIGNAL('update(QString)'), str(self.count*self.n) )

    def run(self):
        self.partDone.emit(0)
        
        #self.conn = sqlite3.connect(fileName)
        self.conn = sqlite3.connect(self.db_path)
        #QtGui.QMessageBox.about(self, "My message box", "Connected")     
        #QtGui.Message.about(self, "1", "2")
        self.partDone.emit(2)
        c = sqlite3.connect('../test_case/chicago-Result.sqlite')
        c.enable_load_extension(1)
        self.partDone.emit(3)
        c.load_extension('./spatialite4.dll')
        self.partDone.emit(4)
        if int(c.execute("select CheckSpatialMetaData()").fetchone()[0] ) != 3: 
            c.execute("select InitSpatialMetaData()")
        self.partDone.emit(5)
        c.execute("select DiscardGeometryColumn('link_moe', 'GEO')")
        self.partDone.emit(6)
        c.execute("drop table if exists link_moe")
        self.partDone.emit(7)
        c.commit()
        self.partDone.emit(8)
        self.conn.execute("attach database \'../test_case/chicago-Result.sqlite\' as res")
        #self.conn.execute("create table res.link_moe as select GEO, link, type, fspd_ab, fspd_ba, lanes_ab, lanes_ba from link")
        self.conn.set_progress_handler(self.status,  self.n)        
        c.set_progress_handler(self.status,  self.n)        
        self.partDone.emit(9)
        self.conn.execute("""create table res.link_moe as 
        select 
        GEO, 
        link_uid, 
        avg(link_travel_time) as tt,
        avg(link_queue_length) as link_queue_length,
        avg(link_travel_delay) as link_travel_delay,
        avg(link_speed) as link_speed,
        avg(link_density) as link_density,
        avg(link_in_flow_rate) as link_in_flow_rate,
        avg(link_out_flow_rate) as link_out_flow_rate,
        avg(link_in_volume) as link_in_volume,
        avg(link_out_volume) as link_out_volume,
        avg(link_speed_ratio) as link_speed_ratio,
        avg(link_in_flow_ratio) as link_in_flow_ratio,
        avg(link_out_flow_ratio) as link_out_flow_ratio,
        avg(link_density_ratio) as link_density_ratio,
        avg(link_travel_time_ratio) as link_travel_time_ratio,
        avg(num_vehicles_in_link) as num_vehicles_in_link,
        avg(link_speed) as link_speed
        from LinkMOE, link 
        where start_time < ? and start_time > ? and link.link == LinkMOE.link_uid/2 and lanes_ab > 0 
        group by link_uid""", (self.end_time, self.start_time,))        
        self.conn.commit()        
        c.execute("select RecoverGeometryColumn('link_moe', 'GEO',  26916, 'LINESTRING', 'XY')")
        c.commit()
        c.close()
        self.allDone.emit()
        return

class DBPlot1(QtGui.QWidget): 
    def __init__(self, conn):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_DBPlot1()
        self.ui.setupUi(self)
        self.ui.plotButton.clicked.connect(self.plot_xy)
        self.fig = mpl.MyMplCanvas(self, width=6, height=5, dpi=100)
        self.ui.verticalLayout.addWidget(self.fig.mpl_toolbar)
        self.ui.verticalLayout.addWidget(self.fig)
        self.conn = conn
        self.ui.whereText.setPlainText("type where statement here...")
        ind = 0
        res = self.conn.execute('SELECT name FROM sqlite_master WHERE type=\'table\' and rootpage < 10000 and rootpage!=0 and name NOT LIKE (\'sqlite%\') order by name ').fetchall()
        for item in res:
            self.ui.comboTable.insertItem(ind,item[0])
            ind += 1
        res = self.conn.execute('SELECT name FROM res.sqlite_master WHERE type=\'table\' and rootpage < 10000 and rootpage!=0 and name NOT LIKE (\'sqlite%\') order by name ').fetchall()
        for item in res:
            self.ui.comboTable.insertItem(ind,item[0])
            ind += 1
        QtCore.QObject.connect(self.ui.comboTable, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.populate_xy)
    def populate_xy(self, table):
        res = self.conn.execute('pragma table_info(%s)'%table).fetchall()
        ind = 0
        self.ui.comboX.clear()
        self.ui.comboY.clear()
        for item in res:
            if item[2] not in ["INTEGER", "REAL"]:
                continue
            self.ui.comboX.insertItem(ind, item[1])
            self.ui.comboY.insertItem(ind, item[1])
            ind += 1

        pass
    def plot_xy(self, text):
        self.fig.axes.clear()
        xcol = self.ui.comboX.currentText()
        ycol = self.ui.comboY.currentText()
        table = self.ui.comboTable.currentText()
        res = self.conn.execute('select %s, %s from %s where %s'%(xcol, ycol, table, str(self.ui.whereText.toPlainText()))).fetchall()
        x = []
        y = []
        for item in res:
            x.append(item[0])
            y.append(item[1])
        self.fig.axes.plot(x,y,'*')
        self.fig.axes.set_xlabel(str(xcol).capitalize())
        self.fig.axes.set_ylabel(str(ycol).capitalize())
        self.fig.draw()

class TimeSpanDialog(QtGui.QDialog):
    ok_signal = QtCore.pyqtSignal(int, int)
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_timeSpanDialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
    def accept(self):
        start = self.ui.timeStart.time()
        end = self.ui.timeEnd.time()
        start_sec = start.hour()*60*60 + start.minute()*60 + start.second()
        end_sec = end.hour()*60*60 + end.minute()*60 + end.second()
        #QtGui.QMessageBox.about(self, "Debug", str(start_sec))
        #QtGui.QMessageBox.about(self, "Debug", str(end_sec))
        self.ok_signal.emit(start_sec,end_sec)
        self.close()


#DD MATPLOTLIB TO THE db plot widget
class DBPlot(QtGui.QWidget): 
    def __init__(self, conn):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_DBPlot()
        self.ui.setupUi(self)
        self.ui.plotButton.clicked.connect(self.plot_xy)
        self.fig = mpl.MyMplCanvas(self, width=6, height=5, dpi=100)
        self.ui.verticalLayout.addWidget(self.fig.mpl_toolbar)
        self.ui.verticalLayout.addWidget(self.fig)
        self.conn = conn
         
    def plot_xy(self, text):
        self.fig.axes.clear()
        t = str(self.ui.sqlText.toPlainText())
        m = re.search("\s*select\s*(\w+)\s*\,\s*(\w+)", t)
        xlabel = m.group(1)
        ylabel = m.group(1)
        res = self.conn.execute(t).fetchall()
        x = []
        y = []
        for item in res:
            x.append(item[0])
            y.append(item[1])
        self.fig.axes.plot(x,y,'*')
        self.fig.axes.set_xlabel(str(xlabel).capitalize())
        self.fig.axes.set_ylabel(str(ylabel).capitalize())
        self.fig.draw()

# create the dialog for the plugin builder
class PolarisDialog(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.conn = None
        self.tabs = {}
        self.layouts = {}
        # Set up the user interface from Designer.        
        self.ui = Ui_Polaris()
        self.ui.setupUi(self)
        self.ver_progress = QtGui.QHBoxLayout(self)
        self.progress_bar = QtGui.QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.ui.statusbar.addWidget(self.progress_bar)
        self.status_message = QtGui.QLabel("")
        self.status_message.setMinimumSize(QtCore.QSize(80,20))
        self.ui.statusbar.addWidget(self.status_message)
        self.ui.actionConnect_TestCase.triggered.connect(self.connect)
        self.ui.actionDraw.triggered.connect(self.draw_tt)
        self.ui.actionQuit.triggered.connect(self.fileQuit)
        self.ui.actionNew_XY_DB_Plot.triggered.connect(self.db_plot)
        self.ui.actionNew_XY_DB_Plot_1.triggered.connect(self.db_plot_1)
        self.ui.actionTravel_Time_Layer.triggered.connect(self.crate_new_layer)
        self.connect()
        self.draw_all()
        self.db_table(self.dbfileName,"1", "County/Class VMT", "select county as COUNTY, link_type as TYPE, sum(link_vmt) as VMT from link_vmt group by county, link_type order by county, link_type")
        self.db_table(self.dbfileName,"3", "Class VMT","select link_type as TYPE, sum(link_vmt) as VMT from link_vmt group by link_type order by link_type")
        self.db_table(self.dbfileName,"5", "County VMT", "select county as COUNTY, sum(link_vmt) as VMT from link_vmt group by county")
    def fileQuit(self):
        self.close()
    def create_tab(self,tab_tag, tab_name):
        self.tabs[tab_tag] = QtGui.QWidget()
        self.tabs[tab_tag].setObjectName(_fromUtf8(tab_name))
        layout_tag = tab_tag+"Layout"
        self.layouts[layout_tag] = QtGui.QVBoxLayout(self.tabs[tab_tag])
        self.layouts[layout_tag].setObjectName(_fromUtf8(layout_tag))
        self.ui.tabWidget.addTab(self.tabs[tab_tag], _fromUtf8(tab_name))                
    def db_table(self,dbfileName, tag, name,sql):
        self.create_tab(tag, name)
        tv = QtGui.QTableView(self)
        tv.setObjectName(_fromUtf8(tag+"tableView"))
        self.layouts[tag+"Layout"].addWidget(tv)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(dbfileName)
        QtGui.QMessageBox.about(None, "POLARIS", dbfileName)
        if not db.open():
            QtGui.QMessageBox.warning(None, "POLARIS",
                QString("Database Error: %1").arg(db.lastError().text()))
        model = QtSql.QSqlTableModel(None, db)
        sql_prepared = QtSql.QSqlQuery(sql)
        model.setQuery(sql_prepared)
        #model.setTable("Link")
        model.select()
        #QtGui.QMessageBox.about(None,"POLARIS", "Statement: "+model.selectStatement())
        #QtGui.QMessageBox.about(None,"POLARIS", "Name: "+self.dbfileName)
        tv.setModel(model)
        #tv.show()
        del db
        return tv
    def db_plot(self):
        self.create_tab("db_plot", "DB Plot")
        dbp = DBPlot(self.conn)
        self.layouts["db_plotLayout"].addWidget(dbp)
    def db_plot_1(self):
        self.create_tab("db_plot_1", "DB Plot 1")
        dbp = DBPlot1(self.conn)
        self.layouts["db_plot_1Layout"].addWidget(dbp)
    def load_recent(self):
        home = os.path.expanduser("~")
        home += "/.polaris"
        if not os.path.exists(home):
            os.makedirs(home)
            with open(home+'/recent', 'w') as fh: #create empty file
                pass
        with open(home+'/recent', 'r') as fh:
             self.recent_db.add(item)
    def draw_tt(self):
        x = []
        y = []
        tt = self.conn.execute("select * from TTime_Distribution order by TTime_minutes").fetchall()
        for item in tt:
            tt,count = item
            x.append(int(tt))
            y.append(int(count))
            #y.append(math.log10(int(count)))   
        self.create_tab("ttTab", "Travel Time")
        fig = mpl.MyMplCanvas(self.tabs["ttTab"], width=5, height=4, dpi=100)
        self.layouts["ttTabLayout"].addWidget(fig.mpl_toolbar)
        self.layouts["ttTabLayout"].addWidget(fig)       
        fig.axes.plot(x,y, '*-')
        fig.axes.set_xlabel("Trevel Time (min)")
        fig.axes.set_ylabel("Vehicle Count")
    def treat_null(self, value):
        if value is None:
            return 0
        else:
            return value
    def draw_mode(self):
        data = self.conn.execute("select * from Mode_Distribution").fetchall()
        types = []
        autos = []
        transits = []
        for item in data:
            type, auto, transit, total = map(self.treat_null, item)
            type = type[0]
            autos.append(auto)
            types.append(type)
            transits.append(transit)
        self.create_tab("atTab", "Activity Type")
        fig = mpl.MyMplCanvas(self.tabs["atTab"], width=5, height=4, dpi=100)
        self.layouts["atTabLayout"].addWidget(fig.mpl_toolbar)
        self.layouts["atTabLayout"].addWidget(fig)       

        N = len(types)
        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        fig.axes.set_xticks(ind+width)
        fig.axes.set_xticklabels( types )
        ar = fig.axes.bar(ind, autos, width, color='r')
        tr = fig.axes.bar(ind+width, transits, width, color='y')
        fig.axes.legend( (ar[0], tr[0]), ('Auto', 'Transit') )
        fig.axes.set_xlabel("Activity Type")
        fig.axes.set_ylabel("Trip Count")
    def draw_all(self):
        self.draw_tt()
        self.draw_mode()
    def connect(self):
        fileName = "D:\\proj\\polaris\\analyser\\\data\\chicago-Supply.sqlite"
        if not os.path.exists(fileName):
            fileName = QtGui.QFileDialog.getOpenFileName(None, "Open Database", ".", "Image Files (*.db *.sqlite)");
        self.dbfileName = fileName
        if (fileName == ''):
            QtGui.QMessageBox.about(None,"POLARIS", "No file was selected. The plug-in will not start")
            return

        db_dir = os.path.dirname(fileName)
        #os.environ['PATH'] = 'C:\\opt\\polarisdeps\\spatialite\\Win32' + ';' + os.environ['PATH']
        self.conn = sqlite3.connect(fileName)
        #self.conn = sqlite3.connect("../test_case/chicago-Supply.sqlite")
        self.conn.enable_load_extension(1)
        
        self.conn.load_extension('spatialite.dll')
        self.conn.execute("attach database \'%s/chicago-Demand.sqlite\' as Demand"%db_dir) 
        self.conn.execute("attach database \'%s/chicago-Result.sqlite\' as res"%db_dir)
        #QtGui.QMessageBox.about(self, "My message box", "Connected")     
        self.conn_message = QtGui.QLabel("Connected to test_case/chicago-Supply.sqlite")
        self.conn_message.setMinimumSize(self.conn_message.sizeHint())
        self.ui.statusbar.addWidget(self.conn_message)
    def update_status_message(self, val):
        self.status_message.setText(str(val))
        self.repaint()
    def add_layer_to_canvas(self):
        self.update_status_message(-999)
        uri = QgsDataSourceURI()
        uri.setDatabase('../test_case/chicago-Result.sqlite')
        schema = ''
        table = 'link_moe'
        geom_column = 'GEO'
        uri.setDataSource(schema, table, geom_column)
        display_name = 'Link MOE'
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')   
        QgsMapLayerRegistry.instance().addMapLayer(vlayer)
    
    def start_generating_layer(self, start, end):
        self.update_status_message(-10)
        
        self.th = CreateLayerTread("../test_case/chicago-Supply.sqlite", start, end)
        self.update_status_message(-9)
        #QtCore.QObject.connect( self.th, QtCore.SIGNAL("update(QString)"), self.update_status_message )
        self.th.partDone.connect(self.update_status_message)
        self.th.allDone.connect(self.add_layer_to_canvas)
        self.update_status_message(-8)
        self.th.start()

    def crate_new_layer(self):
        self.tsd = TimeSpanDialog()
        self.tsd.ok_signal.connect(self.start_generating_layer)
        self.tsd.exec_()


        
        
        
         
