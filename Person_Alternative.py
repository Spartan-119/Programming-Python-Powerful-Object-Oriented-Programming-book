class Person:
    # creating the constructor
    def __init__(self, name, age, pay, job):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    
    # creating the __str__ method
    def __str__(self):
        return '<%s => %s: %s, %s>' % (self.__class__.__name__, self.name, self.age, self.pay)
    
    # method to retrieve the last name
    def lastName(self):
        return self.name.split()[-1]
    
    # method to give a raise of some percentage
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
        
# creating a child class
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job = 'Manager')
    
    # overloading the giveRaise method
    def giveRaise(self, percent, bonus = 0.5):
        Person.giveRaise(self, percent + bonus)
        
# creating the driver class
if __name__ == '__main__':
    abin = Person('Abin Varghese', 25, 150000, 'Data Scientist')
    alex = Person('Alexis Xander', 29, 200000, 'Blockchain Developer')
    alan = Manager('Alan Turing', 42, 500000)
    
    db = [abin, alex, alan]
    
    for obj in db:
        print(obj.lastName())
        print(obj.__str__())
        obj.giveRaise(0.1)
        print(obj.pay, '\n')