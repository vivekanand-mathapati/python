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

class Developer(Employee):
	'''This is a developers class'''

	def __init__(self,fname,lname,email,pay,prog_lang):
		super().__init__(fname,lname,email,pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self,fname,lname,email,pay,employees = None):
		super().__init__(fname,lname,email,pay)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self,emp):
		if emp not in employees:
			self.employees.append(emp)
		else:
			print('employee exist')

	def remove_employee(self,emp):
		if emp in employees:
			self.employees.remove(emp);
		else:
			print('employee not exist')

	def print_employees(self):
		for emp in self.employees:
			print(emp.getFullname())

dev_1 = Developer('vivekanand','mathapati','vivekanand.d.mathapati@gmail.com',60000,'python')
dev_2 = Developer('vivek','math','vivek@gmail.com',70000,'php')
mgr_1 = Manager('preethan','panditaral','preethanpa@gmail.com',900000,[dev_1,dev_2])
mgr_1.print_employees()
print(issubclass(Manager,Employee))
print(isinstance(dev_1,Developer))







