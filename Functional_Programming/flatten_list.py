def flat_list(listt,result=None):
   if result == None:
      result=[]

   for i in listt:
      if isinstance(i,list):
         flat_list(i,result)
      else:
         result.append(i)
   return result

res = flat_list([ [1, 2, [3, 4] ], [5, 6], 7])
print (res)
