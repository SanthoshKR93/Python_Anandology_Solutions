# Write a function tree_reverse to reverse elements of a nested-list recursively.
res = []
def tree_reverse(listt):
   i = 0
   length = len(listt)
   while i<length:
      if isinstance(listt[i],list):
         tree_reverse(listt[i])
      i = i+1
   listt.reverse()
   return listt
  
result = tree_reverse([[1, 2], [3, [4, 5]], 6])

print(result)
