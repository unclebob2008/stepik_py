import sys

n = int(input())
s = 1

if n == 1:
    print(n)
    sys.exit()
else:
    a = [[0] * n for i in range(n)]
    if n % 2 != 0:
        a[n // 2][n // 2] = n * n
    for r in range(1, n // 2 + 1):
        for j in range(r - 1, n - r):
            a[r - 1][j] = s
            s += 1

        for i in range(r - 1, n - r):
            a[i][n - r] = s
            s += 1

        for j in range(n - r, r - 1, -1):
            a[n - r][j] = s
            s += 1

        for i in range(n - r, r - 1, -1):
            a[i][r - 1] = s
            s += 1

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()
