lst = [int(i) for i in input().split()]
x = int(input())
p = []

for i in range(0, len(lst)):
    if lst[i] == x:
        p.append(i)
if len(p) == 0:
    print("Отсутствует")
else:
    for e in p:
        print(e, end=' ')
