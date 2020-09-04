import random

statements = ["Hello"]
responses = {}

def startbot():
	usrinput = 0
	while True:
		current_statement = statements[random.randint(0, len(statements)-1)]
		print("Bot: " + current_statement)
		while True:	
			usrinput = input("You: ")
			is_in_s = usrinput in statements
			if is_in_s == True:
				if usrinput in responses.keys():
					print("Bot: " + responses[usrinput])
					current_statement = responses[usrinput]
				else:
					print("Bot: " + usrinput)
					current_statement = usrinput
			else:
				statements.append(usrinput)
				responses[current_statement] = usrinput
				break
def main():
	startbot()

main()
