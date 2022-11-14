class Employee:

    #Class variables here

    num_of_emps = 0
    raise_multiplier = 1.04

    def __init__(self,first,last,pay):

        #Increment num of emps
        Employee.num_of_emps += 1

        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first+'_'+last+'@company.com'

    def full_name(self):
        return "{} {}".format(self.fname,self.lname)


    def apply_raise(self):
        #raise_multiplier is given self coz we can give different raise_multiplier for different emp
        self.pay = int(self.pay * self.raise_multiplier)

    def __repr__(self):
        return "Employee Class : {} {}".format(self.fname,self.lname)

    def __str__(self):
        return "{} {}".format(self.email, self.full_name())

    def __add__(self, other):
        return (self.pay + other.pay)

    def __sub__(self, other):
        return abs(self.pay - other.pay)

    def __len__(self):
        return len(self.full_name())



#Instance Variables
e1 = Employee('Bibhu','Padhy',50000)
e2 = Employee('Test','User',60000)

print(e1.__repr__())
print(e1.__str__())
print(e1+e2)
print(e1-e2)
print(len(e1))