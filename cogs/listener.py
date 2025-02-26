import discord
from discord.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

async def setup(bot):
    print("Loading Listener cog")
    await bot.add_cog(Listener(bot))

