from random import randrange

def constant_function():
	print('CONSTANT FUNCTION:')
	l = []
	l.append(1)
	print(len(l))   # 1

	l = list(range(1000))
	l.append(1)
	print(len(l))   # 1000

def logarithmic_function():
	print('LOGARITHMIC FUNCTION:')
	def binary_search(l, item):
		first = 0
		last = len(l) - 1
		found = False

		while first <= last and not found:
			midpoint = round( (first + last) / 2 )
			if l[midpoint] == item:
				found = True
			else:
				if item < l[midpoint]:
					last = midpoint-1
				else:
					first = midpoint+1
		return found

	input = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

	print(binary_search(input, 3))   # found: False
	print(binary_search(input, 13))  # fount: True

def square_root_function():
	print('SQUARE ROOT FUNCTION:')
	def is_prime_number(x):
		if x >= 2:
			for y in range(2, x):
				# if x divides with zero remainder (i.e. equal to bool False)
				if not (x % y):
					return False
				else:
					return False
		return True

	print(is_prime_number(23))
	print(is_prime_number(1376187))

def linear_function():
	print('LINEAR FUNCTION:')
	def search(x, input):
		for i in input:
			if i == x:
				print('found element: ', x)
				return

		print('element not found: ',x)

	search(5, range(10))
	search(5, range(1000))
	search(999, range(1000))
	search(99999, range(10000))

def linearithmic_function():
	print('LINEARITHMIC FUNCTION:')
	def quicksort(arr):
		if len(arr) < 2:
			return arr
		else:
			rand = randrange(0, len(arr))  # grab a random index
			pivot = arr.pop(rand)
			less = [i for i in arr if i <= pivot]
			greater = [i for i in arr if i > pivot]
			return quicksort(less) + [pivot] + quicksort(greater)


	input = [10, 5, 2, 3, 7, 0, 9, 12]
	print("sorted:  ", quicksort(input))

def quadratic_function():
	print('QUADRATIC FUNCTION:')
	def power(input):
		p = 0
		for i in range(input):
			for j in range(input):
				p += input
		return p

	print(power(3))
	print(power(4))

def exponential_function():
	print('EXPONENTIAL FUNCTION:')
	def fibonacci(num):
		if (num <= 1):
			return num
		return fibonacci(num - 2) + fibonacci(num - 1)
	
	print(fibonacci(10))
	breakout()
	print(fibonacci(20))

def factorial_function():
	print('FACTORIAL FUNCTION:')
	def factorial(n):
		if n > 1:
			return n * factorial(n-1)
		else:
			return n
	
	print(factorial(3))
	print(factorial(4))
	print(factorial(5))

if __name__ == '__main__':
	constant_function()
	logarithmic_function()
	square_root_function()
	linear_function()
	linearithmic_function()
	quadratic_function()
	exponential_function()
	factorial_function()