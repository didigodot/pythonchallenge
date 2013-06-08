import urllib
import re
c = 0
i = '23103'
def main():
    global i
    print i
    y = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+i).read().strip("and the next nothing is ")
    i = y
for x in range(400):
    main()
print i
