# Write a program reverse.py to print lines of a file in reverse order.

import sys
fname = sys.argv[1]

f = open(fname,'r')
v = f.readlines()
rev = v[::-1]
v = "".join(v)
reverse = ''.join(rev)
print("Original : \n" + v)
print ("Reverse : \n" + reverse)

# result is: 
#Original : 
# original Text
#Reverse : 
# Reversed text
