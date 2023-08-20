import string 
import random


def RandID(length):
	characters = string.ascii_letters + string.digits
	result = ''.join(random.choices(characters, k=length))
	return result