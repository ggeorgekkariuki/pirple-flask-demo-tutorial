import sqlite3

connection = sqlite3.connect('pirple_flask_demo_tutorial.db', check_same_thread=False)

cursor = connection.cursor()

# Populate the User Table in the schema with the data
cursor.execute(
    """
    INSERT INTO users (
        username,
        password,
        favorite_color
    ) VALUES (
        'GORDON',
        'RAMSEY',
        'RED'
    );
    """
)

cursor.execute(
    """
    INSERT INTO users (
        username,
        password,
        favorite_color
    ) VALUES (
        'JIM',
        'HALPERT',
        'BLUE'
    );
    """
)

cursor.execute(
    """
    INSERT INTO users (
        username,
        password,
        favorite_color
    ) VALUES (
        'WAYNE',
        'BRUCE',
        'BLACK'
    );
    """
)

cursor.execute(
    """
    INSERT INTO users (
        username,
        password,
        favorite_color
    ) VALUES (
        'SELINA',
        'MARQUEZ',
        'BURGENDY'
    );
    """
)

cursor.execute(
    """
    INSERT INTO users (
        username,
        password,
        favorite_color
    ) VALUES (
        'JUSTIN',
        'LI',
        'WHITE'
    );
    """
)

cursor.execute(
    """
    INSERT INTO users (
        username,
        password,
        favorite_color
    ) VALUES (
        'George',
        'george',
        'GREEN'
    );
    """
)


# Once you are done with the database operations, close the connection and the cursor object.
connection.commit()
cursor.close()
connection.close()


# import sqlite3

# # This method returns the color of the selected Username from the Users Table in the DB
# def show_color(username):
#     # Open the database via the connection
#     connection = sqlite3.connect('pirple_flask_demo_tutorial.db', check_same_thread=False)
#     cursor = connection.cursor()

#     # Execute the command
#     cursor.execute(
#         """
#         SELECT favorite_color FROM users WHERE username = '{username}' ORDER BY pk DESC;
#         """.format(username = username)
#     )

#     # Save the first item in the cursor
#     color = cursor.fetchone()[0]

#     # Close the database
#     connection.commit()
#     cursor.close()
#     connection.close()

#     # The Return
#     message = "Your login was successful! { username }'s favorite color is { color }.".format(username=username, color=color)
#     return message
