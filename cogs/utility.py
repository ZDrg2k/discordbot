import discord
from discord.ext import commands
from usrmgmt.user_manager import add_user, print_users

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Ping! {round(self.bot.latency * 1000)}ms")
    
    @commands.command()
    async def listusers(self, ctx):
        print_users()
    
    @commands.command(name="register")
    async def adduser(self, ctx):
        add_user(ctx.message)
        await ctx.send("User added")

async def setup(bot):
    print("Loading Utility cog")
    await bot.add_cog(Utility(bot))

