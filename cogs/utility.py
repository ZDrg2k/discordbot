import discord
from discord.ext import commands
from usrmgmt.user_manager import  print_users, active_users
from usrmgmt.UserClass import User
from utils.database import grab_user, add_user
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Ping: {round(self.bot.latency * 1000)}ms")
    
    @commands.command()
    async def listusers(self, ctx):
        print("Hi this command is working fine!")
        print_users()
    
    @commands.command()
    async def register(self, ctx):
        try:
            # sends this fine
            await ctx.reply("Attempign to register...")
            # sends this fine
            print("Setting user = to ctx.author") # removed this as it seemed to cause issues??
            # its never gotten past this point??? im so confused

            # doesnt print
            print(F"User: {ctx.author.id} Is attempting to register...")
            print("Grabbing now!")
            user_i = grab_user(ctx.author.id)

            print(f"what was grabbed: {user_i}")
            if(not user_i):
                # add them to the databse
                print(f"User {ctx.author.id} not found in database... attempting to add")

                # checks if a User instance already exists for them
                if(ctx.author.id in active_users):
                    print("User found in active users, adding")
                    add_user(active_users[ctx.author.id])
                # else creates an instance for them
                # and adds it to the db
                else:
                    print("Creating new user...")
                    add_user(User(ctx.author.id,))
            else:
                await ctx.send("You are already in the databse")
        except Exception as e:
            print(f"Registereation error occured: {e}")
        print("Register command over")

        
        
async def setup(bot):
    print("Loading Utility cog")
    await bot.add_cog(Utility(bot))
    

