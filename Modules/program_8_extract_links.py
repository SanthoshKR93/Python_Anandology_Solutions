# Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.

import urllib.request
import re

v = []
k = []
def unique(x):
   length = len(x)
   for i in range(length):
      global k
      if x[i] in k:
         continue
      else:
         k.append(x[i])
   
   return k
   k = []



def ext_links(url):
   response = urllib.request.urlopen(url)
   content = response.read().decode('utf-8')
   #print (content)
   robj = ('href=.*.html')
   v = re.findall(robj,content)
   
   uv = unique(v)
   for i in uv:
      i = list(i)
      i = i[6:]
      print (("").join(i))

ext_links("https://docs.python.org/3/tutorial/")
