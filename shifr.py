s1 = list(input())
s2 = list(input())
s3 = list(input())
s4 = list(input())
s5 = []
s6 = []

for i in range(len(s3)):
    s5 += s2[s1.index(s3[i])]
for i in range(len(s4)):
    s6 += s1[s2.index(s4[i])]

print(''.join(s5))
print(''.join(s6))
