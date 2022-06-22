from Person import Person

class Manager(Person):
    
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job = 'Manager')
    
    # overriding the giveRaise method
    def giveRaise(self, percent, bonus = 0.1):
        self.pay *= (1.0 + percent + bonus)
        
# creating the driver class
if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age = 50, pay = 50000)
    
    print(tom.lastName())
    print(tom.giveRaise(.20))
    print(tom.pay)