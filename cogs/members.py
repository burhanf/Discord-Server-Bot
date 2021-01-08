'''Event for when a member joins or leaves the server'''
import discord 
from discord.ext import commands

class Members(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"Hello {member}, welcome to the server!")
    
    async def on_member_remove(self, member):
        print(f"{member} has left the server.")

def setup(client):
    #pass in an instance of the class
    client.add_cog(Members(client))
