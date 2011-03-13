class BankAccount(object):
	interest_rate = 0.3

	def __init__(self, name, number, balance):
		self.name = name
		self.number = number
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print 'Your deposit updated as %d' %(self.balance)
	
	def withdraw(self, amount):
		if amount > self.balance:
			print 'Overdraft!!!'
			return
		self.balance -= amount
		print 'Your deposit updated as %d' %(self.balance)
	
	def add_interest(self, time):
		self.balance += self.balance * self.interest_rate
		print 'Your deposit updated as %d' %(self.balance)
		
class StudentAccount(BankAccount):

	def withdraw(self, amount):
                if self.balance - amount < 1000:
                        print 'Overdraft!!!'
                        return
                self.balance -= amount
                print 'Your deposit updated as %d' %(self.balance)


b1 = BankAccount('s', 12, 1200)
b1.deposit(500)	
b1.withdraw(3000)
b1.add_interest(2)
s1 = StudentAccount('s', 12, 5000)
s1.withdraw(1000)
s1.withdraw(1000)
s1.withdraw(1000)
