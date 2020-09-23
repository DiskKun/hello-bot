import os
import random
import json
import discord

## BOT INIT
with open('statements.txt', 'r+') as file:
	statements = json.load(file)
with open('responses.txt', 'r+') as file:
	responses = json.load(file)
current_statement = statements[random.randint(0, len(statements)-1)]

TOKEN = '[BOT TOKEN]'

client = discord.Client()
channel = client.get_channel([CHANNEL ID])

@client.event
#async def on_join():
#	await channel.send(current_statement)
	
async def on_message(message):
	global current_statement
	if message.channel.id == [CHANNEL ID]:
		channel = message.channel
		if message.author == client.user:
			return
		## BOT CODE
		usrinput = message.content.lower()
		is_in_s = usrinput in statements
		if is_in_s == True:
			if usrinput in responses.keys():
				value = random.choice(responses[usrinput])
				await channel.send(value)
				current_statement = value
			else:
				await channel.send(usrinput)
				current_statement = usrinput
		else:
			statements.append(usrinput)
			responses.setdefault(current_statement, [])
			if usrinput in responses[current_statement]:
				pass
			else:
				responses[current_statement].append(usrinput)
			current_statement = statements[random.randint(0, len(statements)-1)]
			await channel.send(current_statement)
		jstatements = json.dumps(statements)
		jresponses = json.dumps(responses)
		with open('statements.txt', 'w+') as file:
			file.write(jstatements)
		with open('responses.txt', 'w+') as file:
			file.write(jresponses)
			
client.run(TOKEN)
