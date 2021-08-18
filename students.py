import os
if os.path.exists("res.txt"):
    os.remove("res.txt")

with open('dataset_3363_4.txt', 'r', encoding="utf8") as fl:
    lns = fl.readlines()
d = {}
ll = []
pc = 0
ps = ''
for ln in lns:
    ll = ln.strip().split(';')
    d[ll[0]] = ll[1:]
    pc = len(ll[1:])

with open('res.txt', 'a') as wf:
    for key in d.keys():
        s = 0
        for i in d[key]:
            s += int(i)
#        print(s / len(d[key]))
        wf.write(str(s / len(d[key])) + '\n')

    for i in range(0, pc):
        s = 0
        for key in d.keys():
            s += int(d[key][i])
        ps += str(s / len(d)) + ' '
#    print(ps)
    wf.write(ps)
