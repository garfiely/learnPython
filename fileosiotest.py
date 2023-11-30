import os

os.rename("TFWB.txt","TFWBNEW.txt")
os.makedirs("L1dir")
os.chdir("L1dir")
file1 = open("TFWA.txt","w")
file1.close()