import string
import os, base64
from itertools import starmap, cycle

alphabet = string.ascii_lowercase
listaposibles = []
nums = ['1','2','3','4','5', 'D']

class polybius:
	def __init__(self):
		self.polybius = {}
		char_to_skip = str(input('[Polybius] Char to skip (brute -> Bruteforce): '))

		if char_to_skip != 'brute':
			try:
				self.chars = alphabet.replace(char_to_skip, '')
			except:
				self.chars = alphabet.replace('j', '')

			print('[Polybius] Result: ' + self.decode())

		else:
			for char in alphabet:
				self.chars = alphabet.replace(char, '')
				print(f'[Polybius] Result [{char}]: ' + self.decode())

	def decode(self):
		decoded = ''
		num0 = 1
		num1 = 1
		for char in self.chars:
			if num1 == 6:
				num0 += 1
				num1 = 1
			
			self.polybius[int(str(num0) + str(num1))] = char
			num1 += 1

		for value in values.split():
			decoded += self.polybius[int(value)]

		return decoded

class caesar: ## FALTA AÑADIR QUE NO COJA LOS SIMBOLOS

	def __init__(self):
		self.shift = str(input('[Caesar] Shift (brute -> Bruteforce): '))
		if self.shift != 'brute':
			print('[Caesar] Result: ' + self.decode())
		else:
			for num in range(len(alphabet)):
				self.shift = num + 1
				print(f'[Caesar] Result [{self.shift}]: ' + self.decode())


	def decode(self):
		decoded = ''
		self.shift = int(self.shift)
		for value in values:
			charset = alphabet[alphabet.find(value):] + alphabet[:alphabet.find(value)]
			decoded += charset[len(alphabet) - self.shift]
		
		return decoded

class vigenre:

	def __init__(self):
		self.key = str(input('[Vigenre] Key: '))
		self.values = ''.join([i for i in values.strip() if i.isalpha()])
		print('[Vigenre] Result: ' + self.decode())

	def decode(self):
	    def dec(c, k): 
	        return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))
	 
	    return ''.join(starmap(dec, zip(self.values, cycle(self.key))))


def ascii():
	decoded = ''.join([chr(int(i)) for i in values.split()])
	print('[Ascii] Result: ' + decoded)

def hex():
	decoded = b''.fromhex(values.strip())
	print('[Hex] Result: ' + decoded.decode('utf'))

def main():
	global values
	os.system('cls')
	print('#\tAUTOMATIC DECODER BY Astr0\t#\n\n\t\t[1] Caesar\n\t\t[2] Polybius\n\t\t[3] Vigenre\n\t\t[4] Ascii\n\t\t[5] Hex\n\n\t\t[D] Detect\n')
	inp = str(input('--> '))
	if inp in nums:
		values = str(input('[INPUT] Code: '))
		if inp == nums[0]:
			caesar()
		elif inp == nums[1]:
			polybius()
		elif inp == nums[2]:
			vigenre()
		elif inp == nums[3]:
			ascii()
		elif inp == nums[4]:
			hex()
		elif inp == 'D':
			detect()
		else:
			print('[LOG] Wrong number')



def detect():
	for value in values.split():
		try:
			if value.isdigit() == True and len(value) == 2 and int(value) < 55:
				if 'polybius' not in listaposibles:
					listaposibles.append('polybius')

			if value.isdigit() == True and len(value) == 2 or len(value) == 3 and int(value) < 255 and int(value) > 30:
				if 'ascii' not in listaposibles:
					listaposibles.append('ascii')
				
			if value[1] in alphabet[:6] and value[0].isdigit():
				if 'hex' not in listaposibles:
					listaposibles.append('hex')

		except:
			pass


	#COMPRUEBA TODOS LOS POSIBLES
	for possible in listaposibles:
		try:
			exec(possible + '()')
			print(f'[LOG] This one -> ' + possible[0].upper() + possible[1:])
		except:
			print(f'[{possible[0].upper() + possible[1:]}] Result: wrong type')
			pass

if __name__ == '__main__':
	main()