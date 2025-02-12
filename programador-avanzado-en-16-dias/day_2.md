# Data type

| Type         | contraction | Information                                                           | Example                                             |
| ------------ | ----------- | --------------------------------------------------------------------- | --------------------------------------------------- |
| string       | str         | It's text                                                             | `"Hello world"`                                     |
| number       | int         | It's a integer number                                                 | `5`                                                 |
| number       | float       | It's a decimal number                                                 | `5.2`                                               |
| lists        | list        | It's a ordered collection of items (have index)                       | `["salt", 1, 2, -3, 4.5, "marte"]`                  |
| dictionaries | dict        | It's a collection of pairs of items (don't have order)                | `{"color": "red, "art": "music"}`                   |
| tuples       | tuple       | It's a ordered collection of elements but its order is immutable      | `("mon", "tue", "wed", "thu", "fri", "sat", "sun")` |
| sets         | set         | It's a ordered collection of unique items (don't have reapeted items) | `{"a", "b", "c", "d", "e"}`                         |
| booleans     | bool        | It's a date that only can be true or false                            | `True, False`                                       |

# Variables

A variable is a named storage location that holds data value, for example, strins, integers, floats, etcetera:

```
name = "Jorge Oziel"
print(name)
print(type(name))
```

# Rules for variable names

- Legible: must be consistent `dog_name = "terry"`
- Unit: should not have spaces, you can separate words using "\_" like `my_name = "Jorge"`
- Not hispanisms, for example: instead of año use anio
- You can use numbers, but not at the beginning
- You can't use signs
- You can't use keywords like print, input, string, and that kind of words.

# Casting

Casting is the process of transform a type of data to other type, there are two types of casting:

1. Implicit:
   A casting is called implicit when Python converts the data type to another data type automatically, that means, the user doesnot need to do anything. For example:

```
num1 = 20 # This variable is integer
num2 = 30.5 # This variable is a float

num1 = num1 + num2 = # Now num1 is converted automatically toa float
print(num1) # >>> 50.5
print(type(num1)) # >>> <class 'float'>
print(type(num2)) # >>> <class 'float'>
```

2. Explicit:
   A casting is called explicit when the user is who converts the data type to another. For example:

```
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1) # Here's the casting, we conveted a float to an integer
print(num2) # >>>5
print(type(num2)) >>> int <class 'int'>
```

# Format strings

Format strings also known as f-strins, are a way to embed expressions inside strings literals, using curly braces `{}`. There are several ways to format strings:

1. Using function format():

```
color_auto = "red"
license_plate = "GDLJ1921HB"
print("My car is {} and has the license plate {}".format(color_auto, license_plate))
```

2. Using literal strings:

```
color_auto = "red"
license_plate = "GDLJ1921HB"
print(f"My car is {color_auto} and has the license plate {license_plate}")
```

# Mathematic operations

```
x = 6
y = 2
z = 7
```

1. Addition
   `print(f"{x} plus {y} equals {x+y}")`
2. Substraction
   `print(f"{x} minus {y} equals {x-y}")`
3. Multiplication
   `print(f"{x} times {y} equals {x*y}")`
4. Division
   `print(f"{x} divided {y} equals {x/y}")`

- Floor division: It is a mathematical operation that divides two numbers and rounds the result down to the nearest integer. For example:
  `print"The floor division of {z} by {y} is {z//y}")`

5. Modulo
   This operation finds the remainder after division of one number by another
   `print(f"{z} modulo {y} is {z%y}")`

6. Power
   `print(f"{x} raised to the power of {y} is {x**y}")`

7. Root
   `print(f"The square root of {x} is {x**0.5}")`

# Rounding

This function returns a floating point number that is a rounder version of the specified number, with the specified number of decimals. round(number, digits)
`print(round(90/7,2))`
