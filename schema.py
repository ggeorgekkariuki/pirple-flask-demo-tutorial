import sqlite3

# Create a connection
connection = sqlite3.connect('pirple_flask_demo_tutorial.db', check_same_thread=False)

# Create a cursor object that will be used to access the database
cursor = connection.cursor()

# Create the Database Tables Users - Primary Key, Username, Password, Favourite Color
cursor.execute(
    """
    CREATE TABLE users (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32),
        favorite_color VARCHAR(16)
    );
    """
)

# Once you are done with the database operations, close the connection and the cursor object.
connection.commit()
cursor.close()
connection.close()