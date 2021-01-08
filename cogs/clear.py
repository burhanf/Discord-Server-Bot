'''Clear messages'''
import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=5):
    #Need to add 1 because it clears the initial command message itself
    #Check permission, reference: https://www.youtube.com/watch?v=THj99FuPJmI&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ&index=5
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            await ctx.channel.purge(limit=amount + 1)

    @clear.error
    async def clear_error(self, ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission for this command.")
            
            
def setup(client):
    client.add_cog(Clear(client))

