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

#neko commands 

@client.event
async def on_message(message):
    if message.author == client.user:
       return

    if message.content.startswith('E?neko'):
        await message.channel.send('Command disabled due to lack of cats')


# Listening Status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Daddy Ethical'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


keep_alive()
client.run(os.getenv("TOKEN"))