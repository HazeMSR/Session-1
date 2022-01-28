def turn_into_another_function(fnc):
	return another_function

#@turn_into_another_function
def a_function():
	print('a function')

def another_function():
	print('another function')

if __name__ == '__main__':
	a_function = turn_into_another_function(a_function)
	a_function()
