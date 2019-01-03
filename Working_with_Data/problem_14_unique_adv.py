# Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.

k = []
def unique1(s,key):
   for j in range(len(s)):
      s[j]=key(s[j])
   length = len(s)
   for i in range(length):
      global k
      if s[i] in k:
         continue
      else:
         k.append(s[i])
   
   print (k)
   k = []


unique1(["python", "java", "Python", "Java"], key=lambda s: s.lower())
