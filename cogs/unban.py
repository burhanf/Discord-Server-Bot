'''Ban'''
import discord
from discord.ext import commands

class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        #Seperate the name and discriminator
        member_name, member_discrimanator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discrimanator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
                return

def setup(client):
    client.add_cog(Unban(client))