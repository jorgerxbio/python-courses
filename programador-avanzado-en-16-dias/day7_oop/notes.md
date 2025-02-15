# Object-Oriented Programming

OOP is a programming paradigm that focuses on objects, which can contain data and code data in the form of fields (often known as attributes or properties), and code in form of procedures (often known as methods). In OOP, computer progams are designed by making them out of objects that interact with one another. This paradigm is widely used and supported by many programming languages such as C++, Java, Python.

## What is a paradigm?

The word paradigm has its roots in Greek, derived from "paradeigma", meaning "pattern" or "model", which is a combination of "para" (beside) and "deiknymi" (to show). This etymology reflects the concept of a paradigm as a representative example of framework for understanding.
Some synonyms of paradigm include model, framework, pattern, and archetype, all of which convey the idea of a conceptual structure or a standard example that guides thought or behavior.

## Purpose

The purpose of the object-oriented paradigm was to adress the problems commonly grouped together as the "software crisis", which manifested itself in the complexity of large software projects. This complexity led to many problems, and OOP was seen as a way to organize and group methods and data structures into 'objects' that can be taken, reused, and inherited across different pieces of software.

- Simula: A language that introduces foundational concepts such as classes, objects and inheritance.
- Smalltalk: A language that advanced the OOP paradigm and introduced concepts such as encapsulation and polymomphism.

# Concepts

## Classes

Classes are blueprints, while an object are instances of a class. The instance captures the detailed information about one particular class.

## How to declare a class

```python
class Bird:  # Class declaration
    pass


my_bird = Bird()  # Instance of the Bird class
my_other_bird = Bird()  # Instance of the Bird class

print(my_bird)
print(my_other_bird)
```

## Constructor

A special method to initialize objects.

```python
def __init__(self):
    pass
```

## Methods overloading and overriding

Overloading allows multiple methods with the same name but different parameters, while overriding allows sublass to modify a method from its superclass.

## Atributes

```python
class Bird:  # Class declaration
    pass

    alas = True  # Class atribute

    def __init__(
        self, color
    ):  # Class constructor, it is used to create a instance of this class
        # self parameter represents the instance that will be created
        self.color = color  # Instance atribute


my_bird = Bird("blue")
print(my_bird.color)
```

# Methods

Methods are functions but they are associated to classes.

```python
    # Methods
    def piar(self):
        print("pio")

    def fly(self, feets):
        print(f"The {self.specie} has flown {feets} feets")

my_bird = Bird("blue", "toucan")
my_bird.piar()
my_bird.fly(10)
```

## Decorators

Decorators are functions that modify the behavior of other functions or methods. They allow you to wrap another function to add functinality without changing its actual codel

### How decorators work

Decorators use the @decorator_name syntax above a function definition. They take a function as an argument, modify or extend its behavior, and return a new function.

### Built-in Decorators:

1. instance methods: There are regular methods in a class that operate on an instance of the class. They take `self` as their first parameter, which represents the instance.
   - Can access and modify instance attributes
   - Can access other methods
2. @classmethod: Defines a method that receives the class as its first argument.
   ```python
   @classmethod
   def my_method(cls):
       print("something")
   ```
   - They are not associated to the class instances, but to the class itself, so they can be called not only from instances, but also from the class.
   - They can't modify the instance astributes, but can modify class atributes
3. @staticmethod: Defines a static method in a class.
   ```python
   @staticmethod
   def my_method():
       print("something")
   ```
4. @property: Defines a getter method for a class property.

# Principles

## Inheritance (Code reusability)

- Inheritance allows a class to inherit attributes and methods from another clas, promoting code reuse.
- Why? Avoid code duplication and makes maintenance easier.

```python
class Animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def be_born(self):
        print("This animal was born")


class Bird(Animal):
    pass


piolin = Bird(2, "yellow")

piolin.be_born()
print(piolin.color)
```

## Extended inheritance

```python
class Animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def be_born(self):
        print("This animal was born")

    def speak(self):
        print("This animal makes a sound")

class Bird(Animal):
    def __init__(self, age, color, flight_height):
        super().__init__(age, color) # Keyword for avoid to write self.astribute...
        self.flight_height = flight_height

    def speak(self): # Overwrite a method of the animal class
        print("pio")

    def fly(self, feets): # Add own method for bird class
        print(f"The bird flies {feets} feets")


piolin = Bird(2, "yellow", 5)

piolin.be_born()
print(piolin.color)
```

## Multiple inheritance

```python
class Father:
    def speak(self):
        print("Hola")

    pass


class Mother:
    def laugh(self):
        print("jasjdfwaerwaf")


class Son(Father, Mother): # Multiple inh
    pass


class Grandson(Son):
    pass


my_grandson = Grandson()

my_grandson.speak()
my_grandson.laugh()
```

## Encapsulation (Data Hiding)

- Encapsulation means building data (attributes) and methods (functions) within a class and restricting direct access to some details.
- Why? It protects internal objects state and enforces controlled access.

## Abstraction (Hiding Complexity)

- Abstraction means hiding complex details and exposing only essential features.
- Why? It simplifies code usage and reduces complexity.

## Polymorphism (Many Forms)

- Polymorphism allows different classes to trated as the same interface, meaning the same method name can have different behaviors.
- Why? It allows flexibility and generalization.

## Especial methods

```python

class CD:
    def __init__(self, author, title, songs):
        self.author = author
        self.title = title
        self.songs = songs

    def __str__(self):  # Modify the behavior of the special method __str__
        return f"Album: {self.title} by {self.author}"

    def __len__(self):  # Modify the behavior of the special method __len__
        return self.songs

    def __del__(self):
        print("The cd was deleted")


my_cd = CD("Pink Floyd", "The wall", 24)
print(my_cd)
print(len(my_cd))
del my_cd
```

# Code

```python
class Bird:  # Class declaration
    pass

    alas = True  # Class atribute

    def __init__(
        self, color, specie
    ):  # Class constructor, it is used to create a instance of this class
        # self parameter represents the instance that will be created
        self.color = color  # Instance atribute
        self.specie = specie

    # Instance methods
    def piar(self):
        print("pio")

    def fly(self, feets):
        print(f"The {self.specie} has flown {feets} feets")
        self.piar()  # Instance methods can also call other instance methods

    def print_dark(self):
        self.color = "dark"
        print(
            f"Now {self.specie} is dark"
        )  # Instance methods can modify instance atributes

    @classmethod
    def lay_leggs(cls, amount):
        print(f"Bird lay {amount} eggs")
        cls.alas = False  # Cass methods can modify class atributes

    @staticmethod
    def look():  # Static methods can't access to atributes or other methods
        print("Bird looks")


my_bird = Bird("blue", "toucan")
my_bird.piar()
my_bird.fly(10)
my_bird.alas = False
print(my_bird.alas)


# Calling class methods
Bird.lay_leggs(5)

# []
```
