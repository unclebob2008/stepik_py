x = float(input())
y = float(input())
opr = str(input())

if opr == "+":
    print(x + y)
elif opr == "-":
    print(x - y)
elif opr == "/":
    if y != 0:
        print(x / y)
    else:
        print('Деление на 0!')
elif opr == "*":
    print(x * y)
elif opr == "mod":
    if y == 0:
        print('Деление на 0!')
    else:
        print(int(x) % int(y))
elif opr == "pow":
    print(x ** y)
elif opr == "div":
    if y != 0:
        print(int(x) // int(y))
    else:
        print('Деление на 0!')
else:
    print('No such operator')
