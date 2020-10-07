import discord
from discord.ext import tasks, commands
from six.moves import urllib
from discord.ext import commands
import time
from datetime import datetime


#id = 456446844768354306

client = commands.Bot(command_prefix=".")
client.Work = False
client.AuthorList = ["Valentino#7570"]
client.SendMessage = False
client.MessageToSend = ""

@client.event
async def on_ready():
    print("Bot is ready.")

class BotCog(commands.Cog):
    def __init__(self):
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    
    @tasks.loop(seconds=300.0)
    async def printer(self):
        if client.Work:
            await client.Channel.send("p!work")
            


BC = BotCog()


@client.event
async def on_message(message):
    id = client.get_guild(456446844768354306)


    if message.author == client.user:
        return
    client.Channel = message.channel


    if message.content.startswith('!servus:auther:name:get'):
        await message.channel.send("Ihr Name lautet " + str(message.author) + ".")

    if str(message.author) == client.AuthorList[0]:
        if message.content.startswith('Fang an zu arbeiten, mein Sklave!'):
            client.Work = True
            await message.channel.send("Ok. Ich werde für meinen Herren arbeiten. Möge Gott mich segnene.")
        
        if message.content.startswith('Höre auf zu arbeiten, mein Sklave!'):
            client.Work = True
            await message.channel.send("Ok. Ich werde nicht mehr für meinen Herren arbeiten. Möge Gott mich segnene.")


client.run("NzYzNDE1MzMyNjIyNjk2NDg4.X33X7g.7aUGLp57PuWi8ZQSOLcQU8yyfm8")