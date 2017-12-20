class Employee:
    def __init__(self,fname,lname,email,pay):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pay = pay
    
    def __repr__(self):
        return 'Employee("{}","{}","{}","{}")'.format('fname','lname','email','pay')

    def __str__(self):
        return 'Employee("{}","{}","{}",{})'.format(self.fname,self.lname,self.email,self.pay)
    
    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fname)
    
emp1 = Employee('vivek','mathapati','vivek@gmail.com',50000)
emp2 = Employee('veer','math','math@gmail.com',40000)
print(emp1)
print(emp1.__repr__())
print(emp1 + emp2)
# OR
print(emp1.__add__(emp2))
print(len(emp1))
print(emp1.__len__())
print('vivek'.__len__())