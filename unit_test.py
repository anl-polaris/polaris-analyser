from ReportItem import ReportItem
import Project
from utils import *
import sqlite3
import os.path
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

c.execute('drop table if exists temp_table')
req = ('temp_table',['temp_column'],'create table interm.temp_table (temp_column int)')
ri.add_requirement(req)
assert ri.check_requirement(req)!=True
ri.apply_requirements()
assert ri.check_requirement(req)==True
s = """
my location = c:\users\vsokolov
name=My New Project
MasterDataBase = c:/users/vsokolov/db.sqlite
; this line is a comment

ReportItem = ;;;;
"""
(k,v) = FromString(s)
assert len(k) == len(v)
assert len(k) == 4
assert k[2] == 'MasterDataBase'.lower()
assert v[2] == 'c:/users/vsokolov/db.sqlite'.lower()

pr = Project.Project()
assert len(pr.db_paths) == 3 
assert len(pr.ri_paths) == 5
assert pr.db_paths[0] ==  (os.path.expanduser('~')+'/db.sqlite').lower()

print "All of the tests passed!"