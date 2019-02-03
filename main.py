# Made using Python 3.7.2
import discord
import asyncio

TOKEN = "NTQxNDg0MzY2OTY3MzQxMDc3.DzgNng.rh9_dJ1qnYlicLdwgSjcRiGGPx4"

client = discord.Client()


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('!'):
		msg = 'yeet {0.author.mention}'.format(message)
		await client.send_message(message.channel,msg)



client.run(TOKEN)

