#!/bin/python 

import discord
import sys

token = sys.argv[1]
client = discord.Client()

@client.event
async def on_message(message):
    if message.content == 'Are you alive?':
        await message.channel.send('Yes, I am.')

client.run(token)
