# Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are 
# replaced by a hyphen, typically used to create blog post URL from post title. It should also make sure there are no more than one
# hyphen in any place and there are no hyphens at the biginning and end of the slug.

import re
a = []
alp = []
content = ''
cc = ''
def make_slug(strng):
   alp=map(chr,range(32,48))
   for i in alp:
      a.append(i)
   #print (a)
   alp=map(chr,range(58,65))
   for i in alp:
      a.append(i)
   #print (a)
   alp=map(chr,range(91,97))
   for i in alp:
      a.append(i)
   #print (a)
   alp=map(chr,range(123,127))
   for i in alp:
      a.append(i)
   #print (a)

   stri = list(strng)
   
   for i in range(len(stri)):
      if stri[i] in a or stri[i] == ' ':
         stri[i] = '-'
      else:
         continue
   content = "".join(stri)
   cc = content.strip('-')
   #print(content)
   #print(cc)
   
   ro = re.compile('-+')
   mo=re.sub(ro,'-',cc)
   print(mo)

make_slug('--hello-  world--')




