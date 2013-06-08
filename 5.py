import zipfile

i = '90052'
zf = zipfile.ZipFile('channel.zip')
s = []
def main():
    global i
    if(i!='Collect the comments.'):
        y = open('channel/'+i+'.txt').read().strip("Next nothing is ")
        s.append(i+'.txt')
        i = y
def dostuff():
    for info in zf.infolist():
        if info.filename!='readme.txt':
            a = s.index(info.filename)
            s[a]=info.comment

for x in range(950):
    main()
print s
dostuff()
for i in s:
    print i,
