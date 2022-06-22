from Person import Person
from Manager import Manager

bob = Person('Bob Smith', 42, 10000, 'Software Engineer')
abin = Person('Abin Varghese', 25, 20000, 'Data Scientist')
tom = Manager(name = 'Tom Doe', age = 50, pay = 30000)

print(tom)

db = [bob, abin, tom]

for obj in db:
    obj.giveRaise(0.10)
    
for obj in db:
    print(obj.job, "=>", obj.pay)