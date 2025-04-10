"""
class Person:

    def __init__(self, name, age):
         self.name = name
         self.age = age

    def introduce(self):

        print("Hi, my name is " + self.name + " and I am " + str(self.age) + " years old.")


p1 =  Person("arian", 21)
p1.introduce()
"""






"""
class Dog:

    def __init__(self, name, energy):
        self.name = name
        self.energy = energy


    def bark(self):
        print("Woof! Im " + self.name)
        self.energy = self.energy - 10
        print(f"energy {self.energy}")


    def sleep(self):
        print(self.name + " is sleeping")
        self.energy = self.energy + 20
        print(f"energy {self.energy}")


d1 = Dog("Bruno", 100)
d1.bark()
d1.sleep()
"""




"""
class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed = self.speed + amount


    def brake(self, amount):

        if self.speed - amount < 0:

            self.speed = 0
        else:
            self.speed = self.speed - amount

    def status(self):
        print(f"The {self.brand} is going {self.speed}")


c1 = Car("BMW", 0)
c1.accelerate(40)
c1.brake(20)
c1.status()
"""



# Bank System (OOP)


"""
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance



    def deposit(self, amount):
        self.balance = self.balance + amount
        # add to balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough money")

        else:
            self.balance = self.balance - amount
        # subtract from balance if enough money

    def status(self):

        print(f"{self.owner} has {self.balance} $")


account1 = BankAccount("Arian", 500)
account1.status()
account1.deposit(200)
account1.withdraw(100)
account1.status()
"""



# Library Management System

class Book:

    def __init__(self, name, author):
        self.name= name
        self.author = author


    def __str__(self):
        return f"{self.name} by {self.author}  "






class Library:

    def __init__(self):
        self.shelf = []


    def add_book(self, add):

        self.shelf.append(add)



    def borrow_book(self, subtract):


        if subtract in self.shelf:
            self.shelf.remove(subtract)

        else:
            print("Sorry, book not available")




    def __str__(self):

        result = "Books available\n"
        for x in self.shelf:
            result = result + str(x) + "\n"
        return result




class Member:

    def __init__(self, member):

        self.member = member

    def display(self, book):

        r1 = f" {self.member} borrowed {book}"
        print(r1)




book1 = Book("DC", "George Orwell")
book2 = Book("The Alchemist", "Paulo Coelho")


lib1 = Library()
lib1.add_book(book1)
lib1.add_book(book2)
lib1.borrow_book(book2)

account1 = Member("Arian")
account1.display(book2)

print(lib1)
