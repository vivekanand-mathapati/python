class Employee:
    raise_pay = 1.04
    inst_count = 0
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.inst_count +=1

    @classmethod
    def set_raise_amount(cls,amt):
        cls.raise_pay = amt
    
    @staticmethod 
    def display():
        print('hello')

    def raise_amount(self):
        self.pay = int(self.pay * self.raise_pay)

class Developer(Employee):
    pass

emp1 = Developer('vivek','mathapati',5000000)
emp2 = Developer('veer','math',5000699)


print(isinstance(emp1,Employee))
print(issubclass(Employee,Developer))

print(str(emp1))