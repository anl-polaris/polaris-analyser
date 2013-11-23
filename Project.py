from PyQt4 import QtGui
from xml.dom.minidom import parse, parseString, getDOMImplementation
import ui_project_properties
class Project(object):
    xml_string = None
    name = None
    db_paths = []
    xml_doc = None
    """description of class"""
    def __init__(self):
        self.name = "New Report Project"
        self.ToXml()
    def ToXml(self):
        impl = getDOMImplementation()
        xml_doc = impl.createDocument(None, "Name", None)
        top_element = xml_doc.documentElement
        text = xml_doc.createTextNode(self.name)
        top_element.appendChild(text)
        self.xml_string = xml_doc.toprettyxml()
        self.xml_doc = xml_doc

class ProjectWidget(QtGui.QWidget): 
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = ui_project_properties.Ui_Form()
        self.ui.setupUi(self)
    def SetText(self, text):
        self.ui.textEdit.setText(text) 