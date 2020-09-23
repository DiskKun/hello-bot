import random
import json
import time
import threading
import discord
import os
newresponses = {}
newstatements = ["hello"]
saidTime = False
saveInterval = 600 ##How long between saves, in seconds

with open('statements.txt', 'r+') as file:
    
       statements = json.load(file)
    
with open('responses.txt', 'r+') as file:
    
    responses = json.load(file)
current_statement = statements[random.randint(0, len(statements) - 1)]

client = discord.Client()
channel = client.get_channel([CHANNEL ID])

def getResponses():

    tempResponses = responses.copy()
    tempResponses.update(newresponses)
    
    return tempResponses

def getStatements():
    
    tempStatements = statements.copy()
    tempStatements.extend(newstatements)
    
    return tempStatements


def saveLoop():
    
    while True:

        time.sleep(saveInterval/4*3)

        await channel.send("SYSTEM: Saving all responses and statements in " +  str(saveInterval/60/4) + " minutes")

        time.sleep(saveInterval/4)

        jstatements = json.dumps(getStatements())
        jresponses = json.dumps(getResponses())

        with open('statements.txt', 'w+') as file:
            
            file.write(jstatements)
            
        with open('responses.txt', 'w+') as file:
            
            file.write(jresponses)
        
        statements.append(newstatements)
        responses.update(newresponses)
        newresponses = {}
        newstatements = ["hello"]
        
        await channel.send("Saved responses! You can no longer /remove any recent messages.")

@client.event

async def on_message(message):
    
    global current_statement = "hello"
    
    if message.channel.id == [CHANNEL ID]:

        channel = message.channel

        if message.author == client.user:
            return

        ##BOT CODE
        
        usrinput = message.content.lower()
        
        is_in_s = usrinput in statements
        if not is_in_s:

            is_in_s = usrinput in newstatements
        
        if is_in_s:
            
            if usrinput in responses.keys():
                
                value = random.choice(getResponses()[usrinput])
                await channel.send(value)
                
                current_statement = value
                
            else:
                
                await channel.send(usrinput)
                current_statement = usrinput
                
        elif usrinput == "/quit" or usrinput == "/exit":
            
            jstatements = json.dumps(getStatements())
            jresponses = json.dumps(getResponses())
            
            with open('statements.txt', 'w+') as file:
                
                file.write(jstatements)
                
            with open('responses.txt', 'w+') as file:
                
                file.write(jresponses)
                
            quit()
            
        elif usrinput.startswith("/remove "):

            textToRemove = usrinput.rsplit(" ", 1)
            textToRemove = textToRemove[1]
            
            if textToRemove in newstatements:

                while textToRemove in newstatements:
                    
                    newstatements.remove(textToRemove)
            
            for statement, response in newresponses.items():
                
                if response.count(textToRemove) > 0:
                    
                    newresponses[statement].pop(newresponses[statement].index(textToRemove))
            
        else:

            if not usrinput in newstatements:
            
                newstatements.append(usrinput)

            newresponses.setdefault(current_statement, [])
            
            if usrinput in newresponses[current_statement]:
                
                                pass
                            
            elif responses.get(current_statement) and usrinput in responses.get(current_statement):
                
                                pass
                            
            else:
                newresponses[current_statement].append(usrinput)
                
            current_statement = getStatements()[random.randint(0, len(getStatements())-1)]
            await channel.send(current_statement)

saveThread = threading.Thread(target=saveLoop)
saveThread.start()
client.run(TOKEN)
