# Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and 
# read the IP address from there. The program should print only the IP address and nothing else.

import urllib.request
import re
content = ''
cont = []
def my_ip():
   response = urllib.request.urlopen("http://httpbin.org/get")
   content = response.read().decode('utf-8')
   robj = re.compile('\d+.\d+.\d+.\d+')
   ro = re.findall(robj,content)
   for i in ro:
      print(i)
   

my_ip()

