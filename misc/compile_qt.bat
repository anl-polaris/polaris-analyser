@echo off
set qgis_folder="C:\Program Files\QGIS Dufour"
set qgis_uic_folder=%qgis_folder%\apps\Python27\Lib\site-packages\PyQt4\uic
%qgis_folder%\bin\pyrcc4.exe -o ui\resources_rc.py ui\resources.qrc
c:\Python27\python.exe %qgis_uic_folder%\pyuic.py ui\ui_polaris.ui -o ui_polaris.py
c:\Python27\python.exe %qgis_uic_folder%\pyuic.py ui\ui_db_plot.ui -o db_plot.py
c:\Python27\python.exe %qgis_uic_folder%\pyuic.py ui\ui_db_plot1.ui -o db_plot1.py
c:\Python27\python.exe %qgis_uic_folder%\pyuic.py ui\ui_time_span.ui -o ui_time_span.py