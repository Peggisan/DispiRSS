# Made using Python 3.6.8

import discord
import os
from dotenv import load_dotenv
load_dotenv()


client = discord.Client()


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('!'):
		msg = 'yeet {0.author.mention}'.format(message)
		await client.send_message(message.channel,msg)




TOKEN = os.getenv("TOKEN")
print(TOKEN)
client.run(TOKEN)

