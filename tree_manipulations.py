import Project
from PyQt4 import QtGui, QtCore
import glob
import os.path
import json
#QTreeWidget  tree
def setup_tree(tree):
    tree.setHeaderLabels(QtCore.QStringList("Project Items"))
    tree.setColumnCount(1)
    
#some usefule documentation for the qt trees:
#http://pyqt.sourceforge.net/Docs/PyQt4/qt.html#ItemDataRole-enum
#http://pyqt.sourceforge.net/Docs/PyQt4/qtreewidgetitem.html
#http://pyqt.sourceforge.net/Docs/PyQt4/qtreewidget.html
#http://pyqt.sourceforge.net/Docs/PyQt4/qvariant.html

def populate_tree(project, tree):
    root = tree.invisibleRootItem()
    tree.setHeaderHidden(True)
    column = 0
    pp = add_parent(root, column, "Project Properties",project.str, project.filename)
    rq = add_parent(root, column, "Requirements")
    data = add_parent(root, column, "Data")
    ri = add_parent(root, column, "Report Items")
    folder = project.control_data['sql_path']
    #populate Data item
    data_ls = glob.glob(folder+'/data_*.sql')
    for item in data_ls:
        fn = os.path.basename(item)
        n = len(fn)
        data_name = fn[5:n-4]
        if not os.path.exists(item):
            continue
        with open(item) as fh:
            content = fh.read()
        temp = add_child(data, column, data_name, content, item)        
    #populate Requirements
    rqls = glob.glob(folder+'/rq_*.sql')
    for item in rqls:
        fn = os.path.basename(item)
        n = len(fn)
        rq_name = fn[3:n-4]
        if not os.path.exists(item):
            continue
        with open(item) as fh:
            content = fh.read()
        temp = add_child(rq, column,rq_name, content, item)
        #if rq_name in satisifed_items:
        #    temp.setTextColor(column, QtGui.QColor(0,255,0))
        #else:
        #    temp.setTextColor(column, QtGui.QColor(255,0,0))
    colorize_requireents(project, tree)
    content = None
    if os.path.exists(folder+'/report.json'):
        with open(folder+'/report.json') as fh:
            content = json.load(fh)
        report_items = content["items"]
        for item in report_items:
            #temp = add_child(ri, column,item, report_items[item], None)
            temp = add_child(ri, column,item,[1,2,3], None)
    return content


def colorize_requireents(project, tree):
    for i in range(tree.topLevelItemCount()):
        if tree.topLevelItem(i).data(0,0).toString() == "Requirements":
            req_item = tree.topLevelItem(i)
            break
    satisifed_items = project.SatisfiedItems()
    for i in range(req_item.childCount()):
        temp = req_item.child(i)
        rq_name = temp.data(0,0).toString()
        if rq_name in satisifed_items:
            temp.setTextColor(0, QtGui.QColor(0,255,0))
        else:
            temp.setTextColor(0, QtGui.QColor(255,0,0))

def add_parent(parent, column, title, data=None, filename=None):
    item = QtGui.QTreeWidgetItem(parent, [title])
    item.setData(column, QtCore.Qt.UserRole, data)
    item.setData(column, QtCore.Qt.UserRole+1, filename)
    item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
    item.setExpanded (True)
    return item

def add_child(parent, column, title, data, filename=None):
    item = QtGui.QTreeWidgetItem(parent, [title])
    item.setData(column, QtCore.Qt.UserRole,  QtCore.QVariant(data))
    item.setData(column, QtCore.Qt.UserRole+1,  QtCore.QVariant(filename))
    #item.setCheckState (column, QtCore.Qt.Unchecked)
    return item
