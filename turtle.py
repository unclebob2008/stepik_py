n = int(input())
x = 0
y = 0
a = [[0] for i in range(n)]
for i in range(n):
    a[i] = input().split()
    if a[i][0] == 'север':
        y += int(a[i][1])
    elif a[i][0] == 'юг':
        y -= int(a[i][1])
    elif a[i][0] == 'восток':
        x += int(a[i][1])
    else:
        x -= int(a[i][1])
print(x, y)
