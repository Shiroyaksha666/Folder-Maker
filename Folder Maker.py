import os
Number = int(input("Enter your number: "))
path = input("Enter your path: ")
os.chdir(f"{path}")
for i in range(1 , Number + 1):
    os.mkdir(f"{i}")
#Code By Ali Esmkhani