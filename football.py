tl = {}
n = int(input())
s = [[0] * n for i in range(n)]
for i in range(n):
    s[i] = str(input()).split(';')
    for j in range(0, len(s[i]), 2):
        if s[i][j] not in tl:
            tl[s[i][j]] = [1, 0, 0, 0, 0]
        else:
            tl[s[i][j]][0] += 1
    if int(s[i][1]) > int(s[i][3]):
        tl[s[i][0]][1] += 1
        tl[s[i][0]][4] += 3
        tl[s[i][2]][3] += 1
    elif int(s[i][1]) == int(s[i][3]):
        tl[s[i][0]][2] += 1
        tl[s[i][2]][2] += 1
        tl[s[i][0]][4] += 1
        tl[s[i][2]][4] += 1
    else:
        tl[s[i][2]][1] += 1
        tl[s[i][2]][4] += 3
        tl[s[i][0]][3] += 1
for key in tl:
    b = ' '.join(str(i) for i in tl[key])
    print(str(key) + ':' + b)
