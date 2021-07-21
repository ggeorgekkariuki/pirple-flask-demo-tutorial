import sqlite3

# This method returns the color of the selected Username from the Users Table in the DB
def show_color(username):
    # Open the database via the connection
    connection = sqlite3.connect('pirple_flask_demo_tutorial.db', check_same_thread=False)
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(
        """
        SELECT favorite_color FROM users WHERE username = '{username}' ORDER BY pk DESC;
        """.format(username = username)
    )

    # Save the first item in the cursor
    color = cursor.fetchone()[0]

    # Close the database
    connection.commit()
    cursor.close()
    connection.close()

    # The Return
    message = "Your login was successful! {username}\'s favorite color is {color}.".format(username=username, color=color)
    return message

# This method checks the password
def check_password(username):
    # Open the database via the connection
    connection = sqlite3.connect('pirple_flask_demo_tutorial.db', check_same_thread=False)
    cursor = connection.cursor()

    # Check the password according to the user
    cursor.execute(
        """
        SELECT password FROM users WHERE username = '{username}' ORDER BY pk DESC;
        """.format(username = username)
    )

    password = cursor.fetchone()[0]

    # Close the database
    connection.commit()
    cursor.close()
    connection.close()

    # The return
    return password

# This method checks the password
def signup(username, password, favorite_color):
    # Open the database via the connection
    connection = sqlite3.connect('pirple_flask_demo_tutorial.db', check_same_thread=False)
    cursor = connection.cursor()

    # Check the password according to the user
    cursor.execute(
        """
        SELECT password FROM users WHERE username = '{username}' ORDER BY pk DESC;
        """.format(username = username)
    )

    # Checks if a user exists
    exists = cursor.fetchone()

    if exists is None:
        # Insert the new user here
        cursor.execute(
            """
            INSERT INTO users (
                username,
                password,
                favorite_color
            ) VALUES (
                "{username}",
                "{password}",
                "{favorite_color}"
            );
            """.format( username=username, password=password, favorite_color=favorite_color)
        )

        # Close the database
        connection.commit()
        cursor.close()
        connection.close()

    else:
        message = "User already exists in the database."
        return message

    # The return
    return ("You have been signed up successfully!")

def check_users():
    # Open the database via the connection
    connection = sqlite3.connect('pirple_flask_demo_tutorial.db', check_same_thread=False)
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(
        """
        SELECT username FROM users ORDER BY pk DESC;
        """
    )

    # Save the list of lists in the cursor
    db_users = cursor.fetchall()

    users = []

    # Add all the usernames in the list of Users
    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    # Close the database
    connection.commit()
    cursor.close()
    connection.close()

    return users