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

#Commands
'''Marco Polo'''
@client.command()
async def marco(ctx):
    await ctx.send(f"Polo! (Latency: {round(client.latency * 1000)} ms)")

'''Magic 8 Ball'''
@client.command(aliases=['8ball'])
#alias for function name
async def magic8ball(ctx, *, question):

    responses = ["Hell yeah!","It is likely.","Yessir!","Obviously.","YAASSS","Without a doubt.",
    "Ask again later.","I forgot what you asked, can you say it again?","Try again later.","I dont know im just an 8ball.","Im not smart enough to answer this, try again when Im older.",
    "No.","Not looking too good.","Hell no!","Oooof, nah fam.","Very doubtful"]

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

'''Jokes'''
@client.command()
async def joke(ctx):
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

    client.run("Insert token here")
