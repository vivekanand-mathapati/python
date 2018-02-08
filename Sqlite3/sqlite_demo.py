import sqlite3 
from employee import Employee

#connect('filename') or connect(':memory:') for in memory db #cretes fresh db in RAM every time u run code 
# sqlite3.connect('employee.db') #connects to employee.db file if exists else creates one
# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

#create corsore to execute sql queries
c = conn.cursor()

#create employee table
c.execute("""CREATE TABLE employee(
            fname text,
            last text,
            pay integer)"""
         )

#insert 
# c.execute("INSERT INTO employee VALUES('vivek','math', 99888)")
# c.execute("INSERT INTO employee VALUES('veer','math', 99888)")
# c.execute("INSERT INTO employee VALUES('shanker','math', 99888)")
# c.execute("INSERT INTO employee VALUES('kanki','math', 99888)")
# c.execute("INSERT INTO employee VALUES('kumba','math', 99888)")

emp_1 = Employee('keevi','mathapati',564564)
emp_2 = Employee('chiku','math',5644)
emp_3 = Employee('apple','takker',56774564)

# c.execute("INSERT INTO employee VALUES(?, ?, ?)", (emp_1.fname, emp_1.last, emp_1.pay))
# conn.commit()
# #or u can also use this method
# c.execute("INSERT INTO employee VALUES(:fname, :last, :pay)", {'fname': emp_2.fname, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()
# #but dont use this one - sql injection volnarability 
# c.execute("INSERT INTO employee VALUES('{}', '{}', '{}')".format(emp_3.fname, emp_3.last, emp_3.pay))
# conn.commit()

def insert_employee(emp_obj):
    with conn:
        c.execute("INSERT INTO employee VALUES('{}', '{}', '{}')".format(emp_obj.fname, emp_obj.last, emp_obj.pay))

insert_employee(emp_1)

def get_employee_by_name(value):
    c.execute("SELECT * FROM employee where last=:last", {'last': value})
    print(c.fetchall())

def update_employee():
    pass

def delete_employee():
    pass

get_employee_by_name('mathapati')

#fetch data now
# c.execute("SELECT * FROM employee")
# print(c.fetchone()) #tuple
# print(c.fetchmay(5)) #list containing tuples

# c.execute("SELECT * FROM employee where last=?", ('math',))
# print(c.fetchall()) #list containing tuples

# c.execute("SELECT * FROM employee where last=:last", {'last': 'mathapati'})
# print(c.fetchall()) #list containing tuples

conn.close()
