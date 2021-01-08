'''Jokes'''
import discord
from discord.ext import commands
import random

class Jokes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jokes(self, ctx):
        jokes = ['I ate a clock yesterday, it was very time-consuming.',
    "Have you played the updated kids' game? I Spy With My Little Eye . . . Phone.",
    "A perfectionist walked into a bar...apparently, the bar wasn’t set high enough.",
    "Did you hear about the crook who stole a calendar? He got twelve months.",
    "I own the world's worst thesaurus. Not only is it awful, it's awful.",
    "So what if I don't know what 'Armageddon' means? It's not the end of the world.",
    "What's the difference between a good joke and a bad joke timing.",
    "Velcro—what a rip-off!"
    ]
        await ctx.send(random.choice(jokes))

def setup(client):
    #pass in an instance of the class
    client.add_cog(Jokes(client))