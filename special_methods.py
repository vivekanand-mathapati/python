class Employee:
	'''this is a employee class'''
	
	raise_amount = 0.04

	def __init__(self,fname,lname,email,pay):
		self.fname = fname
		self.lname = lname
		self.email = email
		self.pay = pay

	def getFullname(self):
		return self.fname+' '+self.lname

	def apply_raise(self):	
		self.pay = self.pay + (self.pay * self.raise_amount)

	def __repr__(self):
		return 'Employee("{}","{}","{}","{}")'.format(self.fname,self.lname,self.email,self.pay)
	
	def __str__(self):
		return self.getFullname()

	def __add__(self,other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.getFullname())

emp1 = Employee('vivek','mathapati','vivek@gmail.com',10000)
emp2 = Employee('veer','math','veer@gmail.com',50000)	
print(repr(emp1))
print(str(emp1))
print(len(emp1))
print(emp1+emp2)