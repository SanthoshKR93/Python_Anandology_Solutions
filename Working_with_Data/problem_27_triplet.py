# Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.

def triplet(n):
   x = [(a,b,c) for a in range(n) for b in range(n) for c in range(n) if (a + b == c) and a!=b!=c!=0]
   print(tuple(x))

triplet(5)
