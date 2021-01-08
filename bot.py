import discord
from discord.ext import commands
import random

#Reference: https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ&index=1

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

#Create command prefix
# client = commands.Bot(command_prefix = "$", intents = intents)
client = commands.Bot(command_prefix = ".", intents = intents)

@client.event
async def on_ready():
    #When bot is ready
    print("Bot is ready!") 

#When user joins or leaves the server
@client.event
async def on_member_join(member):
    print(f"Hello {member}, welcome to the server!")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server.")

client.run("Insert token here")