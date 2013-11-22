from ReportItem import ReportItem
import sqlite3

data_path = 'd:/proj/polaris/analyser/data/'
c = sqlite3.connect(data_path + 'chicago-Supply.sqlite')
c.execute("attach database 'chicago-Result.sqlite' as res")
c.execute("attach database 'chicago-Intermidiate.sqlite' as interm")

ri = ReportItem("select link, speed_ab from link", "xy", (c,['res','interm']))
req = ('link', 'link','')
ri.add_requirement('link', 'link','')
assert ri.check_requirement(req)==True

req = ('temp_column', 'temp_table','create temp table temp_table (temp_column int)')
ri.add_requirement('temp_column', 'temp_table','create table interm.temp_table (temp_column int)')
assert ri.check_requirement(req)!=True
ri.apply_requirements()
assert ri.check_requirement(req)==True
print "All of the tests passed!"