# Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.

import urllib.request
import re

urls=["file:///home/killbox/myfile.html"]

i=0

these_regex="<.*>(.+?)<.*>"
pattern=re.compile(these_regex)

while(i<len(urls)):
        htmlfile=urllib.request.urlopen(urls[i])
        htmltext=htmlfile.read().decode('utf-8')
        titles=re.findall(pattern,htmltext)
        print (titles)
        i+=1
