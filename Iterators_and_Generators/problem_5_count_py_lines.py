# Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

import os,sys
count = 0
g = []
sd = 0
def py(ftype):
   listt = []
   path = os.getcwd()
   v = os.walk(path)
   global count
   for gpath,gdir,gfile in v:
      for i in gfile:
         if ftype in i[-3:]:
            listt.append(i)
            os.chdir(gpath)
            f = open(i,'rb')
            h = f.readlines()
            sd = len(h)
            print(i,sd)
            count = count + sd
            f.close()      
   return count

g = py('.py')
# print (len(g))
print("total :-",g)
