import discord
from discord.ext import commands
import re

TOKEN = 'NTAwMTQ3NjYzNTQ3NzkzNDA4.DqGmpw.WICruk1d4p9__fw36FJN5hNerVw'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Jonnyboi is online.')

@client.event
async def on_message(message):
    channel = message.channel

    s = re.compile('[Ss][Ss]?')

    if message.content.startswith('!jonnyboi ') and not message.author.bot:
        
        message = message.content[10:]
        new_sentence = re.sub(s, 'sh', message).capitalize()
        await client.send_message(channel, new_sentence)

client.run(TOKEN)
