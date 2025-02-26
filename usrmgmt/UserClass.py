
# class that stores user information
# dont sent any of the variables to anything, for now
class User:
    def __init__(self, discord_id, user_name, display_name):
        self.discord_id = discord_id
        self.user_name = user_name
        self.display_name = display_name
    
    def print_info(self):
        print(f"Discord ID: {self.discord_id}")
        print(f"User Name: {self.user_name}")
        print(f"Display Name: {self.display_name}") 