def sum(l):
    i = len(l)
    res = 0
    while i :
        res += l[i - 1]
        i -=1
    return res

my_list = [1, 2, 3, 4, 5]
print(sum(my_list))