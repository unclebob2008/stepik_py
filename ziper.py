z = ''
c = 1

while True:
    s = str(input())
    if len(s) > 0:
        break

if len(s) == 1:
    print(s + str(c))
else:
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            c += 1
        else:
            z += s[i] + str(c)
            c = 1
        if i + 1 == len(s) - 1:
            z += s[i + 1] + str(c)
print(z)
