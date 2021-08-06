n = int(input())
p = []

for i in range(1, n + 1):
    p += [i] * i
for i in range(0, n):
    print(p[i], end=' ')
