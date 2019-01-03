# Write a python function parse_csv to parse csv (comma separated values) files.

# using csv module
import csv
v = []
k = []
l = []
def parse_csv(fcsv):
   f = open(fcsv)
   v = csv.reader(f)
   for i in v:
      k.append(i)
   print(k)
   f.close()


# without using csv module
def parse_csv1(fcsv1):
   f1 = open(fcsv1)
   p = f1.readlines()
   for j in p:
      j = j.strip("\n")
      j = j.split(",")
      l.append(j)
   print(l)
   f1.close()

parse_csv("santhosh.csv")
parse_csv1("santhosh.csv")

