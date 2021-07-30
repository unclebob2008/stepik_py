s = str(input())

s = s.lower()
c = s.count('g')
c += s.count('c')
print(c / len(s) * 100)
