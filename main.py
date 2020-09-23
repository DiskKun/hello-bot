import random
import json
newresponses = {}
newstatements = ["hello"]

input1 = input("Load file? (Y/n) ")
if input1 == "y" or input1 == "Y" or input1 == "":
    
    with open('statements.txt', 'r+') as file:
        
        statements = json.load(file)
        
    with open('responses.txt', 'r+') as file:
        
        responses = json.load(file)
        
else:
    
    with open('statements.txt', 'w+') as file:
        
        statements = ["hello"]
        file.write(json.dumps(statements))
        
    with open('responses.txt', 'w+') as file:
        
        responses = {}
        file.write(json.dumps(responses))

def getResponses():

    tempResponses = responses.copy()
    tempResponses.extend(newresponses)
    
    return tempResponses

def getStatements():
    
    tempStatements = statements.copy()
    tempStatements.extend(newstatements)
    
    return tempStatements

        
def main():
    
    usrinput = 0
    current_statement = "hello"
    
    while True:
        
        usrinput = input("You: ")
        usrinput.lower()
        
        is_in_s = usrinput in statements
        
        if is_in_s:
            
            if usrinput in responses.keys():
                
                value = random.choice(getResponses()[usrinput])
                print("Bot: " + value)
                
                current_statement = value
                
            else:
                
                print("Bot: " + usrinput)
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
            
            newstatements.append(usrinput)
            newresponses.setdefault(current_statement, [])
            
            if usrinput in newresponses[current_statement]:
                
                                pass
                            
            elif responses.get(current_statement) and usrinput in responses.get(current_statement):
                
                                pass
                            
            else:
                newresponses[current_statement].append(usrinput)
                
            current_statement = getStatements()[random.randint(0, len(getStatements())-1)]
            print("Bot: " + current_statement)

main()
