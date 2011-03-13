class palindrom(object):

	def __init__(self, string):
		self.string = string

	def reverse(self):
		l1 = list(self.string)
		l1.reverse()
		return ''.join(l1)
	
	def isPalindrom(self):
		return self.string == self.reverse()


p1 = palindrom('aba')
print p1.reverse()
print p1.isPalindrom()

p1 = palindrom('abba')
print p1.reverse()
print p1.isPalindrom()

p1 = palindrom('abca')
print p1.reverse()
print p1.isPalindrom()

