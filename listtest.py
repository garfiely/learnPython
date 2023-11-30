lst = [1,2,3,4,5,6,7,8,9]
lst1 = []
print(lst)
while len(lst) > 0 :
    lst1.append(lst.pop())
    print(lst1[len(lst1) - 1])

for x in lst1 : print(x)