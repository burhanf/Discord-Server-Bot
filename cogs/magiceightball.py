'''Magic 8 Ball'''
import discord
from discord.ext import commands
import random

class Magic8Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    #alias for function name
    async def magic8ball(self, ctx, *, question):

        responses = ["Hell yeah!","It is likely.","Yessir!","Obviously.","YAASSS","Without a doubt.",
    "Ask again later.","I forgot what you asked, can you say it again?","Try again later.","I dont know im just an 8ball.","Im not smart enough to answer this, try again when Im older.",
    "No.","Not looking too good.","Hell no!","Oooof, nah fam.","Very doubtful"]

        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
def setup(client):
    #pass in an instance of the class
    client.add_cog(Magic8Ball(client))
