def another_function():
	print('another function')

def turn_into_another_function(fnc):
	return another_function

@turn_into_another_function
def a_function():
	print('a function')

if __name__ == '__main__':
	#a_function = turn_into_another_function(another_function)
	a_function()