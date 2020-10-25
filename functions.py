import subprocess
from time import sleep as rest
import discord

def test():
	print("```yaml\nTesting\nTesting\n1 2 3```")

def die():
	print("no u")


def execute(com):
	ste = subprocess.run(['python3', '-c', f'import functions; {com}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	st = ste.stdout.decode('utf-8')
	ster = ste.stderr.decode('utf-8')
	if ster is '':
		ster = 'No Errors'
	rest(2)
	return f'`{ster}`\n```fix\nOutput:```\n{st}'
