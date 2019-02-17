# Write a function profile, which takes a function as argument and returns a new function,
# which behaves exactly similar to the given function, except that it prints the time consumed in executing it.

import datetime
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        #print('y2')
        return fib(n-1) + fib(n-2)
def trace(f):
    f.indent = 0
    def g(x):
        print ('|  ' * f.indent + '|--', f.__name__, x)
        f.indent += 1
        value = f(x)
        print ('|  ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value
    return g
def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g
def profile(f):
	result=[]
	inp=[]
	def g(x):
		inp.append(x)
		result.append(datetime.datetime.now())
		r=f(x)
		result.append(datetime.datetime.now())
		if x==inp[0]:
			print ("time taken:- ",max(result)-min(result))
		return r
	return g

fib = trace(fib)
fib = memoize(fib)
fib=profile(fib)
b=fib(10)
print (b)
