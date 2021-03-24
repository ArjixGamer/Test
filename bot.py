#!/bin/python 

import discord
import sys
import time

token = sys.argv[1]
client = discord.Client()

@client.event
async def on_ready():
    originalStart = time.time()
    start = originalStart

    while True:
        time.sleep(1)
        start += 1
        
        if start - originalStart >= 18000:
            sys.exit(0)

@client.event
async def on_message(message):
    print(message)
    if message.content == 'Are you alive?':
        await message.channel.send('Yes, I am.')

    if message.content == 'Ping!':
        await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

client.run(token)
