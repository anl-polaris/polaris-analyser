polaris-analyser
================

A QGIS(2.0) plugin that allows to analyze and validate outputs of the Polaris simulations

Some of the versions of QGIS used Tkinter as default backend for matplotlib but do not distribute it!
http://lists.osgeo.org/pipermail/qgis-user/2010-September/009637.html
To swith to QT4, open
C:\Program Files\QGIS Dufour\apps\Python27\Lib\site-packages\matplotlib\mpl-datamatplotlibrc
and modify line 31
from:
    backend      : TkAgg
to:
    backend      : Qt4Agg