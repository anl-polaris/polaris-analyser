from PyQt4 import QtGui
import ui_data_widget
from ReportItem import ReportItem
import mpl
class ReportItem2D(ReportItem):
    """Implementation of """
    def __init__(self,sql, conn):
        self =  super(ReportItem2D, self).__init__(sql, conn)
        self.x = []
        self.y = []
        sefl.poulated = False
    def populate_data(self):
        c = conn[0]
        d = c.execute(sql)
        x = []
        y = []
        for item in d:
            x.append(item[0])
            y.append(item[0])
        self.populated = True
    def get_widget(self):
        if not self.populated:
            self.populate_data()

#ADD MATPLOTLIB TO THE db plot widget
class DBPlot(QtGui.QWidget): 
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = ui_data_widget.Ui_Form()
        self.ui.setupUi(self)
        self.fig = mpl.MyMplCanvas(self, width=6, height=5, dpi=100)
        self.ui.verticalLayout.addWidget(self.fig.mpl_toolbar)
        self.ui.verticalLayout.addWidget(self.fig)
    def clear(self):
        self.fig.axes.clear()
    def add_xy(self, x,y, title="", xlabel="x", ylabel="y"):
        self.fig.axes.plot(x,y,'--')
        self.fig.axes.set_xlabel(str(xlabel).capitalize()) 
        self.fig.axes.set_ylabel(str(ylabel).capitalize())
        self.fig.draw()