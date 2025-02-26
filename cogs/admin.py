import discord
from discord.ext import commands
from utils.database import dbtotxt

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


async def setup(bot):
    print("Loading Admin cog")
    await bot.add_cog(Admin(bot))

