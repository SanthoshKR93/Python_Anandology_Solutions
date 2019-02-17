# Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flat_dict(idict,res = None):
   if res is None:
      res = {}

   for key in idict:
      value = idict[key]
      if isinstance(value,dict):
         newdict = {}
         for keys in value:
            newdict[str(key)+'.'+str(keys)]= value[keys]
         flat_dict(newdict,res)
      else:
         res[key] = value

   return res

rdict = flat_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})

print (rdict)
