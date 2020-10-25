import discord
import functions
from time import sleep as rest
from json import load as jload
from json import dump as jdump
from discord.ext import commands

client = commands.Bot(command_prefix='=')
client.remove_command('help')
class config:
	name = 'Spooky Birdo'
	helpone = f'=help\n'

def wjson(file, key, val=None, read=False):
	if read is not False:
		with open(file, 'r') as v:
			x = jload(v)
		return x[key]
	else:
		with open(file, 'r') as v:
			x = jload(v)
		x[key] = val
		with open(file, 'w') as v:
			jdump(x, v, indent=4)

@client.event
async def on_ready():
	print(f"Ready")
	await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='Zelo\'s snoring'))

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		pass
	else:
		await ctx.send(error)

@client.command()
@commands.is_owner()
async def stop(ctx):
	await ctx.message.delete()
	await client.close()

@client.command()
@commands.is_owner()
async def invoke(ctx, erro, test):
	if erro == "CommandError":
		raise discord.ext.commands.CommandError(test)
	elif erro == "ArgumentParsingError":
		raise discord.ext.commands.ArgumentParsingError(test)
	elif erro == "BadArgument":
		raise discord.ext.commands.BadArgument(test)
	elif erro == "UserInputError":
		raise discord.ext.commands.UserInputError(test)

@client.command()
async def help(ctx):
	e = discord.Embed(title='Help page 1', color=discord.Color.blurple())
	e.set_footer(text=f'Bot developed by {config.name}')
	e.add_field(name='General Commands:', value=config.helpone)
	await ctx.send(embed=e)

@client.command()
async def invite(ctx, type=None):
	if type is None:
		await ctx.send("The syntax for this command is: `=invite (bot/server)'")
	elif type == "server":
		await ctx.send(await ctx.channel.create_invite())
	elif type == "bot":
		e = discord.Embed(title="Bot invite", description="[Click Here](https://discord.com/api/oauth2/authorize?client_id=722515081912647732&permissions=8&scope=bot)")
		await ctx.send(embed=e)

@client.command()
async def lls(ctx):
	await ctx.message.delete()
	async with ctx.channel.typing():
		await ctx.send("Well...")
		rest(1)
		await ctx.send("Currently my laser is broken :(")
		rest(1)
		await ctx.send("But it will come back sometime in the future and it will be better than the original :)")

@client.command()
@commands.is_owner()
async def purge(ctx, amount):
	await ctx.channel.purge(limit=(int(amount) + 1))

@client.command()
@commands.is_owner()
async def input(ctx, file, key, val, read=False):
	await ctx.message.delete()
	if read is not False:
		val = None
		await ctx.send(f"Here is the data for {key}: {wjson(file, key, read=True)}")
	else:
		wjson(file, key, val, read=False)
		await ctx.send(f"Wrote {key} ({val}) into {file}")

@client.command()
async def execute(ctx, fun=None, member=True):
	await ctx.message.delete()
	msg = await ctx.send('Executing Function...')
	id = ctx.author.id
	if member is False:
		if ctx.author.id == 392502213341216769:
			id = 0
		else:
			raise discord.ext.commands.CommandError("Missing Required Permissions!")
			return

	if id == 392502213341216769:
		if fun is None:
			await ctx.send("Please provide a function")
			return
		else:
			await ctx.send(functions.execute(fun))
	else:
		if fun == "functions.test()":
			await ctx.send(functions.execute(fun))
		elif fun == "functions.die()":
			await ctx.send(functions.execute(fun))
		elif fun == None or (fun == "0" and member == False):
			e = discord.Embed(title="User-allowed Functions:", color=discord.Color.blurple())
			e.add_field(name="functions.test()", value="Test the program!")
			e.add_field(name="functions.die()", value="Uh oh!")
			await ctx.send(embed=e)
		else:
			if fun == "0":
				pass
			else:
				await ctx.send("You do not have permission to execute this function!")

	await msg.edit(content='Executed Function')

def get_token():
	with open('h.json', 'r') as v:
		x = jload(v)
	return x["TOKEN"]

client.run(get_token())
