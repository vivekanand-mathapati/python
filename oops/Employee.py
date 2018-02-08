'''This module contains classes related to Employee'''

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

emp1 = Employee('vivek','mathapati','vivek@gmail.com',879878)
emp2 = Employee('veer','math','veer@gmail.com',777897)
# print(Employee.getFullname(emp1
# print(Employee.getFullname(emp1))

Employee.raise_amount = 0.10
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp1.__dict__)
print(Employee.__dict__)