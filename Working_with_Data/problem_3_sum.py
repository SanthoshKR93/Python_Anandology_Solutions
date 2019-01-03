# Python has a built-in function sum to find sum of all elements of a list (strings). Provide an implementation for sum.
# sum(['hello','world','!'])   ----> hello world
res=''
def sum(x):
   for i in x:
      global res
      res = res+i
   return res

y = sum(['hello','world','!'])
print(y)

   

