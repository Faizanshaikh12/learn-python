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

# SUPER FUNCTION 🦸 = super() = Function used to give access to the methods of a parent class.
                                # Returns a temporary object of a parent class when used.
# Rectangle is super
# class Rectangle:
#     def  __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Square(Rectangle):
#     def __init__(self, length, width):
#         super().__init__(length, width)
    
#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
    
#     def volume(self):
#         return self.length*self.width*self.height
    
# square = Square(3,3)
# cube = Cube(3,3,3)
# print(square.area())
# print(cube.volume())

# ABSTRACT CLASSES 👻
# Prevents a user from creating an object of that class
# Compels a user to override abstract methods in a child class
# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def go(self):
#         print('You drive the car')
     
#     def stop(self):
#         print('This car is stopped')

# class MotorCycle(Vehicle):
#     def go(self):
#         print('You drive the motor cycle')
     
#     def stop(self):
#         print('This motor cycle is stopped')
        
# car = Car()
# car.go()
# car.stop()
# motorCycle = MotorCycle()
# motorCycle.go()
# motorCycle.stop()

# OBJECTS AS ARGUMENTS 🏍️
# class Car:
#     color = None

# class Bike:
#     color = None


# def change_color(car, color):
#     car.color = color

# car = Car()
# bike = Bike()

# change_color(car, "PINK")
# change_color(bike, "BLUE")

# print(car.color)
# print(bike.color)

# DUCK TYPING 🦆
# concept where the class of an object is less importent than the methods class type is not checked if minimum methods/attributes are present
# "If it walks like a duck, and it quacks like a duck, than it must be a caugth"

# class Duck():
#     def walk(self):
#         print("This duck is walking")

#     def talk(self):
#         print("This duck is qwuacking")

# class Chicken:
#     def walk(self):
#         print("This is chicken is walking")
    
#     def talk(self):
#         print("This duck is clucking")

# class Person:
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")


# duck = Duck()
# chicken = Chicken()
# person = Person()
# person.catch(duck)
# person.catch(chicken)

# WALRUS OPERATOR 🦦
# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variable as part of a larger expression

# happy = True
# print(happy := True)

# foods = list()
# while True:
#     food  = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)

# ZIP FUNCTION 🤐 (*iterables)
# aggregate elements from two or more iterables (list, tuples, sets etc.)
# creates a zip object with paired elemetns stored in tuples for each elements.
usernames = ["Dude", "Bro", "Mister"]
passwords = ["Password", "Admin123", "guest"]

users = zip(usernames, passwords)
for i in users:
    print(i)
