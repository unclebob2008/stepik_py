import re
ns = ''
with open('dataset_3363_2.txt', 'r') as fl:
    s = fl.readline()
l = re.findall('\D', s.strip())
n = re.findall('\d{1,5}', s.strip())
for i in range(0, len(l)):
    ns += l[i] * int(n[i])
with open('res.txt', 'w') as rf:
    rf.write(ns)
