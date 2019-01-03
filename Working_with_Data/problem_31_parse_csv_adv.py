# Generalize the above implementation of csv parser to support any delimiter and comments.
v = []
s = []
k = []
def csv_parser(fname,x,comnt):
   f = open(fname)
   v = f.readlines()
   print(v)
   for i in v:
      
      if i[0] != comnt:
         i = i.strip("\n")
         i = i.split("!")
         s.append(i)
      
   s.remove([''])   
   print(s)   
csv_parser("santhosh2.csv",'!','#')
   
