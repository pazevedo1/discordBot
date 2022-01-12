import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

with open("bannedWords.txt") as file:
    bannedWords = [word.strip().lower() for word in file.readlines()]

@client.event
async def on_ready():
    print('Bot is ready')

client.event
async def on_message(message):
    print(message.content)

channel = client.get_channel("771303091936296973")

@client.event
async def on_member_join(member):
    print(f'(member) is a big gay')

@client.event
async def on_member_remove(member):
    print(f'(member) left the server')

@client.event
async def on_message(message):
    for word in bannedWords:
        if message.content.count(word) > 0:
            print("Your message was yeeted from this server")
            await message.channel.purge(limit=1)
            await message.channel.send("Your message was yeeted from this server")

    await client.process_commands(message)

client.run('NzcxMzA0NTIzMDc0ODk1ODcy.X5qLUA.8pfLAaPMrk1OMlEHIQgcoVa9x8A')

