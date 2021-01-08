import discord 
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        #When bot is ready
        print("Bot is ready!") 

def setup(client):
    #pass in an instance of the class
    client.add_cog(Ready(client))