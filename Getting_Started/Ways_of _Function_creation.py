# various ways of function creation

def square(x):
   return x*x
print(square(4))

# Using existing functions in creating new functions.

def sum_of_squares(x,y):
   return square(x) + square(y)
print(sum_of_squares(2,3))

# Passing existing function as a parameter to new function.

def fxy(f,x,y):
   return f(x) + f(y)
print(fxy(square,2,3))

# Functions can be called with keyword parameters.

def difference(x,y):
   return x-y

print(difference(x=5,y=2))
print(difference(5,y=2))
print(difference(x=5,2))
print(difference(y=2,x=5))

# Arguements can have default values.

def val(x,y=1):
   x=x+y
print(val(5))
print(val(5,5))

# creating Functions using lambda operator

print((lambda x: x+1)(5))
# result is 6

sqr=(lambda x: x ** 2)
print(sqr(2))
# result is 4
