# Write a function treemap to map a function over nested list.

def treemap(func,listt):
   j = 0
   while j<len(listt):
      if isinstance(listt[j],list):
         treemap(func,listt[j])
      else:
         listt[j] = func(listt[j])
      j = j + 1
   return listt

res = treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
print(res)
