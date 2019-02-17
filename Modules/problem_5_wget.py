# Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL.
# If the URL ends with a /, consider the basename as index.html.

import urllib.request,sys
content = ''
blist = []
def wget(url):
   blist = url.split("/")
   response = urllib.request.urlopen(url)
   content = response.read()
   if blist[-1] != "":
      n = blist[-1]
      print(n)
      f = open(n,'wb')
      f.write(content)
      f.close()
      print("saving"+ url +"as" + blist[-1])
   else:
      n = 'index.html'
      f1 = open(n,'wb')
      f1.write(content)
      print("saving" + url +"as" + "index.html")

wget(sys.argv[1])
