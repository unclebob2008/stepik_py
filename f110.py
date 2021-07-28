import sys

A = int(input())
if 1900 > A or A > 3000:
    sys.exit('Out of range')
    print('Out of range')
if (A % 4 == 0 and A % 100 != 0) or A % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
