a = [int(i) for i in input().split()]
b = [0] * len(a)

if len(a) == 1:
    print(str(a[0]))
else:
    for i in range(0, len(a)):
        if i == len(a) - 1:
            b[i] = str(a[i - 1] + a[0])
        else:
            b[i] = str(a[i - 1] + a[i + 1])
    print(' '.join(b))
