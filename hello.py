# class Dog():
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f'{self.name} aww aww!')

# my_dog = Dog('renens', 'askal')
# my_dog.bark()

# class car():

#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
     
#     def start(self):
#         print(f'The {self.name} {self.model} is now starting')

#     def stop(self):
#         print(f'The {self.name} {self.model} is now stoping')
    
# my_car = car('supra', 'toyota')
# my_car.start()
# my_car.stop()


# class dog():
#     name = input('enter your name :')
#     breed = input('enter the breed:')
#     print(f'the dog name is {name} and the breed is {breed} ')

# print(dog)
class fruit():
    def __init__(self, name, cost ):
        self.name = name
        self.cost = cost
    
    def meth1():
        ...

    def meth2():
        ...

    def __str__(self):
        return f'{self.name} (${self.cost})'

Banana = fruit('banana', 10.0)
print(Banana)