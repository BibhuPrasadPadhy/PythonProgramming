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


#Instance Variables
e1 = Employee('Bibhu','Padhy',50000)
e2 = Employee('Test','User',60000)


print(e1.pay)
e1.apply_raise()
print(e1.pay)


#We can access class variable by class name or instance variable
print(Employee.raise_multiplier)
print(e1.raise_multiplier)
print(e2.raise_multiplier)


#Class variable is always there in class namespace but not in object namespace
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)


#Here class variable is accessable to class & object and value is same 1.05
Employee.raise_multiplier = 1.05
print(Employee.raise_multiplier)
print(e1.raise_multiplier)
print(e2.raise_multiplier)


# Here raise_multiplier would be created as a instance variable for e1 object
e1.raise_multiplier = 1.06

print(e1.__dict__)

print(Employee.raise_multiplier)
print(e1.raise_multiplier)
print(e2.raise_multiplier)

print(Employee.num_of_emps)