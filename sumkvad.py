n = []
s = 0
while True:
    n.append(int(input()))
    if sum(n) == 0:
        break
for i in n:
    s += i * i
print(s)
