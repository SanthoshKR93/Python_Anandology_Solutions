# What will be output of this code?

x = [0, 1, [2]]
x[2][0] = 3
print (x)
x[2].append(4)
print (x)
x[2] = 2
print (x)

# result is : [0,1,[3]]  [0,1,[3,4]]  [0, 1, 2]
