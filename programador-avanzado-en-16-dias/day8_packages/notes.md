# Installing packages

PyPi is a open-source repository:

```bash
pip install
```

It's recommendable to create a python environment and then install packages into it instead of installing the packages on your operating system.

# What is a module?

A module is code of python storaged in a python file (a file with extension .py)

# What is a package

A package is a group of modules

All packages need to have atleast a file called `__init__.py` is useful to python understand that is a package and not a common directory

# Create modules and packages

# Error handling

## Try

## Except

## Finally

# Error detecting using pylint

```python
def addition():
    n1 = int(input("number 1: "))
    n2 = int(input("number 2: "))
    print(n1 + n2)
    print("Thanks for addition" + n1)


try:
    addition()
except TypeError:
    # Code to run if there are a error
    print("You're trying concatenate different types of data")

except ValueError:
    print("You're trying to enter a string instead of a number")
else:
    print("All is fine")
    # Code to run if there are not a error
    pass
finally:
    print("That was all")
    # Code to run always
```

```python
def ask_for_a_number():

    while True:
        try:
            number = int(input("Give me a number: "))
        except:
            print("That is not a number")
        else:
            print(f"You entered the number {number}")
            break

    print("Thanks")


ask_for_a_number()
```

# Pyling

Run "python file.py -r y" to watch a report of your code
For example, a good code:

```python
"""
This is a module to ask for a number without errors
"""


def ask_for_a_number():
    """
    This function does something important
    """

    while True:
        try:
            number = int(input("Give me a number: "))
        except (ValueError, TypeError):
            print("That is not a number")
        else:
            print(f"You entered the number {number}")
            break

    print("Thanks")


ask_for_a_number()
```

# Test code using unittest

```python
def upper_case(text):
    return text.upper()
```

```python
import unittest

import change_text


class TestChangeText(unittest.TestCase):
    def test_upper_case(self):
        word = "good day"
        result = change_text.upper_case(word)
        self.assertEqual(result, "GOOD DAY")


if __name__ == "__main__":
    unittest.main()
```

# Decorators

They are functions that modify the behavior of other functions

```python
"""
Everything in python is a object, inclusive the functions are objects
"""


def upper_case(text):
    print("hello")
    print(text.upper())
    print("goodbye!")


def lower_case(text):
    print(text.lower())


def a_function(function):
    return function


my_function = upper_case  # A function can be assigned to a variable

a_function(upper_case("testing")) # A function can be pass as a argument in a function

my_function("python")
```

```python
"""
Everything in python is a object, inclusive the functions are objects
"""


def change_letters(typ):

    def upper_case(text):
        print("hello")
        print(text.upper())
        print("goodbye!")

    def lower_case(text):
        print(text.lower())

    if typ == "upp":
        return upper_case
    elif typ == "low":
        return lower_case
    else:
        print("Invalid operation type")
        return lambda text: None  # Return a no-op function (does nothing)


my_operation = change_letters("low")

my_operation("word")
```

```python
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower()):

mayuscula_decorada = decorar_saludo(mayusculas)

mayusculas_decorada('georce')
```

# Generators

```python
def my_generator():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = my_generator()

print(next(g))
print(next(g))
print("Hello")
print(next(g))
```
