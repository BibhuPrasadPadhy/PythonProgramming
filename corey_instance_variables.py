# Python Object-Oriented Programming

# Without Init Method

# class Employee:
#     pass

#
# e1.first = 'Bibhu'
# e1.last = 'Padhy'
# e1.email = 'bpray@allstate.com'
# e1.pay = 50000
#
# e2.first = 'Test'
# e2.last = 'User'
# e2.email = 'test@allstate.com'
# e2.pay = 500000
#
# print(e1.email)
# print(e2.email)


# With Init Method
class Employee:

    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first+'_'+last+'@company.com'

    def full_name(self):
        return "{} {}".format(self.fname,self.lname)


#Instance Variables
e1 = Employee('Bibhu','Padhy',50000)
e2 = Employee('Test','User',60000)

print(e1.email,e2.email)

print(e1.full_name())                #passing object inherently
print(Employee.full_name(e1))        #Calling function using class.functionname, so we need to pass object explicitly



