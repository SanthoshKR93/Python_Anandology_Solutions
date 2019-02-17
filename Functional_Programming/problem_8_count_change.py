# Write a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.
def count(S, m, n):
   table = [0 for k in range(n+1)]
   #print (table)
# Base case (If given value is 0) 
   table[0] = 1
   #print (table)
# Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the picked coin
   for i in range(0,m):
      for j in range(S[i],n+1):
         table[j] += table[j-S[i]]
         #print (table)
   return table[n]

# Driver program to test above function 
arr = [1,5]
m = len(arr)
n = 10
x = count(arr, m, n)
print (x)
