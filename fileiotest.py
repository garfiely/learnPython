prompt = "Please input a char(999 for stop) :"
str = input(prompt)
#print(str * 3)

file1 = open("TFWB.txt","w")
file2 = open("TFWA.txt","a")
#print(file1.name)
#print(file1.closed)
#print(file1.mode)
while str != "999" :
    file1.write(str)
    file1.write("\n")
    file2.write(str)
    file2.write("\n")
    str = input(prompt)
file1.close()
file2.close()