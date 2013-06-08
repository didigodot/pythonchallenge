import string, re
file = open('equality.html', 'rb').read().replace('\n', '')
print ''.join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',file))
