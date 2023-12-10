import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='mnist',
            user='root',
            password='root'
        )
        if connection.is_connected():
            print('Connected to MySQL database')

            return connection

    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def close_connection(connection):
    """ Close MySQL connection """
    if connection.is_connected():
        connection.close()
        print('Connection closed')

def insert_blob_data(connection, file_path, result):
    """ Insert BLOB data into the database """
    try:
        cursor = connection.cursor()

        with open(file_path, 'rb') as file:
            binary_data = file.read()

        # inserting BLOB data
        query = "INSERT INTO images (image,prediction) VALUES (%s, %s)"
        cursor.execute(query, (binary_data,result))

        connection.commit()
        print('BLOB data inserted successfully')
        

    except Error as e:
        print(f"Error inserting to database: {e}")

def main(result):

    connection = connect()

    if connection:
        file_path = 'src\image.jpg'
        insert_blob_data(connection, file_path, result)
        
        #close the connection
        close_connection(connection)

if __name__ == "__main__":
    main()
