import Project
from PyQt4 import QtGui, QtCore

#QTreeWidget  tree
def setup_tree(tree):
    tree.setHeaderLabels(QtCore.QStringList("Project Items"))
    tree.setColumnCount(1)
    

def populate_tree(project, tree):
    item=QtGui.QTreeWidgetItem(["Properties"])
    tree.addTopLevelItem(item);
    item=QtGui.QTreeWidgetItem(["Report Items"])
    l  = [1,2,3]
    item.setData(0,0,l)
    l.append(5)
    tree.addTopLevelItem(item)