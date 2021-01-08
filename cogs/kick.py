'''Kick'''
import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
    #make member a discord member object
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member.mention}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission for this command.")
            
            
def setup(client):
    client.add_cog(Kick(client))