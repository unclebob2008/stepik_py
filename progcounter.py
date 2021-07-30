n = int(input())
r = n % 100

if r > 20:
    r = r % 10
if r == 0 or 5 <= r <= 20:
    print(n, "программистов")
if r == 1:
    print(n, "программист")
if 2 <= r <= 4:
    print(n, "программиста")
