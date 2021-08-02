import re

newlist = [0] * 200

file1 = open('F:\\disk_f\\Docs\\Docs\\SpaVorota\\ppp.txt', 'r')
alllines = file1.readlines()

for oneline in alllines:
    r1 = re.search('\d{1,3}$', oneline.strip())
    if r1:
        newlist[int(r1.group())] = oneline
file2 = open('f:\\temp\\ppp2.txt', 'a')
for line in newlist:
    if line != 0:
        file2.write(line)
file2.close()
