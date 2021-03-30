#!/bin/python 

import discord
import sys
import os
import time
import asyncio

token = os.environ.get("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    originalStart = time.time()
    start = originalStart

    while True:
        await asyncio.sleep(1)
        start += 1
        
        if start - originalStart >= 18000:
            await client.logout()
            await client.close()
            sys.exit(1)
            # raise KeyboardInterrupt

@client.event
async def on_message(message):
    if message.content == 'Are you alive?':
        await message.channel.send('Yes, I am.')

    if message.content == 'Ping!':
        await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

client.run(token)
