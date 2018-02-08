class Employee:
	'''this is a employee class'''
	
	raise_amount = 0.04

	def __init__(self,fname,lname,email,pay):
		self.fname = fname
		self.lname = lname
		self.email = email
		self.pay = pay

	def show_employee(self):
		print('fname:{}\n lname:{}\n email:{}\n pay:{}\n'.format(self.fname,self.lname,self.email,self.pay))

	def getFullname(self):
		return self.fname+' '+self.lname

	def apply_raise(self):	
		self.pay = self.pay + (self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

Employee.set_raise_amt(10)
emp1 = Employee('vivek','mathapati','vivek@gmail.com',5000)
emp1.apply_raise()
emp2 = Employee('veer','math','veer@gmail.com',4000)
emp1.show_employee()
