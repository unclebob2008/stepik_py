sl = []
ch = []
er = set()

n = int(input())
for i in range(n):
    sl.append(input().lower())

m = int(input())
for i in range(m):
    ch.append(input().lower().split())

for i in range(len(ch)):
    for j in range(len(ch[i])):
        if ch[i][j] not in sl:
            er.add(ch[i][j])
for i in er:
    print(i)
