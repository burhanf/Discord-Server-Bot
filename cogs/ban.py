'''Ban'''
import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        #make member a discord member object
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member.mention}")

    @ban.error
    async def ban_error(self, ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission for this command.")
    
            
            
def setup(client):
    client.add_cog(Ban(client))
