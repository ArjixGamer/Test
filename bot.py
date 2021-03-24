#!/bin/python 

import discord
import sys
import time
import asyncio

token = sys.argv[1]
client = discord.Client()

@client.event
async def on_ready():
    originalStart = time.time()
    start = originalStart

    while True:
        await asyncio.sleep(1)
        start += 1
        
        if start - originalStart >= 18000:
            # It's literally this bad, client.close and client.logout might as well not exist, since they do jack
            raise KeyboardInterrupt

@client.event
async def on_message(message):
    if message.content == 'Are you alive?':
        await message.channel.send('Yes, I am.')

    if message.content == 'Ping!':
        await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

client.run(token)
