# Write a function istrcmp to compare two strings, ignoring the case.


def istrcmp(x,y):
   x=x.upper()
   y=y.upper()
   if x==y:
      print ('True')
   else:
      print('False')


istrcmp('python','PyThOn')

# result is: True
