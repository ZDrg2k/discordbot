import discord
from discord.ext import commands
from utils.database import dbtotxt, printdb
from usrmgmt.user_manager import print_users

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down...")
        # shut the bot down 
        await self.bot.close()
    
    @commands.command()
    @commands.is_owner()
    async def dumpdb(self,ctx):
        # dump the database
        await ctx.send("Dumping database")
        dbtotxt()

    @commands.command()
    @commands.is_owner()
    async def printusers(self,ctx):
        await ctx.send("Printing users now...")
        print_users()
        print("Printed all users!")
        await ctx.send("All users printed!")

    @commands.command()
    @commands.is_owner()
    async def printdb(self,ctx):
        # print the database
        await ctx.send("Printing database")
        printdb()


async def setup(bot):
    print("Loading Admin cog")
    await bot.add_cog(Admin(bot))

