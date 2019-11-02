#Discord dependencies
import discord
from discord.ext import commands

#Webpage automation
import pyautogui
import time
from selenium import webdriver

#Import Desmos functions
import desmos_interface
from desmos_interface import screenshot
from desmos_interface import setup
from desmos_interface import delete
from desmos_interface import show_graph


setup()

TOKEN = 'NTAxMjQ1OTkxNTM0NzIzMDcy.Dqk5NA.fykIbBCWjl60hqCRszKhOHVlUkA'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Dalton is online')
    print()

@client.event
async def on_message(message):
    channel = message.channel

    if message.content.startswith('#help'):
        await client.send_message(channel, 'I am Dalton, the Graphing Calculator' \
                                  ' assistant. You can summon me by typing "#graph" followed by a number and an equation.' \
                                  '\nEx: #graph1 (x^3-x)/(2x)' \
                                  '\n\nFunctions:\n' \
                                  '#graph - Displays current graph\n' \
                                  '#graph[n] (equation) - Graphs equation in graph n (where n is an integer 1-3)\n' \
                                  '#delete [n] - Deletes graph n (where n is an integer 1-3)\n' \
                                  '#delete all - Deletes all graphs')

    if message.content.startswith('#graph') and message.content != '#graph' and not message.author.bot:

        try:
            number = int(message.content[6])
            equation = message.content[8:]

            print("Graph:", number)
            print("Equation:", equation)
            print()

            if screenshot(number, equation) is True:
                await client.send_message(channel, f'Graph of {equation}')

                await client.send_message(channel, f'Loading graph...')
                await client.send_file(channel, 'graph.png')

            else:
                await client.send_message(channel, "I can only graph up to 3 graphs")

        except:
            await client.send_message(channel, "I'm afraid I can't do that.")  


    if message.content.startswith('#delete all') and not message.author.bot:
        for _ in range(10):
            boolean = delete(1)
            
        await client.send_message(channel, f"Deleted all graphs.")

    if message.content.startswith('#delete ') and not message.content.startswith('#delete all') and not message.author.bot:
        try:
            number = int(message.content[8])

            print("Deleting graph", number)
            print()

            if delete(number) is True:
                await client.send_message(channel, f"Deleted graph {number}.")
            else:
                await client.send_message(channel, f"I can only graph up to 3 graphs.")
            
        except:
            await client.send_message(channel, "I'm afraid I can't do that.")

    if message.content == '#graph' and not message.author.bot:
        show_graph()
        await client.send_message(channel, "Displaying current graph...")
        await client.send_file(channel, 'graph.png')
        
client.run(TOKEN)

#TODO:
    #Zoom in and out
    #Move graph
