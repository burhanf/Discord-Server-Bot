import discord
from discord.ext import commands
import os

#Reference: https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ&index=1

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

#Create command prefix
# client = commands.Bot(command_prefix = "$", intents = intents)
client = commands.Bot(command_prefix = ".", intents = intents)

'''Commands for cogs'''
#LOAD
@client.command()
async def load(ctx, extension):
    #load extension which is our class
    client.load_extension(f"cogs.{extension}")

#UNLOAD
@client.command()
async def unload(ctx, extension):
    #load extension which is our class
    client.unload_extension(f"cogs.{extension}")

#for cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        #splice to remove the last 3 characters (the .py)
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("Insert token here")
