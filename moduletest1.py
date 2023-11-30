def sum2number(a,b) :
    return a + b

def sumlist(lst) :
    sum = 0
    i = 0
    while i < len(lst) :
        sum += lst[i]
        i += 1
    return sum

def sumnumbers(*valtuple) :
    sum = 0
    for x in valtuple :
        sum += x
    return sum

def sumlist2(lst) :
    sum = 0
    for x in lst :
        sum += x
    return sum