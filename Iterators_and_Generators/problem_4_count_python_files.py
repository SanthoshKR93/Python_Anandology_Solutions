# Write a function to compute the number of python files (.py extension) in a specified directory recursively.

g = []
import os,sys
def py(fpath,ftype):
   listt = []
   os.chdir(fpath)
   path = os.getcwd()
   v = os.walk(path)
   for gpath,gdir,gfile in v:
      for i in gfile:
         if ftype in i:
            j = os.path.join(gpath,i)
            listt.append(j)
   return listt


g = py(sys.argv[1],'.py')
print (len(g))

