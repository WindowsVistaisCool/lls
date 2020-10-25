import discord
from json import load as jload
from discord.ext import commands

client = commands.Bot(command-prefix='=')
client.remove_command('help')

@client.event
async def on_ready():
	print(f"Ready ({client.id}, {client.user})")
	await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='Zelo\'s snoring')

def get_token():
	with open('h.json', 'r') as v:
		x = jload(v)
	return x["TOKEN"]

client.run(get_token())
