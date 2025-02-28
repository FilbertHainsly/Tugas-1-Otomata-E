class ArithmeticChecker:
	'''
	Arithmethic sentence checker
	'''

	base = '0123456789'
	operators = '+-*/'
	
	def __init__(self) -> None:
		self.sentence = ''
		self.pos = -1
		self.curr = ''

	def check(self, sentence: str) -> bool:
		'''
		Validates arithmetic sentence / expression.

		Args:
			sentence (str): The sentence string to validate.

		Returns:
			bool: Validation result.
		'''
		self.sentence = sentence
		self.pos = -1
		valid = True
		self.next()
		while valid and self.curr != '':
			valid = self.expression()
		return valid

	def next(self) -> str:
		'''
		Gets the next non-whitespace character from sentence if available.

		Returns:
			bool: Validation result.
		'''
		if self.pos + 1 == len(self.sentence):
			self.curr = ''
		else:
			self.pos += 1
			self.curr = self.sentence[self.pos]
			while self.pos + 1 < len(self.sentence) and self.curr == ' ':
				self.pos += 1
				self.curr = self.sentence[self.pos]
		return self.curr

	def number(self) -> bool:
		'''
		Validate if number complies with generated rules (Rule 1 and Rule 2).

		Returns:
			bool: Validation result.
		'''
		if self.curr == '(':
			self.next()
			if not self.expression():
				return False
			if self.curr != ')':
				return False
			self.next()
			return True
		if not self.curr:
			return False
		if self.curr not in self.base:
			return False
		while self.curr and self.curr in self.base:
			self.next()
		return True

	def unary(self) -> bool:
		'''
		Validate unary operations (Rule 2).

		Returns:
			bool: Validation result.
		'''
		if self.curr == '-':
			self.next()
		return self.number()

	def binary(self) -> bool:
		'''
		Validate binary operations (Rule 3).

		Returns:
			bool: Validation result.
		'''
		left = self.unary()
		while left and self.curr:
			if self.curr == '(':
				left = self.number()
			elif self.curr in self.operators:
				self.next()
				left = self.unary()
			else:
				break
		return left

	def expression(self) -> bool:
		'''
		Validate expression (Rule 1, Rule 2, Rule 3).
		
		Returns:
			bool: Validation result.
		'''
		return self.binary()


if __name__ == '__main__':
	checker = ArithmeticChecker()
	sentence = str(input('Sentence: '))
	print('Valid' if checker.check(sentence) else 'Tidak Valid')
