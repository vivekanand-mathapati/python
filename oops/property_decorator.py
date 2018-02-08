class Employee:
	'''this is a employee class'''
	
	raise_amount = 0.04

	def __init__(self,fname,lname,pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay

	def getFullname(self):
		return self.fname+' '+self.lname

	def apply_raise(self):	
		self.pay = self.pay + (self.pay * self.raise_amount)

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.fname,self.lname)

	@email.setter
	def email(self,name):
		self.fname,self.lname = name.split(' ')

	@email.deleter
	def email(self):
		print('name deleted')

emp_1 = Employee('vivek','math',80000)
emp_1.email = 'veerendr singh'
print(emp_1.email)
del emp_1.email
print(emp_1.email)
