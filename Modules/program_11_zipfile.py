# Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files
# to add as rest of the arguments.

from zipfile import *
import sys
fname = ''
listt = []
def zip_file(fname,listt):
   f = ZipFile(fname,'w')
   for i in listt:
      f.write(i)


zip_file(sys.argv[1],sys.argv[2:])
   
