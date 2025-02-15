# Functions

## Methods

Methods are function thar are associated with objects and can manipulate their data or perform actions on them. They are defined within a class and are called using dot notation, with the object name followed by a period and the method name.
There are types of methods in python: instance methods, class methods, and static methods. Example of string objects:

```python
"hello".upper() # This method modify the content of the string instance
"hello".index() # This return information of the string instance
```

## Help and documentation

You can get help in the web documentation of python and in your IDE with LSP

## Functions

A function is a block of code designed to perform a specific task. It can take input, manipulate it, and return an output. functions help in organizing and reusing code, adhering to the DRY (Don't Repeat Yourself) principle.

To define a function in Python, you use the def keword followed by the function name and parentheses. You can include parameters inside the parentheses to pass values into the function. After the function name and parentheses, you use a colon to indicate the start of the function block.
For example:

```python
def myfunction():
  print("Hello world")
```

To call this function , you simply write its name followed by parentheses:

```python
myfunction()
```

Function can also return values using the return keyword, which allows the function to send data back to the caller.
Python supports various types of functions, including built-in functions, user-defined functions, anonymous functions (lambda functions), and recursive functions.
Functions are essential in Python programming as they help in creating cleaner, more maintainable, and reusable code, which envolves enhances overall program efficiency and readability.
It's a good habit to write information about the function lower the definition, for example:

```python
def greet():
  """This function print a message of Hello world"""
  print("Hello world")
```

## Dinamic functions

```python
def check_3_figures(my_list):
    list_3_figures = []
    for n in my_list:
        if n in range(100, 1000):
            list_3_figures.append(n)
        else:
            pass
    return list_3_figures

result = check_3_figures([553, 992, 5674])
print(result)
```

## Function interaction

```python
from random import shuffle

# Inital list
sticks = ['-', '--', '---', '----']

# Mix sticks
def mix(my_list):
    shuffle(my_list)
    return my_list

# Ask for a number
def try_your_luck():
    attempt = ''

    while attempt not in ['1', '2', '3','4']:
        attempt = input("Choice a number between 1 and 4: ")

    return int(attempt)

# Check attempt
def check_attempt(my_list, attempt):
    if my_list[attempt - 1] == '-':
        print("Let's wash the dishes")
    else:
        print("You are safe this time")

    print(f"You got number {my_list[attempt - 1]}")

mixed_sticks = mix(sticks)
the_choice = try_your_luck()
check_attempt(mixed_sticks, the_choice)
```

## Undefined arguments

In python, undefined arguments refer to variables that have not been declared or initialized before being used in a function call, or elsewhere in the code. This can lead to errors such as "NameError: name 'variable_name' is not defined" when the interpreter encounters the variable without a prior definition.

When defining a function, if you pass arguments that are not defined, Python will raise an error indicating that the argument is undefined. For example, if you define a function expecting certain arguments but do not provide them or provide them incorrectly, you might receive an error message like "display_results() takes 0 position arguments but 5 were not given" if the function is not set up to accept the given number of arguments.

To hande undefined arguments more elegantly, you can use default values for function parameters, allowring the function to run even if certain arguments are not provided. Adittionally, you can use \*args and \*\*kwargs to accept a variable number of arguments and keyword arguments, respectively.

### Default arguments: By setting default values for function parameters, you can ensure the function can run even if some arguments are not provided. For example:

```python
def my_function(arg1, arg2=None):
    # Function body
```

Here, arg2 has a default value of None, so the function can run even if arg2 is not provided.

### Variable arguments (\*args and \*\*kwargs)

These allow you to pass a variable number of arguments to a function. \*args collects non-keyworded arguments into a tuple, while \*\*kwargs collects keyworded arguments into a dictionary.
Args:

```python
def suma(*args):
    return sum(args)

print(suma(5, 6, 100, 2, 5))
```

Kwargs:

```python
def test(num1, num2, *args, **kwargs):
    print(f"first value is {num1}")
    print(f"second value is {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for key, value in kwargs.intems():
        print(f"{key} = {value}")

args = [100, 200, 300, 400]
kargs = {'x': 'uno', 'y': 'dos'}

test(10, 15, args, kwargs) # This is valid
test(10, 15, 100, 200, 300, 400, x='uno', y='dos') # This is also valid
```
