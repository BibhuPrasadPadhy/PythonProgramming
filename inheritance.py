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


class Developer(Employee):
    raise_multiplier = 1.08

    def __init__(self, first, last, pay,prog_lang):

        super().__init__(first,last,pay)
#       Employee.__init__(self,first,last,pay)           can be also used, to be used in multiple inheritance
        self.prog_lang = prog_lang



class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):

        super().__init__(first,last,pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees



    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.full_name())



d1 = Developer('Bibhu','Padhy',50000,'Java')
d2 = Developer('Test','User',60000,'Python')
#
#
# print(d1.pay)
# print(d1.prog_lang)
# print(d1.email)

manager1 = Manager('Bibhu','Padhy',50000,[d1])
print(manager1.email)

print(manager1.print_emp())
manager1.add_employee(d2)
print(manager1.print_emp())

manager1.rem_employee(d1)
print(manager1.print_emp())


print(isinstance(manager1,Manager))
print(issubclass(Manager,Employee))