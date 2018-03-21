# Returns boolean, if the given agument is 
# a integer or not
def is_integer(number):
	try:
		int(number)
		return True
	except ValueError:
		return False

def tell_status(age):
	if age > 17:
		print("Your are an adult!")
	elif age < 17 and age > 12:
		print("You are a teenager!")
	else:
		print("You are a child!")

def run():
	age = input("What's you age: ")

	if is_integer(age):
		age = int(age)
		tell_status(age)
	else:
		print("You may pass only numbers for the age")

