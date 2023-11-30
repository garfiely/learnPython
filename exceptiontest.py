try :
    file1 = open("TFWA.txt","a")
    file1.write("appendline\n")
    print("Write sucessfully")
    file1.close()
except :
    print("Write file failed")
    #file1.close()