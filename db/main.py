import sqlite3
conn = sqlite3.connect('db/college.sqlite3')
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                address TEXT NOT NULL
                )
    """)
    conn.commit()


def insert_student(name,email,address):
    cursor.execute("""
        INSERT INTO students (name, email, address)
        VALUES (?,?,?)
        """,(name,email,address))
    conn.commit()
    print("data inserted successfully")

# name = input("Enter name: ")
# email = input("Enter email: ")
# address = input("Enter address: ")
# insert_student(name,email,address)


def delete(id):
    cursor.execute("""
        DELETE FROM students WHERE id = ?
    """,(id,))
    conn.commit()
    print("data deleted successfully")


# delete(1)


def update(name,address,id):
    cursor.execute("""
        UPDATE students SET name = ?, address = ? WHERE id = ?
    """,(name,address,id))
    conn.commit()
    print("data updated successfully")

update("Rajesh","Kathmandu",2)

def show_students():
    cursor.execute("""
        SELECT * FROM students
    """)
    students = cursor.fetchall()
    # students = cursor.fetchone()
    # students = cursor.fetchmany(2)
    print(students)
show_students()

