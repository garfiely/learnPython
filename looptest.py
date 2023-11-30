i = 0
while i < 100 :
    if (i % 10) == 0 : print(i)
    i += 1

i = 2
j = 10000
while i < j :
    k = 2
    while (k < i) :
        if i % k == 0 :
            break
        elif i == k + 1 :
            print(i)
        k += 1
    i += 1