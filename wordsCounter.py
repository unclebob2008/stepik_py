s = str(input())
a = s.lower().split()
d = {i: a.count(i) for i in a}
for i in d:
    print(i, d[i])
