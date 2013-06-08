import re, string

data = list(open('ocr.html', 'r').read())
s = ''.join(i for i in data if i in string.letters)
print s
