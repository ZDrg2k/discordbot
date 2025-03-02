from .UserClass import User
import discord
from discord import Message

active_users : dict[int,User] = {}

#\

def print_users():
    print(active_users)
    for user in active_users:
        print(user)
    if(len(active_users) == 0):
        print("No users to print")
    return