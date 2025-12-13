import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Connects to the MySQL server and creates the database 'alx_book_store'.
    """
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL Server
        # NOTE: Adjust 'password' if your local setup requires one.
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Hyprince@3000'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it does not exist
            # This satisfies the requirement that the script should not fail if DB exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Print the specific success message required
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Print error message if connection fails
        print(f"Error: {e}")

    finally:
        # Close cursor and connection to free resources
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()