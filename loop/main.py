# what is loop?
# loop is a way to repeat a block of code multiple times
# there are two types of loops in python
# 1. for loop
# 2. while loop
#   . nested loop

# for loop: for loop is used to iterate over a sequence (list, tuple, string, dictionary, set)
# while loop: while loop is used to execute a block of code repeatedly as
# long as the condition is true

# data =['apple', 'banana', 'cherry',  'grape']

# for fn in data:
#     print(fn)

# students=['ram','sita','hari','ram']

# for student in students:
#     if student=='sita':
#         print(student)
        

# numbers=[34,11,13,54,67,99,88,78]
# for num in numbers:
#     # print(f"number is {num}")
#     print("number is", num)

# total=0
# for num in numbers:
#     total+=1

# print(total)

# print(list(range(10)))

# for i in range(1,10,2):
#     print(i,end=' ')

# welcome python class 10 times

# for x in range(1,11):
#     print(f"welcome to python class {x} times")

# total=0
# total_even=0
# total_odd=0

# for i in range(1,11):
#     if i%2==0:
#         total_even+=i
#     else:
#         total_odd+=i
#     total+=i
# print("Total",total)
# print("Total sum even",total_even)
# print("Total sum odd",total_odd)


# numbers=[
#     [23,45,67,89,89],
#     [34,56,78,90,12],
#     [12,34,56,78,90]
# ]

# for number in numbers:
#     for num in number:
#         print(num)


# students=[]
# num=int(input("Enter number of students: "))

# for i in range(num):
#     name = input("Enter name: ")
#     students.append(name)

# print(students)



# for x in range(1,11):
#     print(f"2 * {x} = {2*x}")
    


# students=[
#     {'id':1,'name':"ram",'address':"ktm"},
#     {'id':1,'name':"hari",'address':"ltp"},
#     {'id':1,'name':"gopal",'address':"bkt"},
#     {'id':1,'name':"sophia",'address':"bkt"},
#     {'id':1,'name':"laxmi",'address':"ktm"},

# ]

# I am ram i live in ktm

# While loop

# x=1

# while x<=10:
#     print(x)
#     x+=1
    
# x=10
# while x>=1:
#     print(x)
#     x-=1

# data=['apple', 'banana', 'cherry',  'grape']
# total =len(data)
# x=0
# while x<total:
#     print(data[x])
#     x+=1

# num_of_students=int(input("Enter number of students: "))
# students_marks=[]
# x=1

# while x<=num_of_students:
#     print(f"=====Student Id: {x}========")
#     for a in range(1):
#         nep =int(input("Enter nepali marks: "))
#         eng =int(input("Enter english marks: "))
#         math =int(input("Enter math marks: "))
#         sci =int(input("Enter science marks: "))
#         com =int(input("Enter computer marks: "))
#         total =nep+eng+math+sci+com
#         students_marks.append(total)

#     x+=1

# sid=1
# for total in students_marks:
#     per =total/5
#     grade = ''
#     if per>35 and per<=45:
#         grade='C'
#     elif per>45 and per<=60:
#         grade='B'
#     elif per>60 and per<=75:
#         grade='A'
#     elif per>75 and per<=100:
#         grade='A+'
#     else:
#         grade='F'
#     print(f"Student ID: {sid} Total marks: {total} Percentage: {per} Grade: {grade}")
#     sid+=1



# numbers=[12,13,14,15,12,13,14]
# num=[]

# for x in numbers:
#     if x not in num:
#         num.append(x)

# print(num)

# data =[12,34,65,56]
# data1=[23,45,67,78]
# x=0
# numbers=[]
# while x<len(data) and x<len(data1):
#     total =data[x]+data1[x]
#     numbers.append(total)

#     x+=1

# print(numbers)


# users=[
#     {'id':1,'name':'ram','gender':'male','status':True},
#     {'id':2,'name':'sophia','gender':'female','status':False},
#     {'id':3,'name':'hari','gender':'male','status':False},
#     {'id':4,'name':'gopal','gender':'male','status':True},
#     {'id':5,'name':'rita','gender':'female','status':False},
#     {'id':6,'name':'laxmi','gender':'female','status':True},

# ]

# total_users=len(users)
# total_male=0
# total_female=0
# total_active_user=0
# total_inactive_user=0
# total_active_male=0
# total_active_female=0
# total_inactive_male=0
# total_inactive_female=0


# for user in users:
#     if user['gender']=='male':
#         if user['status']==True:
#             total_active_male+=1
#         else:
#             total_inactive_male+=1
#         total_male+=1
#     else:
#         if user['status']==True:
#             total_active_female+=1
#         else:
#             total_inactive_female+=1
#         total_female+=1
    
#     if user['status']==True:
#         total_active_user+=1
#     else:
#         total_inactive_user+=1


# print(f"Total users: {total_users}")
# print(f"Total Male: {total_male}")
# print(f"Total Female: {total_female}")
# print(f"Total Active User: {total_active_user}")
# print(f"Total Inactive User: {total_inactive_user}")
# print(f"Total Active Male: {total_active_male}")
# print(f"Total Inactive Male: {total_inactive_male}")
# print(f"Total Active Female: {total_active_female}")
# print(f"Total Inactive feMale: {total_inactive_female}")


# users=[
#     {'username':"admin",'password':'admin'},
#     {'username':"ram",'password':'ram'},
#     {'username':"sita",'password':'sita'},
#     {'username':"hari",'password':'hari'}
# ]

# books=[
#     {'id':1,'name':'python','price':1000},
#     {'id':2,'name':'java','price':2000},
#     {'id':3,'name':'c++','price':3000},
#     {'id':4,'name':'c#','price':4000},
#     {'id':5,'name':'php','price':5000},
#     {'id':6,'name':'ruby','price':6000},
#     {'id':7,'name':'perl','price':7000},
#     {'id':8,'name':'javascript','price':8000},
#     {'id':9,'name':'html','price':9000},
#     {'id':10,'name':'css','price':10000},
# ]

# username = input("Enter username: ")
# password = input("Enter password: ")

# is_login=False

# for user in users:
#     if user['username']==username and user['password']==password:
#         is_login=True

        

# if is_login:
#     print(f"Welcome: {username}")
#     for book in books:
#         print(f"Book Id: {book['id']} Book Name: {book['name']} Book Price: {book['price']}")
# else:
#     print("Invalid username or password")


# break and continue

# for x in range(1,11):
#     if x==5 or x==7:
#         # break
#         continue
#     print(x)


# categoryData=[
#     {
#         'category_name':"laptop",
#         'products':[
#                 {'id':1,'name':'dell','price':1000},
#                 {'id':2,'name':'hp','price':2000},
#                 {'id':3,'name':'mac','price':3000},
#                 {'id':4,'name':'toshiba','price':5000},

#             ]
#     },
#     {
#         'category_name':"mobile",
#         'products':[
#                 {'id':1,'name':'samsung','price':10000},
#                 {'id':2,'name':'nokia','price':20000},
#                 {'id':3,'name':'iphone','price':30000},
#             ]
#     },
#     {
#         'category_name':"tablet",
#         'products':[
#                 {'id':1,'name':'samsung','price':1000},
#                 {'id':2,'name':'nokia','price':2000},
#                 {'id':3,'name':'iphone','price':3000},

#             ]
#     },
    

# ]

# for category in categoryData:
#     print(f"Category Name: {category['category_name']}")
#     for product in category['products']:
#         print(f"\t Product Name: {product['name']} Product Price: {product['price']}")
#     print()


# products=[
#     {'id':1,'name':'dell','price':1000},
#     {'id':2,'name':'hp','price':2000},
#     {'id':3,'name':'mac','price':3000},
#     {'id':4,'name':'toshiba','price':5000},
#     {'id':5,'name':'samsung','price':10000},
#     {'id':6,'name':'nokia','price':20000},
#     {'id':7,'name':'iphone','price':30000},
#     {'id':8,'name':'samsung','price':1000},
#     {'id':9,'name':'nokia','price':2000},
#     {'id':10,'name':'iphone','price':3000},
# ]

# search=input("Enter product name: ")

# is_product_found=False

# for product in products:
#     if product['name']==search:
#         is_product_found=True
#         print(f"Product Name: {product['name']} Product Price: {product['price']}")


# if not is_product_found:
#     print("Product not found")


users=[
    {"uid":1,"name":"ram","address":"ktm"},
    {"uid":2,"name":"sita","address":"ltp"},
]

category=[
    {"cid":1,"name":"laptop"},
    {"cid":2,"name":"mobile"},
    {"cid":3,"name":"tablet"},
]

products=[
    {"pid":1,"name":"dell","price":1000,"category_id":1},
    {"pid":2,"name":"hp","price":2000,"category_id":1},
    {"pid":3,"name":"mac","price":3000,"category_id":1},
    {"pid":4,"name":"toshiba","price":5000,"category_id":1},
    {"pid":5,"name":"samsung","price":10000,"category_id":2},
    {"pid":6,"name":"nokia","price":20000,"category_id":2},
    {"pid":7,"name":"iphone","price":30000,"category_id":2},
    {"pid":8,"name":"samsung","price":1000,"category_id":3},
    {"pid":9,"name":"nokia","price":2000,"category_id":3},
    {"pid":10,"name":"iphone","price":3000,"category_id":3},
]

orders=[
    {"oid":1,"user_id":1,"product_id":1,"quantity":2},
    {"oid":2,"user_id":1,"product_id":2,"quantity":1},
    {"oid":3,"user_id":2,"product_id":3,"quantity":3},
    {"oid":4,"user_id":2,"product_id":4,"quantity":2},
    {"oid":5,"user_id":1,"product_id":5,"quantity":1},
    {"oid":6,"user_id":1,"product_id":6,"quantity":1},
    {"oid":7,"user_id":2,"product_id":7,"quantity":3},
    {"oid":8,"user_id":2,"product_id":8,"quantity":2},
    {"oid":9,"user_id":1,"product_id":9,"quantity":1},
    {"oid":10,"user_id":1,"product_id":10,"quantity":1},
]

# name:ram
# address:ktm
# product:dell
# quantity:2
# price