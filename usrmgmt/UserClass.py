import discord

# class that stores user information
# dont sent any of the variables to anything, for now
class User:
    def __init__(self, discord_id):
        self.discord_id = discord_id
        self.level : int = 1
        self.xp : int = 0
        self.money : float = 0.0
    
    async def print_status(self,ctx):
        user = ctx.author
        # should reply to the user with a nice box, displaying the uesrs stats
        status_embed = discord.Embed(
            title = "Status: ",
            color=discord.Color.blue()
        )
        status_embed.set_thumbnail(url=user.display_avatar.url)
        status_embed.fiels(name="Level",value=str(self.level),inline =  True)
        status_embed.add_field(name="XP", value=str(self.xp), inline=True)
        status_embed.add_field(name="Money", value=f"${self.money:.2f}", inline=True)

    def debug_print_info(self):
        print(f"Discord ID: {self.discord_id}")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp} ")
        print(f"money: {self.money}")