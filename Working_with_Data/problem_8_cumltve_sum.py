# Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. 
# Does your implementation work for a list of strings?

sum1 = 0
res = ''
k = []
def cumulative_sum(x):
   a=type(x[0])
   b=type(1)
   c=type('hello')
   for i in range(len(x)):
      if a==b:
         global sum1
         sum1 = sum1 + x[i]
         global k
         k.append(sum1)
      elif a==c:
         global res
         res = res + x[i]
         k.append(res)
      else:
         print("wrong type")
   print(k)
   k=[]
   sum1=0
   re=''

cumulative_sum([1,2,3,4,5,6])
cumulative_sum(['hello','my','name','is','santhosh'])

