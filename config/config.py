import os
from dotenv import load_dotenv

if load_dotenv("config/tokens.env"):
    print("Loaded tokens.env")
else:
    print("tokens.env not found")

class Config:
    
    TOKEN = os.getenv("DISCORD_TOKEN") # Discord token (important, dont give to anyone else)
    PREFIX = "!" # Bot prefix
    OWNER_ID = 381909599185534976 # Your discord id 
