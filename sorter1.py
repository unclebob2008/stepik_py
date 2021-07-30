a = int(input())
b = int(input())
c = int(input())
mx, oth, mn = a, b, c

if b > a:
    mx, oth, mn = b, a, c
    if c > a:
        mx, oth, mn = b, c, a
        if c > b:
            mx, oth, mn = c, b, a
elif b < c:
    mx, oth, mn = a, c, b
    if c > a:
        mx, oth, mn = c, a, b
print(mx)
print(mn)
print(oth)
