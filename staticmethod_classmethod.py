class Employee:
    # Class variables here

    num_of_emps = 0
    raise_multiplier = 1.04

    def __init__(self, first, last, pay):
        # Increment num of emps
        Employee.num_of_emps += 1

        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'

    def full_name(self):
        return "{} {}".format(self.fname, self.lname)

    def apply_raise(self):
        # raise_multiplier is given self coz we can give different raise_multiplier for different emp
        self.pay = int(self.pay * self.raise_multiplier)

    @classmethod
    def set_raise_multiplier(cls, multiplier):
        cls.raise_multiplier = multiplier

    @classmethod
    def from_string(cls,emp_str):                 #class name as alternative constructor
        fname,lname,pay = emp_str.split('-')
        return cls(fname,lname,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



#Instance Variables
e1 = Employee('Bibhu','Padhy',50000)
e2 = Employee('Test','User',60000)

Employee.raise_multiplier = 1.05
print(Employee.raise_multiplier)
print(e1.raise_multiplier)
print(e2.raise_multiplier)

Employee.set_raise_multiplier(1.07)
print(Employee.raise_multiplier)
print(e1.raise_multiplier)
print(e2.raise_multiplier)

e1.set_raise_multiplier(1.09)
print(Employee.raise_multiplier)
print(e1.raise_multiplier)
print(e2.raise_multiplier)


# Alternative Constructor
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-60000'
emp_str_3 = 'Jane-Doe-50000'

fname,lname,sal = emp_str_1.split('-')
print(fname,lname,sal)

e3 = Employee.from_string(emp_str_1)
print(e3.fname,e3.lname,e3.pay,e3.email)


import datetime

my_date = datetime.date(2000,7,10)

print(Employee.is_workday(my_date))