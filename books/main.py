import getpass


books_data=[
    {'id':1,'name':'Python','author':'Guido van Rossum','price':500,'qty':10},
    {'id':2,'name':'Java','author':'James Gosling','price':400,'qty':20},
    
]

def register():
    username = input("Enter username: ").strip()
    if username in open('books/users.txt').read():
        print("User already exists")
        exit()
    
    password = getpass.getpass("Enter password: ").strip()
    comfirm_password = getpass.getpass("Comfirm password: ").strip()
    if password != comfirm_password:
        print("Password mismatch")
        exit()

    handle = open('books/users.txt', 'a')
    handle.write(f"username:{username},password:{password}")
    handle.write("\n")
    handle.close()
    print("User registered successfully")
    exit()


def login():
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    handle = open('books/users.txt', 'r')
    users = handle.readlines()
    is_login=False
    for user in users:
        user = user.strip()
        user = user.split(',')
        uname = user[0].split(':')[1]
        upass = user[1].split(':')[1]
        if uname == username and upass == password:
            is_login = True
    if is_login:
        print("Login success")
        for book in books_data:
            print(f"Book ID: {book['id']}, Name: {book['name']}, Author: {book['author']}, Price: {book['price']}, Qty: {book['qty']}")
    else:
        print("Login failed")     
    


login()