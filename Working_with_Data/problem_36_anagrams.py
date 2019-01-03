# Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.


def permute(result):
   perm =[]
   for i in range(len(result)):
      if i < (len(result)-1):
         temp = result[i]
         result[i] = result[i+1]
         result[i+1] = temp
         perm.append(result)
   perm.remove(result)
   return perm


def unique(x):
   k =[]
   length = 0
   length = len(x)
   for i in range(length):
      
      if x[i] in k:
         continue
      else:
         k.append(x[i])
   
   return k


def anagram(listt):
   ml = []
   temp = []
   res = []
   ach = []
   nl = []
   nv = "" 
   fin = []
   m = []
   d = []
   final = []
   finale = []
   k = []
   finn= []

   l = len(listt)
   fin =[]
   for i in range(l):
      value = []
      for j in range(l):
         g = []
         h = []
         g = list(listt[i])
         #print (g)
         h = list(listt[j])
         #print (h)
         val = ''
         if (g != h) and len(g) == len(h):
            for k in g:
               #print (k)
               if k in h:
                  val= val + k
                  h.remove(k)
                  ach = listt[j]
                  #print(h)
               else:
                  val =''
                  ach = []
                  break
         else:
            continue
         #print (val)
         value.append(val)
         value.append(ach)
         #print (value)
      fin.append(value)   
   #print (fin)

   
   
   for nul in fin:
      while nv in nul:
         nul.remove(nv)
      else:
         continue
   
   #print(fin)
   for final in fin:
      fina = [x for x in final if x]
      finale.append(fina)
   #print (finale)
   finn = []
   for jh in finale:
      fi = unique(jh)
      finn.append(fi)
   
   res = unique(finn)
   #print (res)
   

   for el in res:
      chk = []
      chk = el[::-1]
      #print (el)
      #print (chk)
      if chk in res:
         res.remove(chk)  
      else:
         continue
# add a swap function inorder to take care of permutations
  
   for values in res:
      posbleval = permute(values)
      for hj in posbleval:
         if hj in res:
            res.remove(hj)
   print (res)
   res = []
  
anagram(['layers','nip', 'pin', 'silent', 'rental', 'listen', 'learnt','relays'])
anagram(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
anagram(['layers','nip', 'pin', 'silent', 'rntal', 'listen', 'learnt','relays'])



