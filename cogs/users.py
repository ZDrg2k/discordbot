import discord
from discord.ext import commands
from usrmgmt.user_manager import active_users
from utils.database import add_user,grab_user

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx):
        # are they in active users?
        user = ctx.author
        if(user in active_users):
            active_users[user.id].print_status()
        else:
            await ctx.reply("Error: User isnt detected")

    @commands.command()
    async def save(self,ctx):
        user = ctx.author
        if(user.id in active_users):
            # then we can save just fine
            try:
                add_user(active_users[user.id])
                await ctx.reply("Succesfully saved!")
            except:
                await ctx.reply("Error: something went wrong")
        else:
            await ctx.reply("Im to lazy to fill all the logic in")
            await ctx.send("You probably arent registered")
            # if not in active users
            # this should only really happen if not registered



async def setup(bot):
    print("Loading Listener cog")
    await bot.add_cog(Users(bot))

