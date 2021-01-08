import discord
from discord.ext import commands

class MarcoPolo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    #Marco Polo
    async def marco(self, ctx):
        await ctx.send(f"Polo! (Latency: {round(self.client.latency * 1000)} ms)")

def setup(client):
    #pass in an instance of the class
    client.add_cog(MarcoPolo(client))
