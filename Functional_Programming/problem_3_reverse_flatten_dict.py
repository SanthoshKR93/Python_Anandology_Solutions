# Write a function unflatten_dict to do reverse of flatten_dict.

def unflat_dict(idict,res = None):
   if res is None:
      res = {}

   for key in idict:
      value = idict[key]
      chk = key.split(".")
      newdict = {}
      if len(chk) > 1:
         k = chk[0]
         k1 = chk[-1]
         newdict[k1] = value
         res.setdefault(k,{}).update(newdict)
      else:
         res[key] = value

   return res

result = unflat_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
print(result)
