import random
import string
import math

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
NUMBERS = string.digits


def generate_username(length):
	word = ""
	for i in range(length):
		n = math.floor(random.random() * 3)

		if n == 0:
			word += random.choice(CONSONANTS)
		elif n == 1:
			word += random.choice(VOWELS)
		else:
			word += random.choice(NUMBERS)
	return word