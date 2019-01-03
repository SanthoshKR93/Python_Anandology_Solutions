# Write a function group(list, size) that take a list and splits into smaller lists of given size.
x = []
k = []
def group(listt,group_size):
   input_list_size = len(listt)
   a = input_list_size % group_size
   if a > 0 :
      no_of_sublists = int((input_list_size // group_size)) + 1
   else:
      no_of_sublists = int((input_list_size // group_size)) 
   global x,k
   x = list(range(no_of_sublists))
   for i in range(no_of_sublists):
      for j in range(group_size):   
         k.append(listt[j])
      if len(listt) > (group_size + a): 
         listt = listt[group_size:]
      else:
         listt = listt[group_size:]
         group_size = a
      x[i] = k
      k = []
   print(x)

group([1, 2, 3, 4, 5, 6, 7, 8, 9,10,], 10)   

