import string

class Associator:
	def __init__(self, alphabet=string.ascii_letters+string.digits):
		self.alphabet = alphabet

	def encode(self, num):
		"""Encode a number in the given self.alphabet

		`num`: The number to encode
		`self.alphabet`: The self.alphabet to use for encoding
		"""
		if (num == 0):
			return self.alphabet[0]
		arr = []
		base = len(self.alphabet)
		while num:
			rem = num % base
			num = num // base
			arr.append(self.alphabet[rem])
		arr.reverse()
		return ''.join(arr)

	def decode(self, enc_string):
		"""Decode an encoded string into the number

		Arguments:
		- `string`: The encoded string
		- `self.alphabet`: The self.alphabet to use for encoding
		"""
		base = len(self.alphabet)
		strlen = len(enc_string)
		num = 0

		idx = 0
		for char in enc_string:
			power = (strlen - (idx + 1))
			num += self.alphabet.index(char) * (base ** power)
			idx += 1

		return num
