import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="crmData",
        user="postgres",
        password="Provera@2016"
    )
    return conn

def create_customers_table():
    """ create a table in the PostgreSQL database"""
    command = """
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(100) NOT NULL,
            lastname VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL
        )
        """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = connect()
        cur = conn.cursor()
        # create table
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("Table created successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def list_customers():
    command="SELECT * FROM customers"
    conn=connect()
    cur= conn.cursor()
    cur.execute(command)
    rows= cur.fetchall()
    for row in rows:
        print(f'id: {row[0]} firstname: {row[1]} lastname: {row[2]} age: {row[3]}')
    conn.close()

def add_customer(firstname,lastname,age):
    command="INSERT INTO customers(firstname,lastname,age) VALUES (%s,%s,%s)"
    conn=connect()
    cur=conn.cursor()
    cur.execute(command,(firstname,lastname,age))
    conn.commit()
    print("Customer added seccessfully")
    conn.close()

def update_customer(id,firstname,lastname,age):

    command="UPDATE customers SET firstname = %s ,lastname=%s,age=%s WHERE id=%s"
    conn=connect()
    cur=conn.cursor()
    cur.execute(command,(firstname,lastname,age,id))
    conn.commit()
    print("Customer updated successfully")
    conn.close()

def delete_customer(id):
    command= "DELETE FROM customers WHERE id =%s RETURNING id"
    conn=connect()
    cur=conn.cursor()
    cur.execute(command,(id,))
    result = cur.fetchone()
    if result is None:
        print("No customer found with id:", id)
    else:
        print("Customer deleted successfully")
    conn.commit()
    conn.close()
def menu():
    create_customers_table()
    while True:
        print("1. List customers")
        print("2. Add customer")
        print("3. Update customer")
        print("4. Delete customer")
        print("5. Quit")
        option = int(input("Select an option: "))
        if option == 1:
            list_customers()
        elif option == 2:
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            age = int(input("Enter age: "))
            add_customer(firstname, lastname, age)
        elif option == 3:
            id = int(input("Enter customer id to update: "))
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            age = int(input("Enter age: "))
            update_customer(id, firstname, lastname, age)
        elif option == 4:
            id = int(input("Enter customer id to delete: "))
            delete_customer(id)
        elif option == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()