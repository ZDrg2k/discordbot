from .UserClass import User
import discord
from discord import Message

active_users : dict[int,User] = {}

#\
def add_user(user_id: int, user_name: str, display_name: str):
    print(f"Attempting to add UID{user_id} to active users")
    if(user_id in active_users):
        return
        print("Failed: User already exists")
    new_user = User(user_id, user_name, display_name)
    active_users[user_id] = new_user
    print("User added")

def print_users():
    for user in active_users:
        active_users[user].print_info()
    if(len(active_users) == 0):
        print("No users to print")
    return