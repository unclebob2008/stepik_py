import os

if os.path.exists("res.txt"):
    os.remove("res.txt")
c = 0
s = 0
with open('dataset_3380_5.txt', 'r', encoding="utf8") as fl:
    lns = fl.readlines()
with open('res.txt', 'a') as wf:
    for i in range(1, 12):
        for ln in lns:
            a = ln.split()
            if int(a[0]) == i:
                c += 1
                s += int(a[2])
        if c == 0:
            #            print(i, '-')
            wf.write(str(i) + ' -' + '\n')
        else:
            #            print(i, s / c)
            wf.write(str(i) + ' ' + str(s / c) + '\n')
        c = 0
        s = 0
