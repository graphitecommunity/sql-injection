import sqlite3

def connect_to_db():
    connection = sqlite3.connect('user_data.db')

    return connection

def get_user_input():
    customer = input("Enter a name")
    return customer

def print_result(results):

    try:
        for row in results:
            print(row)
    except TypeError as error:
        print(error)

def create_table():
    connection = connect_to_db().cursor()

    try:
        query = "create table user_data (firstname, lastname)"
        
        connection.execute(query)

        connection.close()

        print("Table crated successfully")

    except sqlite3.OperationalError as error:

        print(error)
        delete_data()
        create_table()

def insert_data():
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        query = "INSERT INTO user_data VALUES ('Qowiyyu', 'Adelaja'), ('Qudus', 'Babalola'), ('Tom', 'Blue')"
        cursor.execute(query)
        connection.commit()
        connection.close()
        print("Data Added to table successfully")

    except sqlite3.OperationalError as error:
        print(error)

def delete_data():
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        query = "DROP TABLE user_data"
        cursor.execute(query)
        connection.commit()
        connection.close()
        print("All data Deleted")
    except sqlite3.OperationalError as error:
        print(error)

def vulnerable_code(name):

    try:
        print(f"The entered name is {name}")
        query = f"SELECT firstname, lastname FROM user_data WHERE firstname = '{name}'"

        cursor = connect_to_db().cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    except sqlite3.OperationalError as error:
        print(error)


def non_vulnerable_code(name):

    try:
        print(f"The entered name is {name}")
        query = f"SELECT firstname, lastname FROM user_data WHERE firstname = ?"

        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute(query, (name,))
        return cursor.fetchall()

    except sqlite3.OperationalError as error:
        print(error)

if __name__ == "__main__":
    create_table()
    insert_data()
    name = get_user_input()
    print("\n\nVULNERABLE CODE RESULT TO FIND QOWIYYU IN THE DATABASE\n\n")
    result = vulnerable_code(name)
    print_result(result)

    print("\n\nNON-VULNERABLE CODE RESULT TO FIND QOWIYYU IN THE DATABASE\n\n")
    result = non_vulnerable_code(name)
    print_result(result)