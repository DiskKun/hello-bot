import random
import json

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
		
def main():
	usrinput = 0
	while True:
		current_statement = statements[random.randint(0, len(statements)-1)]
		print("Bot: " + current_statement)
		while True:	
			usrinput = input("You: ")
			usrinput.lower()
			is_in_s = usrinput in statements
			if is_in_s == True:
				if usrinput in responses.keys():
					print("DEBUG: recognized")
					value = random.choice(responses[usrinput])
					print("Bot: " + value)
					current_statement = value
				else:
					print("Bot: " + usrinput)
					print("DEBUG: unrecognized")
					current_statement = usrinput
			elif usrinput == "/quit" or usrinput == "/exit":
				jstatements = json.dumps(statements)
				jresponses = json.dumps(responses)
				with open('statements.txt', 'w+') as file:
					file.write(jstatements)
				with open('responses.txt', 'w+') as file:
					file.write(jresponses)
				quit()
			else:
				statements.append(usrinput)
				responses.setdefault(current_statement, [])
				if usrinput in responses[current_statement]:
					pass
				else:
					responses[current_statement].append(usrinput)
				break

main()
