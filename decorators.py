<<<<<<< HEAD
from functools import wraps

def new_decorator(func):
	
	@wraps(func)
	def wrap_func():
		print('i am in new_decorator')
		func()
		print('i am in new_decorator')

	return wrap_func

@new_decorator
def func_req_func():
	print('i am func_req_func')

# func_req_func = new_decorator(func_req_func)
func_req_func()
# print(help(func_req_func))
=======
class Employee:
    def __init__(self,fname,lname,email,pay):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    
    @property
    def emailadd(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter
        print('Employee name deleted!')
        self.fname = None
        self.lname = None

emp1 = Employee('vivek','mathapati','vivek@gmail.com',50000)
print(emp1.emailadd)

emp1.fullname = 'vivek math'
print(fullname)

del emp1.fullname
>>>>>>> b8d2e628c116f209ede07f95900115aa99583c4e
