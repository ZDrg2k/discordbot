import discord
from discord.ext import commands
from config.config import Config

bot = commands.Bot(
    command_prefix=Config.PREFIX,
    intents=discord.Intents.all(),
    owner_id=Config.OWNER_ID,
)


