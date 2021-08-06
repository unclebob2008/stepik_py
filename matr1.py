a = []
while True:
    s = input()
    if s == 'end':
        break
    a += [[int(i) for i in s.split()]]

n = len(a)
m = len(a[0])
b = [[0] * m for i in range(n)]

for i in range(0, len(a)):
    x = i
    if i + 1 >= len(a) - 1:
        x = i - len(a)
    for j in range(0, len(a[i])):
        y = j
        if j + 1 >= len(a[i]) - 1:
            y = j - len(a[i])
        b[i][j] = a[i - 1][j] + a[x + 1][j] + a[i][j - 1] + a[i][y + 1]

for i in b:
    for j in i:
        print(j, end=' ')
    print()
