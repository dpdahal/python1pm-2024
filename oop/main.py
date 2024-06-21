# class Laptop:
#     price=9876876

#     def brand(self):
#         print(self.price)
#         print("Dell")

#     def add(self,x,y):
#         return x+y


    

# obj = Laptop()
# # print(obj.price)
# # obj.brand()
# print(obj.add(2,3))




# class Calculator:
#     def add(self,x,y):
#         return x+y
    
#     def sub(self,x,y):
#         return x-y
    

# obj = Calculator()
# print(obj.add(2,3))
# print(obj.sub(4,2))


# class Products:
#     def add_product(self,name,price,quantity):
#         pass

#     def show_prodcut(self):
#         pass


# p = Products()
# p.add_product("Laptop",2000,2)
# p.show_prodcut()


# inheritance
# setter and getter
# scope of variable
# constructor and destructor
# method overloading
# static method
# class method
# property decorator


class Laptop:
    def __init__(self,name):
        print("I am ",name)

    def __del__(self):
        print("I am deleted")

    # def  __str__(self):
    #     pass

    # def __add__(self,other):
    #     pass

    # def __repr__(self) :
    #     pass


obj = Laptop('Dell')
