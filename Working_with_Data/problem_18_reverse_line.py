# Write a program to print each line of a file in reverse order.

import sys

fname = sys.argv[1]

f = open(fname,'r')
clist = f.readlines()
v=[]
for i in clist:
   v.append(i[::-1])
f.close()
# print(v)

print("".join(v))
