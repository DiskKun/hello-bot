import random

statements = ["Hello"]
responses = {}

def startbot():
	while True:
		current_statement = statements[random.randint(0, len(statements)-1)]
		print("Bot: " + current_statement)
		usrinput = input("You: ")
		is_in_s = usrinput in statements
		if is_in_s == True:
			responses[current_statement] = usrinput
		elif is_in_s == False:
			statements.append(usrinput)
			responses[current_statement] = usrinput
def main():
	startbot()

main()
