import random

def power_of(arg):
#def power_of(exponent):
	def decorator(fnc):
		def inner():
			return fnc() ** exponent
		
		return inner
	# return decorator
	
	if callable(arg):
		exponent = 2
		return decorator(arg)
	else:
		exponent = arg
		return decorator

l = [1, 3, 5, 7, 9]

@power_of
def random_odd_digit():
	return random.choice(l)

@power_of(4)
def random_odd_digit_any_exponent():
	return random.choice(l)

if __name__ == '__main__':
	print(random_odd_digit())
	print(random_odd_digit_any_exponent())