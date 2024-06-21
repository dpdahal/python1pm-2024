# if,elif,else,nested if else

# if: It is used to check a condition and execute a block of code if the condition is true.


# x=500
# y=100

# if x>y:
#     print("x is greater than y")
# elif x==y:
#     print("x and y are equal")
# else:
#     print("y is greater than x")


# age =18

# if age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


# x=5
# y=10
# z=20

# if x>y and x>z:
#     print("x is greater than y")
# elif y>x and y>z:
#     print("y is greater than x")
# elif x==y and x==z:
#     print("x,y and z are equal")
# else:
#     print("z is greater than x and y")

# nep = int(input("Enter nepali mark: "))
# eng = int(input("Enter english mark: "))
# mat = int(input("Enter math mark: "))
# com = int(input("Enter cmp mark: "))
# sic = int(input("Enter si mark: "))

# total = nep+eng+mat+com+sic
# per = total/5

# if per>90:
#     print("Grade A")
# elif per>70 and per<=90:
#     print("Grade B")
# elif per>50 and per<=70:
#     print("Grade C")
# else:
#     print("Fail")

# print("1. Add")
# print("2. Sub")
# print("3. Mul")
# print("4. Div")

# num = int(input("Enter your choice: "))
# x = int(input("Enter first number: "))
# y= int(input("Enter second number: "))

# if num==1:
#     print(x+y)
# elif num==2:
#     print(x-y)
# elif num==3:
#     print(x*y)
# elif num==4:
#     print(x/y)
# else:
#     print("Invalid choice")

# WAP to check whether a number is even or odd
# WAP to enter any number and check whether it 
# divisible by 3 and 5

# WAP to enter YEAR and check whether it is leap year or not

# Nested if else

# x=25
# y=20
# z=30

# if x>y:
#     if x>z:
#         print("X is greater then y and z")
#     else:
#         print("Z is greater than x and y")
# else:
#     if y>z:
#         print("Y is greater than x and z")
#     else:
#         print("Z is greater than x and y")


# if x>y and x>z:
#     print("x is greater than y")
# elif y>x and y>z:
#     print("y is greater than x")
# elif x==y and x==z:
#     print("x,y and z are equal")
# else:
#     print("z is greater than x and y")

# username='admin'
# password ='admin002'

# if username=='admin':
#     if password=='admin002':
#         print("Login success")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")

# if username=='admin' and password=='admin003':
#     print("Login success")
# else:
#     print("Login failed")

# print("===========ATM===========")
# pin = int(input("Enter your pin: "))

# if pin==1234:
#     my_amount=10000
#     print("1. Withdraw")
#     print("2. Check balance")
#     option = int(input("Enter your choice: "))
#     if option==1:
#         amount=int(input("Enter amount to withdraw: "))
#         if amount>my_amount:
#             print("Insufficient balance")
#         else:
#             new_balance=my_amount-amount
#             print("Withdrawn amount: ",amount)
#             print("Remaining balance: ",new_balance)
           
#     elif option==2:
#         print("Your balance is: ",my_amount)
#     else:
#         print("Invalid option")
# else:
#     print("Invalid pin")

# age = int(input("Enter your age: "))

# 18 > 
# 40<

# 1-25 -> cooke
# 25-30-> BEER
# 30-40-> WHISKY

# age  = int(input("Enter your age: "))
# if age<18:
#     print("You are child")

# elif age>=18 and age<=25:
#     print("You can eat cooke")
# elif age>25 and age<=30:
#     print("You can drink beer")
# elif age>30 and age<=40:
#     print("You can drink whisky")
# else:
#     print("You are old")

# users=[
#     ['admin','admin002'],
#     ['user','user002'],
# ]

# username = input("Enter your username: ")
# password = input("Enter password: ")

# if users[0][0]==username and users[0][1]==password:
#     print("Welcome: ",username)
# elif users[1][0]==username and users[1][1]==password:
#     print("Welcome: ",username)
# else:
#     print("username & password not match")

# x=900
# y=50
# z=600

# if x>y and x>z:
#     if y>z:
#         print(x,y,z)
#     else:
#         print(x,z,y)
# elif y>x and y>z:
#     if x>z:
#         print(y,x,z)
#     else:
#         print(y,z,x)
# else:
#     if x>y:
#         print(z,x,y)
#     else:
#         print(z,y,x)


# students=[
#     {'username':"ram","password":"ram002"},
#     {'username':"shyam","password":"shyam002"}
# ]


# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if students[0]['username']==username and students[0]['password']==password:
#     print("Welcome: ",username)
# elif students[1]['username']==username and students[1]['password']==password:
#     print("Welcome: ",username)
# else:
#     print("Invalid username and password")

# alternative of switch cas
# language='nep'

# match language:
#     case 'nep':
#         print("Nepali")
#     case 'eng':
#         print("English")
#     case 'hin':
#         print("Hindi")
#     case 'chi':
#         print("Chinese")
#     case _:
#         print("Invalid language")


emp=[
    {"name":"ram","age":20,"dep":"IT"},
    {"name":"shyam","age":25,"dep":"HR"}
]

dep =input("Enter department: ").upper()
if emp[0]['dep']==dep:
    print(emp[0]['name'],"salary is 50000")
elif emp[1]['dep']==dep:
    print(emp[1]['name'],"salary is 30000")
else:
    print("Invalid department")


# for loop
# while loop
# nested loop

# function
