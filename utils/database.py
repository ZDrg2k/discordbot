# this file deals with database stuff :(
# I dont remember how to do most of this
# oh well, time to ask my wife (githubcopilot)
# she's the best

import sqlite3
from usrmgmt.UserClass import User
from usrmgmt.user_manager import active_users

# connect to the database
# creates it if it doesnt exist
db = sqlite3.connect('UserSaveData.db')
cursor = db.cursor()

# create the table if it doesnt exist
# it should use discord id as the primary key
# it should also, for now, just save the user username
# and their display name
# Im fairly sure you can get both of those from the users id
# so im not sure if this is needed

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY, -- Discord ID, index 0
        username TEXT, -- Discord username, index 1
        displayname TEXT -- Discord display name, index 2
    )
''')
db.commit() # commit the changes

# function to add a user to the database
def add_to_db(user: User):
    print(f"Adding user: {user.discord_id} to the database")
    cursor.execute('''
        INSERT INTO users(id, username, displayname)
        VALUES(?,?,?)
    ''', (user.discord_id, user.user_name, user.display_name))
    db.commit()


# function to get a user from the database
def get_from_db(user_id: int) -> User:
    print(f"Getting user: {user_id} from the database")
    try:
        cursor.execute('''
            SELECT * FROM users WHERE id = ?
        ''', (user_id,))
        user = cursor.fetchone()
        return User(user[0], user[1], user[2])
    except Exception as e:
        print(f"Error getting user: {user_id} from the database")
        print(e)
        return None
# function to cycle through all active users and add them to the database
def add_all_to_db():
    print("Adding all active users to the database")
    for user in active_users:
        add_to_db(active_users[user])

# this should make a .txt file with all the users in the database
# for debugging
def dbtotxt():
    print("Writing database to txt file")
    cursor.execute('''
        SELECT * FROM users
    ''')
    with open("database.txt", "w") as f:
        for user in cursor.fetchall():
            f.write(f"{user}\n")
    print("Database written to txt file")
