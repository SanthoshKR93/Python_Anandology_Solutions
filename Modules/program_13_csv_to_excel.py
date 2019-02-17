# Write a program csv2xls.py that reads a csv file and exports it as Excel file. The program should take two arguments. 
# The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.

# Note : here we will have to import a third party library tablib inorder to write data in tabular format.


import tablib

def csvtoxls(csvf,xlsf):
   sno = 0
   content = tablib.Dataset()
   f = open(csvf,'r')
   length = len(f.readlines())
   f = open(csvf,'r')
   while sno < length:
      content.append([sno,f.readline().strip()])
      sno = sno + 1
   exel = xlsf + '.xls'
   f = open(exel,'wb')
   f.write(content.xls)
   f.close()

csvtoxls('santhosh2.csv','santhos')
   
