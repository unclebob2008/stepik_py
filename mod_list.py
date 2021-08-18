def modify_list(l):
    l[:] = [x for x in l if x % 2 == 0]
    for i in range(0, len(l)):
        l[i] = l[i] // 2


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
