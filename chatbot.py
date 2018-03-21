import birth_year
import social_status

def chatbot():
	action = input("Hello, what can I do for you today?")
	
	if "birth" in action:
		birth_year.run()
	elif "status" in action:
		social_status.run()
	elif "social" in action:
		social_status.run()
	elif "social" in action and "birth" in action:
		social_status.run()
		birth_year.run()
	elif "status" in action and "birth" in action:	
		social_status.run()
		birth_year.run()

chatbot()