#employee class defined here
class Employee:
    increment_pay = 0.04
    def __init__(self,fname,last,pay):
        self.fname = fname
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.last)

    @email.setter
    def email(self,name):
        self.fname, self.last = name.split(' ')

# emp_1 = Employee('vivek','mathapati',564564)
# print(emp_1.email)
# emp_1.email = 'vivekanand mathapati'
# print(emp_1.email)