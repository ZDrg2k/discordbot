# this file deals with database stuff :(
# I dont remember how to do most of this
# oh well, time to ask my wife (githubcopilot)
# she's the best

import sqlite3
from usrmgmt.UserClass import User
from usrmgmt.user_manager import active_users

DB_PATH = "data/UserSaveData.db"

def init_db():

# connect to the database
# creates it if it doesnt exist
    db = sqlite3.connect(DB_PATH)
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
            level INTEGER DEFAULT 1, -- User Level
            xp INTEGER DEFAULT 0, -- Ex
            money REAL DEFAULT 0.0 -- Users Money
        )
    ''')
    db.commit() # commit the changes
    db.close() # close the database
    # only opens the database when writing or reading from it
    # this is to prevent the database from being open all the time

# function to add a user to the database
def add_user(user : User):
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()

    # tries to add the user
    try:
        cursor.execute('''
                INSERT INTO users (id, level, xp, money)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET 
                    level = excluded.level, 
                    xp = excluded.xp, 
                    money = excluded.money
            ''', (user.discord_id, user.level, user.xp, user.money)
        )
        db.commit()
    except sqlite3.Error as e:
        print("Error when adding user")
        print(f"Database error has occured: {e}")
    finally:
        db.close()

def grab_user(user_id : int) -> User | None:
    print(f"DEBUG: trying to grab user with id {user_id}")
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    try:
        cursor.execute('SELECT * FROM users WHERE id = ?',(user_id,))
        row = cursor.fetchone()
        
        if row:
            print("User was found")
            # creates a user object and returns it
            new_u = User(row[0])
            new_u.level = row[1]
            new_u.xp = row[2]
            new_u.money = row[3]
            return new_u
        else:
            # returns none
            return None

    except sqlite3.Error as e:
        print("Error while grabbing user")
        print(f"Database error has occured: {e}")
        return None
    finally:
        db.close()


def printdb():

    db = sqlite3.connect('data/UserSaveData.db')
    cursor = db.cursor()
    print("Printing database")
    try:
        cursor.execute('''
            SELECT * FROM users
        ''')
        for user in cursor.fetchall():
            print(user)
        print("Database printed")
    except sqlite3.Error as e:
        print("Error printing database")
        print(e)
    finally:
        db.close()


# this should make a .txt file with all the users in the database
# for debugging
def dbtotxt():
    print("Writing database to txt file")
    db = sqlite3.connect('data/UserSaveData.db')
    cursor = db.cursor()
    try:
        cursor.execute('''
            SELECT * FROM users
        ''')
        with open("database_dump.txt", "w") as f:
            for user in cursor.fetchall():
                f.write(f"{user}\n")
        print("Database written to txt file")
    except sqlite3.Error as e:
        print("Error writing database to txt file")
        print(e)
    finally:
        db.close()
# this should make a .txt file with all the users in the database