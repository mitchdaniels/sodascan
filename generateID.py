import random
import string

def generate_id(length):
	return "".join( [random.choice(string.letters[:26]) for i in xrange(length)] )