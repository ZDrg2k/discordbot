import discord
from discord.ext import commands
from usrmgmt.user_manager import active_users, User
from utils.database import grab_user

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def add_to_active(self,user_id):
        user : User = grab_user(user_id) # grabs a user from the db
        if(user == None):
            print(f"User: {user_id} not in db, ignoring ")
            return
        else:
            active_users[user.discord_id] = user
            # the user was found in the db
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        print(f"Message from {message.author.id}: {message.content}")

        # if the author is not in active users
        if not (message.author.id in active_users):
            self.add_to_active(message.author.id)

async def setup(bot):
    print("Loading Listener cog")
    await bot.add_cog(Listener(bot))

