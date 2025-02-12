# String properties and methods

## Index

Strings in python have index, that means, each character in a string has is own index that indicate what is its position in the string.

```
# To know what is the index of a character
my_text = "This is my text"
my_text.index("i") # Search 'i'
my_text.index("i", 4) # Search 'i' since 4 index to the last
my_text.index("i", 4, 10) # Search 'i' since 4 to 9 (10 is not into it)

# To know the character in certain index
my_text[2]
my_text[-2]

# Rindex method
my_text.rindex("i") # Search 'i' since last character to the first (from left to right)
```

## Slicing

Slicing in Python is a technique used to extract a portion of a sequence, such as a list, tuple, or string.

```
my_text = "That is my text"
slice = my_text[0:4]
slice = my_text[0:15:2]
print(slice)
```

## Methods

`text = This is the Jorge's text`

- Upper `print(text.upper()) >>> THIS IS THE JORGE'S TEXT`
- Lower `print(text.lower()) >>> this is the jorge's text`
- Split `print(text.split()) >>> ['This', 'is', 'the', 'jorge's', 'text']`

```
a = "Learn"
b = "Python"
c = "is"
d = "awesome"

```

- Join `e = " ".join([a, b, c, d]) >>> "Learn Python is awesome`
- Find `print(text.find("s"))`
- Replace `print(text.replace("Jorge", "George"))`

## Properties

- Immutable

```
name = "Jorge"
name[0] = 's'
# >>> Error
```

- Concatenable

```
name = "Jorge"
last = "Rubio"
print(name + " " + last)
# >>> Jorge Rubio
```

- Multiplicable

```
name = "Jorge"
names= name*5
print(names)
# >>> JorgeJorgeJorgeJorgeJorge
```

- Multiline

```
name = """Jorge
Rubio"""
print(name)
```

- Check substrings into strings

```
text = """A thousand small white fish
as if the color of the
wates was boiling
"""
print("thousand" in text)
print("thousand" not in text)
```

- Calculate length

```
text = """A thousand small white fish
as if the color of the
wates was boiling
"""
print(len(text))
```

## Lists

## Size

## concatenate

## Mutable

## Dictionaries

## Tuples

## Sets

## Booleans
