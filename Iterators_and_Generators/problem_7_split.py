# Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file 
# into multiple small files with each having n lines.


def split(fname,nl):
   val = 0
   count = 0
   f = open(fname)
   cont = f.readlines()
   length = len(cont)
   mod = length%nl
   if int(mod)==0: 
      nof = int(length/nl)
      #print(nof)
   else:
      nof = int(length//nl) + 1
      #print(nof)
   for j in range(nof):
      cont = cont[val:]
      if j == nof-1:
         nl = nl - int(mod)
      else:
         nl = nl 
      #print(nl)
      #print(val)
      fnm = 'file' + str(j)
      #print(fnm)
      f = open(fnm,'w')
      for i in cont[:nl]:
         val = nl
         f.write(i)
      f.close()
      
      print(val)
   
split('1.txt',50)
      
