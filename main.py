import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#hello world

@client.event
async def on_message(message):
    if message.author == client.user:
       return

    if message.content.startswith('E?hello'):
        await message.channel.send('Hello!')

#neko commands 

@client.event
async def on_message(message):
    if message.author == client.user:
       return

    if message.content.startswith('E?neko'):
        await message.channel.send('Command disabled due to lack of cats')

keep_alive()
client.run(os.getenv("TOKEN"))