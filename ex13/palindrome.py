def palindrom(s1) :
    s2 = s1
    i = len(s2) - 1
    j = 0
    while i :
        if s1[j] != s2[i]:
             print("is not palindrom")
             return
        i -= 1
        j += 1
    print("is palindrom")
    return 
print(palindrom("racecar"))