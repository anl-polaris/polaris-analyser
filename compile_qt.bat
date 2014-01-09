@echo off
set qgis_folder="C:\Program Files\QGIS Dufour"
set qgis_uic_folder=%qgis_folder%\apps\Python27\Lib\site-packages\PyQt4\uic
%qgis_folder%\bin\pyrcc4.exe -o resources_rc.py resources.qrc
c:\Python27\python.exe %qgis_uic_folder%\pyuic.py data_item_constructor.ui		-o data_item_constructor.py
c:\Python27\python.exe %qgis_uic_folder%\pyuic.py pa.ui					-o ui_pa.py
