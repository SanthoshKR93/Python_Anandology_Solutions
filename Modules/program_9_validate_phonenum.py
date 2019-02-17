# Write a regular expression to validate a phone number.


import re

def val_phno(num):
   
   robj = re.compile('\+\d\d-\d\d\d\d\d\d\d\d\d\d')
   v = re.findall(robj,num)
   #print (type(v))
   
   if num in v:
      print ("yay!!! valid phone number")
   else:
      print("invalid phone number!!! Try again..")


val_phno('+91-8089625072')
