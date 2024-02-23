from car import Car

# Object Oriented Programming (OOP) 🐍
# car1 = Car("Chevy", "Corvette", 2021, "blue")
# car2 = Car("Ford", "Mustang", 2022, "black")

# print(car1.make)
# print(car1.model)
# print(car1.year)
# print(car1.color)

# car1.drive()
# car2.stop()

# CLASS VARIABLES 🚗
# car1 = Car("Chevy", "Corvette", 2021, "blue")
# car2 = Car("Ford", "Mustang", 2022, "black")

# Car.wheels = 2 # global change

# car1.wheels = 2
# print(car1.wheels)
# print(car2.wheels)

# INHERITANCE 👪
# class Animal:
#     alive = True

#     def eat(self):
#         print("This animal is eating")
    
#     def sleep(self):
#         print("This animal is sleeping")

# class Rabbit(Animal):
#     def run(self):
#         print('This rabbit is running')

# class Fish(Animal):
#     def swim(self):
#         print('This fish is swimming')

# class Hawk(Animal):
#     def fly(self):
#         print('This hawk is flying')


# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# rabbit.run()
# rabbit.eat()

# fish.swim()
# fish.eat()

# hawk.fly()
# hawk.eat()

# MULTILEVEL INHERITANCE 👴 = when a derived (child) class inherits anthor derived (child)  class
# class Organism:
#     alive = True

# class Animal(Organism):
#     def eat(self):
#         print("This animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking")

# dog = Dog()
# dog.eat()
# dog.bark()

# MULTIPLE INHERITANCE 👨‍👩‍👧‍👦 = when a child class is derived from more then one parent class
# class Prey:
#     def flee(self):
#         print("This animal flees")

# class Predator:
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()

# METHOD OVERRIDING 🙅
# class Prey:
#     def flee(self):
#         print("This animal flees")

# class Prey2(Prey):
#     def flee(self):
#         print("This animal is hunting")

# prey = Prey2()
# prey.flee()

# METHOD CHAINING ⛓️ = calling multiple methods sequentially each call performs an action on the same object and returns self.
# class Car:
#     def turn_on(self):
#         print("You start the engine")
#         return self
    
#     def drive(self):
#         print("You drive the car")
#         return self
    
#     def brake(self):
#         print("You step on brakes")
#         return self
    
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
    
# car = Car()
# car.turn_on().drive().brake().turn_off()
# car.turn_on()\
# .drive()\
# .brake()\
# .turn_off()