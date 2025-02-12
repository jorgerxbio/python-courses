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

## Data

| Data         | Properties                                    | Methods                                          | Example            |
| ------------ | --------------------------------------------- | ------------------------------------------------ | ------------------ |
| Lists        | Index, concatenation, mutable                 | append, pop, sort, reverse                       | ['a', 5, 6.7]      |
| Dictionaries | Pair items, Key uniques, Key search           | keys, values, items                              | {'c1': 1, 'c2': 2} |
| Tuples       | Index, immutable,                             | count, index                                     | (1, 2, 3, 4)       |
| Sets         | Unique items, not index, not order, immutable | add, remove, discard, pop, clear                 | ((1, 2, 3 , 4))    |
| Booleans     | True or False                                 | Can be declare it using a comparative expression | True               |

## Lists

Lists are a ordered sequence ofi tems and they can be assigned to a varaible and their items cs nbe of any data type, even a list can be composed of different data types. Lists are written in brackets and their elements are separated from each other by a comma. They can be nested or indexed, and they also have methods for manipulating, and they aren't immutable.

Definition:

```python
my_list = ['a', 'b', 'c']
```

Index:

```python
my_list[0:3]
```

Concatenation:

```python
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
```

Immutable:

```python
my_list3[0] = 'alpha'
```

Methods:

```python
my_list3.append('g')
item_removed = my_list3.pop()
my_list3.sort()
my_list3.reverse()
```

## Dictionaries

Dictionaries are a collection of pairs of items, these pairs are key-value items, and each key are uniques, how is a dictionarie written in python, between curly braces, pairs are separated o other using comma, and key is aperated of its value using colon. Dictionaries don't have order.

```python
client = {"nombre": "Juan", "apellido": "Fuentes", "peso": 88, "talla": 1.76}
consult = client["apellido"]  # Get the value of a specify key
print(consult)

# It's possible to nest dictionaries
dictionarie = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dictionarie["c2"][1])

dictionarie = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dictionarie["c2"][1].upper())

dictionarie = {1: "a", 2: "b"}
print(dictionarie)

dictionarie[3] = "c"  # Append a item
print(dictionarie)

dictionarie[2] = "B"  # Dictionaries aren't immutable

print(dictionarie.keys())
print(dictionarie.values())
print(dictionarie.items())
```

## Tuples

Tuples are collection of items similar to lists but with a big difference, they are immutable, also they are wirtten between parenthesis (is also posible written it without parenthesis) and items are separated of each other using commas.
Advantages: They use less memory that lists, and its immutable can be a benefit to avoid problems of modify the collection accidentally.

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple[2])  # Index is in tuples

my_tuple = list(my_tuple)  # Casting is possible between lists and tuples
print(type(my_tuple))

v, x, y, z = my_tuple  # This assignacion is possible

# Tuples methods
my_tuple = (1, 2, 3, 1)
print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index(1))
```

## Sets

Sets are a collection of items similar to lists but with some differences. Sets can be defined writting the word "sets" and then write their elements between parenthesis and using commas to separate items of each others. But in this way you need to get into brackets the elements because python only recognize it like a one argument, this is: `sets([1, 2, 3])`
Other way is writting items between curly braces like `{1, 2, 3, 4}`
Properties:

- They just accepts unique items (not repeated)
- Items have not order, that means that you can't index or order it.
- They are immutable, so you can't include lists or dictionares into it.

```python
my_set = set([1, 2, 3, 4])
my_set = {1, 2, 3, 4}
print(type(my_set))

print(len(my_set))
print(2 in my_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4) # Add a item
s1.remove(3) # Remove a item
s1.discard(6) # Discard a element
s1.pop() # Remove a random item
s1.clear() # Clear the set
```

## Booleans

Bools only can be True or False. The way to declare them is by using a variable and assigning it one of these values, or also a expression True or False:

```python
my_bool = True
my_bool = bool() # This gonna be False
my_bool = 5 > 3
```
