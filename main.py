import mysql.connector
from mysql.connector import errorcode
import toml

config = toml.load("config.toml")

ip = config["database"]["IP"]
porta = config["database"]["PORT"]
nick = config["database"]["USERNAME"]
pswd = config["database"]["PASSWORD"]
DB = config["database"]["DATABASE"]

try:
    connection = mysql.connector.connect(user=nick, password=pswd, host=ip, port=porta, database=DB)

except mysql.connector.Error as error:
    if error.errno == errorcode.CR_UNKNOWN_HOST:
        print("Host not found, maybe the ip or port is wrong?")
    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("username and password does not match")
    else:
        print(error)


def main():
    print("1 - Insert data")
    print("2 - Select data")
    print("3 - Update data")
    print("4 - Delete data")
    option = int(input("Select a option: "))

    if option == 1:
        name = input("Name: ")
        address = input("Address: ")
        insert_data(name, address)
    elif option == 2:
        id = int(input("ID: "))
        select_data(id)
    elif option == 3:
        id = int(input("ID: "))
        name = input("Name: ")
        address = input("Address: ")
        update_data(id, name, address)
    elif option == 4:
        id = int(input("ID: "))
        delete_data(id)

def insert_data(name, address):
    cursor = connection.cursor()
    try:
        query = "INSERT INTO Clientes (name, address) VALUES (%s, %s)"
        data = (name, address)
        cursor.execute(query, data)

        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as error:
        print(f"Failed to insert data because of {error}")
    finally:
        cursor.close()

def select_data(id):
    cursor = connection.cursor(buffered=True)
    try:
        query = "SELECT * FROM Clientes WHERE id = (%s)"
        data = (id,)
        cursor.execute(query, data)

        connection.commit()
        results = cursor.fetchall()

        for x in results:
            print(x)

    except mysql.connector.Error as error:
        print(f"Failed to select data because of {error}")
    finally:
        cursor.close()


def update_data(id, name, address):
    cursor = connection.cursor()
    try:
        query = "UPDATE Clientes SET name = %s, address = %s WHERE ID = %s"
        data = (name, address, id)
        cursor.execute(query, data)

        connection.commit()
        print("Data updated successfully")
    except mysql.connector.Error as error:
        print(f"Failed to update data because of {error}")
    finally:
        cursor.close()

def delete_data(id):
    cursor = connection.cursor()
    try:
        query = "DELETE FROM Clientes WHERE id = %s"
        data = (id,)
        cursor.execute(query, data)
        connection.commit()

        print("Data deleted sucessfully")
    except mysql.connector.Error as error:
        print(f"Failed to delete data because of {error}")
    finally:
        cursor.close()

if __name__ == "__main__":
    main()