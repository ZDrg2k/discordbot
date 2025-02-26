import discord
from discord.ext import commands
from usrmgmt.user_manager import active_users, User
from utils.database import get_from_db
from usrmgmt.user_manager import add_user

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        print(f"Message from {message.author}: {message.content}")

    def check_db(self,message):
        # checks if the user is already in active users
        if message.author_id in active_users:
            return

        # if they are not, check if they are in the database
        # if they are, add them to active users
        if get_from_db(message.author_id):
            add_user(message.author_id, message.author.name, message.author.display_name)
            return
        else:
            print(f"Error adding {message.author} to active users")
            print(f"User {message.author} not found in database")
            return
        # if they are not, do not add them to the database
        # because I need explicit permission to do so
    

async def setup(bot):
    print("Loading Listener cog")
    await bot.add_cog(Listener(bot))

