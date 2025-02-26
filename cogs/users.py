import discord
from discord.ext import commands
from usrmgmt.user_manager import active_users

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx):
        await ctx.send(f"Current status: {ctx.author.status}")

async def setup(bot):
    print("Loading Listener cog")
    await bot.add_cog(Users(bot))

