s = str(input())

r1 = int(s[0])
r2 = int(s[1])
r3 = int(s[2])
r4 = int(s[3])
r5 = int(s[4])
r6 = int(s[5])

if r1 + r2 + r3 == r4 + r5 + r6:
    print("Счастливый")
else:
    print("Обычный")
