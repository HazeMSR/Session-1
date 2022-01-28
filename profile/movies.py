import cProfile, pstats, io

def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

def read_movies(src):

	with open(src) as fd:
		return fd.read().splitlines()

def is_duplicate(movie, movies):
	
	for m in movies:
		if movie.lower() == m.lower():
			return True
	return False

def find_duplicate_movies(src='movies.txt'):

	movies = read_movies(src)
	duplicates = []
	while movies:
		movie = movies.pop()
		if is_duplicate(movie, movies):
			duplicates.append(movie)
	return duplicates

if __name__ == '__main__':
	find_duplicate_movies()
