def f(x):
    return x * 2


c = int(input())
a = {}
i = 1
while i <= c:
    n = int(input())
    i += 1
    if n not in a:
        a[n] = f(n)
        print(a[n])
    else:
        print(a[n])
