# Imports
import discord
from discord.ext import commands
from config.config import Config

import asyncio
import os

# Creating the bot
intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(
    command_prefix=Config.PREFIX,
    intents=intent, 
    owner_id=Config.OWNER_ID,
)

TOKEN = Config.TOKEN

async def load_cogs():
    # Loads all cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_cogs()
        print("Starting now")
        await bot.start(TOKEN)

asyncio.run(main())
