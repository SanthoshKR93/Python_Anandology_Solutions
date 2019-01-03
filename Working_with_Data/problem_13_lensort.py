# Write a function lensort to sort a list of strings based on length.

def lensort(x):
   for m in range(len(x)):
      for j in range(len(x)):
         if len(x[m]) >= len(x[j]):
            x[m],x[j] = x[j],x[m]
         else:
            continue
   print(x)

lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
