str1 = "Hello"
str2 = 'world'
print(str1 + str2)
print(str1 * 5)
print(str1[4])
print(str1[1:2])
print(str1[1:3])
print(str1 + str2)
print(str1 + '\n' + str2)
str3 = 'e'
if str3 in str1 :
    print(str3, " in ", str1)
    print('\'', str3, "\'"," in ", str1)
str3 = 'f'
if str3 not in str1 :
    print(str3, " not in ", str1)