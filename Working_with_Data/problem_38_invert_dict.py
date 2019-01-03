# Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.
invdict={}
def invertdict(dict):
   for keys,values in dict.items():   
      invdict[values] = keys

   print (invdict)


invertdict({'z': 1, 'y': 2, 'a': 3})
