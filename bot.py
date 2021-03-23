#!/bin/python 

import discord
import sys

token = sys.argv[1]
client = discord.Client()

@client.event
async def on_message(message):
    if message.content == 'Are you alive?':
        await message.channel.send('Yes, I am.')

    if message.content == 'Ping!':
        await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

client.run(token)
