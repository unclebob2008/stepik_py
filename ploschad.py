from math import sqrt
form = str(input())
pi = 3.14

if form == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    print(S)
elif form == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif form == 'круг':
    a = float(input())
    print(pi * a ** 2)
else:
    print("No form")
