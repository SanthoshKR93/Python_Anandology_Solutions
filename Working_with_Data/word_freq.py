import sys
filename = sys.argv[1]
v = {}
words = ''
def word_freq(words):
   dict ={}
   for i in words:
      dict[i] = dict.get(i,0) + 1
   return dict

def read_words(filename):
   f = open(filename)
   words = f.read().split()
   return words

v = word_freq(read_words(filename))

for key,value in v.items():
   print(key,value)
