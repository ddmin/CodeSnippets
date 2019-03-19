import discord
from discord.ext import commands
import random

def generate_insult():
    return random.choice(['You\'re a failure',
                          'You should kill yourself',
                          'You are useless',
                          'Jump off a cliff',
                          'You are hopeless',
                          'You\'re a wanker',
                          'You\'ll never amount to anything'])

TOKEN = 'NTAwMTI0ODEzMzIzNTM0MzQ3.DqGRvQ.6eouj3eAWSZ0aygz7Ase_02opOU'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Self-Loathing-Bot is online.')


@client.event
async def on_message(message):
    
    channel = message.channel
    author = str(message.author)
    
    if message.content.startswith('!motivate me'):
        await client.send_message(channel, f'{generate_insult()} {author}.')

    if message.content.startswith('!gayness'):
        await client.send_message(channel, f'Gay Level: {random.randint(50, 100)}%')

    if message.content.startswith('!help'):
        await client.send_message(channel, f'Go figure it out yourself, {author}\n!motivate me: Insults you\n!gayness: Calls you gay')

client.run(TOKEN)
