import discord
from discord.ext import commands
import json
import asyncio


client = commands.Bot(command_prefix = '.')
with open("bannedWords.txt") as file:
    bannedWords = [word.strip().lower() for word in file.readlines()]

@client.event
async def on_ready():
    print('Bot is ready')

client.event
async def on_message(message):
    print(message.content)

@client.command()
async def kick(ctx, member : discord.Member, *,reason=None):
    print(f"(member) has been kicked, due to (reason)")
    await message.channel.send(f"(member) has been kicked, due to (reason)")
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *,reason=None):
    if (reason==None):
        embed = discord.Embed(title=f"{ctx.author.name}, you forgot a reason.", color=0xfbff00)
        await ctx.send(embed=embed)
        #print(f"{ctx.author.name}, you forgot a reason.")
        #await ctx.send(embed=embed)
        #await message.channel.send(f"{ctx.author.name}, you forgot a reason.")
        #return
    else:
        embed = discord.Embed(title=f"(member) has been banned",description = reason, color=0xfbff00)
        #print(f"(member) has been banned, due to (reason)")
        await ctx.send(embed=embed)
        await member.ban(reason=reason)
        #await message.channel.send(f"(member) has been banned, due to (reason)")
@client.command()
async def unban(ctx, *, member):
    banUser = await ctx.guild.bans()
    userName, userNum = member.split('#')
    for banList in banUser:
        user = banList.user
        if (user.name, user.discriminator)==(userName, userNum):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"{user.mention} comes crawling back")
@client.event
async def on_member_join(member):
    print(f'{member} is a big gay')

@client.event
async def on_member_remove(member):
<<<<<<< HEAD
    print(f'(member) left the server')

client = discord.Client()

YOURTOKEN = None
YOURGUILDSID = None
YOURID = None
YOURFILENAME = None # with .json (or txt, etc. at the and)

# it may throw an error when a member joins when the bot isn't running

m = {}

@client.event
async def on_ready():
    global m
    with open(YOURFILENAME, "r") as j:
        m = json.load(j)
        j.close()
    if len(m) == 0:
        m = {}
        for member in client.get_guild(YOURGUILDSID).members:
            m[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}
    print("ready")
    while True:
        try:
            for member in client.get_guild(YOURGUILDSID).members:
                m[str(member.id)]["messageCountdown"] -= 1
        except:
            pass
        await asyncio.sleep(1)

@client.event
async def on_message(message):
    global m
    if message.content == "!stop" and message.author.id == YOURID:
        with open(YOURFILENAME, "w") as j:
            j.write( json.dumps(m) )
            j.close()
        await client.close()
    elif message.content == "!xp":
        await message.channel.send( str(m[str(message.author.id)]["xp"]) )
    elif message.author != client.user:
        if m[str(message.author.id)]["messageCountdown"] <= 0:
            m[str(message.author.id)]["xp"] += 10
            m[str(message.author.id)]["messageCountdown"] = 10

@client.event
async def on_member_join(member):
    m[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}

client.run(YOURTOKEN)

    print(f'{member} left the server')

@client.event
async def on_message(message):
    for word in bannedWords:
        if message.content.count(word) > 0:
            print("Your message was yeeted from this server")
            await message.channel.purge(limit=1)
            await message.channel.send("Your message was yeeted from this server")

    await client.process_commands(message)
client.run('NzcxMzA0NTIzMDc0ODk1ODcy.X5qLUA.8pfLAaPMrk1OMlEHIQgcoVa9x8A')
 146892abb7b041ccb1b478ad56b7d0e52b0fbaca
