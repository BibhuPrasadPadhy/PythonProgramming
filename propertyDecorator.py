class Employee:

    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
        self.pay = pay

    @property
    def email(self):
        return "{}_{}@company.com".format(self.fname,self.lname)

    @property
    def full_name(self):
        return "{} {}".format(self.fname,self.lname)

    @full_name.setter
    def full_name(self,name):
        first,last = name.split(' ')
        self.fname = first
        self.lname = last

    @full_name.deleter
    def full_name(self):
        print('Deleted Name!')
        self.fname = None
        self.lname = None



#Instance Variables
e1 = Employee('Bibhu','Padhy',50000)
e2 = Employee('Test','User',60000)

print(e1.email,e2.email)
print(e1.email)
print(e1.full_name)

e1.full_name = 'Unmesha Prajnashree'
print(e1.email,e2.email)
print(e1.email)
print(e1.full_name)


del e1.full_name