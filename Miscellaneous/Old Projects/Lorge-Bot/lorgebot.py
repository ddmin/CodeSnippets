import discord
from discord.ext import commands
import random

TOKEN = 'NTAwMTQwODAwNTE3MDc5MDY5.DqGgHA.fQ002ZYidcYvoMnbd-zNhZ2At-k'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Daniel Lorge is online.')

@client.event
async def on_message(message):

    channel = message.channel
    author = str(message.author)

    if message.content.startswith('!help'):
        await client.send_message(channel, f'That {author}, he\'s a dummy!\n!hello lorge: Greets you')

    if message.content.startswith('!hello lorge'):
        await client.send_message(channel, random.choice(['Yaow', 'Howdy', 'Yo']))

    if ' hate ' in message.content:
        await client.send_message(channel, 'YEAH! :fist: That\'s some good complaining!')

client.run(TOKEN)
