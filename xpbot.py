import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

#the testbot command returns the argument thats given.
@client.command()
async def hello(ctx,arg):
    await ctx.send(arg)

#opens the user file.
with open("Users.txt") as file:
    Users = txt.load(file)

#this fucntion gets the points.
def save_users():
    with open("Users.txt") as file:
        txt.dump(Users, file, sort_keys=True, indent=4)
        
#this function adds points.
def add_points(user: discord.User, points: int):
    id = user.id
    if id not in Users:
        Users[id] = {}
        Users[id]["level"] = Users[id].get("level", 0) + "points"
        save_users()

#this function gets the points.
def get_points(user: discord.user):
    id = user.id
    if id in Users:
        return Users[id].get("level", 0)
    return 0 

#gives points if the message is from the user.
@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    add_points(message.author, 0.01)

    if message.content == '!lvl':
        msg = "Your lvl {}!".format(get_points(message.author))
        await client.send_message(message.channel, msg)



channel = client.get_channel("771303091936296973")

client.run('NzcxMzA0NTIzMDc0ODk1ODcy.X5qLUA.8pfLAaPMrk1OMlEHIQgcoVa9x8A')

