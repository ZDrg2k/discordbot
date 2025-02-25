import os
from dotenv import load_dotenv

load_dotenv("tokens.env")

class Congig:
    TOKEN = os.getenv("DISCORD_TOKEN") # Discord token (important, dont give to anyone else)
    PREFIX = "!" # Bot prefix
    OWNER_ID = 381909599185534976 # Your discord id 