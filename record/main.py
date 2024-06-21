# What is file?
# Collects data from the user and saves it to a file

# types of file
# 1. text file
# 2. binary file

# modes of file
# r -> read
# w -> write
# a -> append
# r+ -> read and write
# w+ -> write and read
# a+ -> append and read

# name =input("Enter name: ")
# handle =open("record/students.txt","a")
# handle.write(f"Name: {name}")
# handle.write("\n")
# handle.close()

# name =input("Enter your name: ")
# nep =int(input("Enter nep mark: "))
# eng =int(input("Enter eng mark: "))
# mat =int(input("Enter mat mark: "))
# sic =int(input("Enter sic mark: "))
# com =int(input("Enter com mark: "))
# total = nep+eng+mat+sic+com
# per =total/5
# grade=""
# if per>35 and per<45:
#     grade="C"
# elif per>45 and per<60:
#     grade="B"
# elif per>60 and per<80:
#     grade="A"
# elif per>80 and per<100:
#     grade="A+"
# else:
#     grade ="fail"

# handle =open("record/result.txt","a")
# handle.write(f"Name:{name} nep:{nep} eng:{eng} mat:{mat} sic:{sic} com:{com} total:{total} per:{per} grade: {grade} \n")

# handle.close()



data = open("record/students.txt","r")
# print(data.read())
# print(data.readline())
print(data.readlines())