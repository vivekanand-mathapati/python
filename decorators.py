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