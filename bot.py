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

'''Clear messages'''
@client.command()
async def clear(ctx, amount=5):
    #Need to add 1 because it clears the initial command message itself
    #Check permission, reference: https://www.youtube.com/watch?v=THj99FuPJmI&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ&index=5
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission for this command.")

'''Kick and Ban'''
#Kick
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    #make member a discord member object
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")

@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission for this command.")

#Ban
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    #make member a discord member object
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")

@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission for this command.")

#Unban
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    #Seperate the name and discriminator
    member_name, member_discrimanator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discrimanator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
            return

    client.run("Insert token here")
