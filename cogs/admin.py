import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down...")
        # shut the bot down 
        await self.bot.close()

async def setup(bot):
    print("Loading Admin cog")
    await bot.add_cog(Admin(bot))

