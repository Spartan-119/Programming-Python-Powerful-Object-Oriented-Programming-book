class Person:
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
        
    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)
        
    def lastName(self):
       return self.name.split()[-1]
   
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
        return self.pay
        
# creating the main (driver) function
if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 150000, 'Software Engineer')
    abin = Person('Abin Varghese', 25, 500000, 'Data Scientist')
    
    people = [bob, abin]
    
    x = [(person.name, person.pay) for person in people]
    #print(x)
    print()
    
    y = [(rec.pay ** 2 if rec.name == 'Abin Varghese' else rec.pay) for rec in people] # SQL-ish kinda query
    print(y)
    
        