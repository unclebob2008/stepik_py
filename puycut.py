a = int(input())
b = int(input())
x, y = a, b
if x < y:
    x, y = y, x
while x % y != 0:
    x, y = y, x % y
print(int(a * b / y))
