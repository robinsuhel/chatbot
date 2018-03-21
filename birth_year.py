# Returns boolean, if the given agument is 
# a integer or not
def is_integer(number):
	try:
		int(number)
		return True
	except ValueError:
		return False

def tell_year(age):
	year =  str(2017-age)
	print("You born in the year " + year)

def run():
	age = input("What's you age: ")
	
	if is_integer(age):
		age = int(age)
		tell_year(age)
	else:
		print("You may pass only numbers for the age")

