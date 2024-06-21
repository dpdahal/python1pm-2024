# What is function?
# A function is a block of code which only runs when it is called.
# Types of functions:
# 1. Built-in functions: len(), print(), input(), etc.
# 2. User-defined functions: Functions defined by the users themselves.


# x=10
# y=40
# print(x+y)

# x=60
# y=40
# print(x+y)

# print()

# define a function
# def message():
#     # block of code
#     print("Hello python")

# # call a function
# message()

# function accepts parameters

# def add(x,y):
#     print(x+y)


# add()
# add(10,20)
# add(30,40)

# +, -, *, /, %, **, //

# create a function that accepts user input and check if the number is even or odd


# def even_odd(num):
#     if num%2==0:
#         print("Even number")
#     else:
#         print("Odd number")


# num = int(input("Enter a number: "))
# even_odd(num)

# create a function that accepts data and times and print the data that number of times

# def my_rep(data,times):
#     for i in range(times):
#         print(data)

# my_rep("Hello",5)
# create a function that accepts of any number and print multiplication table of that number

# def mul(num):
#     for i in range(1,11):
#         print(num,"*",i,"=",num*i)

# num = int(input("Enter a number: "))
# mul(num)


# def total(numbers):
#     sm =0
#     for x in range(len(numbers)):
#         sm+=numbers[x]
#     print(sm)


# total([10,20,30,40,50])


# optional arguments

# def user(name,age=0):
#     print("Name: ",name)
#     print("Age: ",age)

# user("Ram",40)


# function return value 


# def add(x,y):
#     return x+y


# result = add
# print("total: ",result(5,7))


# def add_sub(x,y):
#     t = x+y
#     s = x-y
#     return [t,s]

# result = add_sub(10,5)
# print(result)

# function scope

# global: variable declared outside the function and can be accessed inside the function or anywhere in the program
# local: variable declared inside the function and can be accessed only inside the function


# x=50

# def test():
#     global x
#     x=x+10
#     print(x)
   

# test()
# print(x)


# recursion: function calling itself
# lambda function: anonymous function
# nestes function: function inside a function
# function decorator: function that takes another function as an argument and extends the behavior of that function without modifying it


# def a():
#     return 30


# def b():
#     print(a())

# b()


# def take_value():
#     p =int(input("Enter the principal amount: "))
#     t =int(input("Enter the time: "))
#     r =int(input("Enter the rate: "))
#     return [p,t,r]

# def calculate():
#     data = take_value()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p*t*r/100

# def display():
#     print("Simple interest: ",calculate())

# display()


# def users():
#     return ["Ram","Shyam","Hari"]

# def search(name):
#     pass


# 5
# 5-1 =4 ->20
# 4-1 =3 ->60
# 3-1 =2 ->120
# 2-1 =1 ->120



# def fac(n):
#     if n==1:
#         return 1
    
#     return n*fac(n-1)


# print(fac(5))



# def test():
#     return 10


# a =test 
# print(a())


# sip = lambda p,t,r: p*t*r/100
# print(sip(1000,2,5))


# def total(x,y):
#     return f" Total number is {x+y}"


# def add(a,b,callback):
#     print(callback(a,b))


# add(10,20,total)


# def outer():
#     x=10
#     def inner():
#         return x
#     return inner


# a =outer()
# print(a())

# def zero_check(anyfunction):
#     def inner(x,y):
#         if y==0:
#             return "y is zero"
#         else:
#             return x+y
#     return inner


# @zero_check
# def add(x,y):
#     return x+y 


# print(add(10,0))



# args and kwargs


# def users(*args,**kwargs):
#     print(args)
#     print(kwargs)



# users("Ram",'sita','gita','hari','shyam',name='sophia',address='ktm',phone='9841000000')


# def total(*args):
#     sm=0
#     for x in args:
#         sm+=x

#     print(sm)

# total(10,20,3,40,5,60,7,80,9,100,87)


# def user(**kwargs):
#     print(kwargs['name'])


# user(name='Ram',address='ktm',phone='9841000000')

# len(),
# map(),
# filter(),
# reduce(),

# map: map(function,iterable)

# data = [10,20,3,40,5]

# def mul(x):
#     return x*2

# result = map(lambda x:x*2,data)
# print(list(result))
# result = map(mul,data)
# print(list(result))

# filter: filter(function,iterable)

# def even(x):
#     return x%2==0

# result = filter(even,data)
# print(list(result))

# reduce: reduce(function,iterable)

# module: math, random, datetime, os, sys, json, re, etc.
