fulls = []
tw = ''
c = 0
with open('dataset_3363_3.txt', 'r') as fl:
    lns = fl.readlines()

for i in range(0, len(lns)):
        fulls += lns[i].lower().strip().split()

for i in range(0, len(fulls)):
    n = fulls.count(fulls[i])
    if n > c:
        tw = fulls[i]
        c = n
    elif n == c:
        if fulls[i] < tw:
            tw = fulls[i]

print(tw, c)
