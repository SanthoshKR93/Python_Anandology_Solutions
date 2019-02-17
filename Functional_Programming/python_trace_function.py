# Python Trace Function

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


# Python memoize function.

def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g
