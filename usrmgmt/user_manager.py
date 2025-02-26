from .UserClass import User
from discord import Message

active_users : dict[int,User] = {}

## message should be 
def add_user(message : Message):
    print(f"Attempting to add UID{message.author.id} to active users")
    if(message.author.id in active_users):
        return
        print("Failed: User already exists")
    new_user = User(message.author.id, message.author.name, message.author.display_name)
    active_users[message.author.id] = new_user
    print("User added")

def print_users():
    for user in active_users:
        active_users[user].print_info()
    if(len(active_users) == 0):
        print("No users to print")
    return