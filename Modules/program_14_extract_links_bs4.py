# Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML. 
# Try using it to extract all HTML links from a webpage.

from bs4 import BeautifulSoup
import sys

def link(url):
   f = open(url)
   #v = ("").join(f.read().split())
   soup = BeautifulSoup(f,'html.parser')
   for i in soup.find_all('a'):
      v = i.get('href')
      
      #print (v)
      v = list(v)
      if '.html' in ("").join(v[-5:]):
         print(("").join(v))
        

link(sys.argv[1])
      
