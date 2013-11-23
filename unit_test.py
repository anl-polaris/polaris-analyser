from ReportItem import ReportItem
import sqlite3

#create database for testing
data_path = './'
c = sqlite3.connect(data_path+"unit_test.sqlite")
c.execute("attach '%sunit_test_intermidiate.sqlite' as interm"%data_path)
c.execute('drop table if exists XY')
c.execute('create table XY (x real, y real)')


ri = ReportItem("select x,y from XY", (c,['interm']))
req = ('XY', ['x', 'y'],'')
ri.add_requirement(req)
assert ri.check_requirement(req)==True

req = ('temp_table',['temp_column'],'create table interm.temp_table (temp_column int)')
ri.add_requirement(req)
assert ri.check_requirement(req)!=True
ri.apply_requirements()
assert ri.check_requirement(req)==True
print "All of the tests passed!"