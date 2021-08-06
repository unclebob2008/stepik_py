a = [int(i) for i in input().split()]
z = []
c = 1

if len(a) != 1:
    a.sort()
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            c += 1
            if i + 1 == len(a) - 1:
                z.append(a[i])
        else:
            if c > 1:
                z.append(a[i])
                c = 1
for i in z:
    print(i, end=' ')
