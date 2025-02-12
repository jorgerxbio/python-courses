# Day 4

## Comparison operator

comparison operators are used to compare two values and return a boolen value basen on the comparison result.

```python
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equal to
!= not equal to
```

## Logical operator

Logical operators are symbols or words used to connect two or more expressions to create a compound expression whose value depends only on the original expressions and the meaning of the operator. Common logical operators are AND, OR, and NOT. These operators are fundalmental in programming and are used to create complex Boolean expressions that control progam flow and implement decision-making logic.

```python
my_bool = 4 < 5 > 6
print(my_bool)

# And
my_bool = 4 < 5 and 5 > 6

# Or
my_bool = 4 < 5 or 5 > 6

text = "hello python I'm world"
my_bool = ('python' in text) or ('hello' in text)
print(my_bool)

# Not
my_bool = not 4 < 5
my_bool = not (4 < 5)
```

## Control flow

Refers to the order in which individual statements, instructions, or function calls are executed or evaluated. It is regulated by conditional statements, loops, and funtion calls, allowing programmers to specify how the program should act in response to specific circumstances and take appropiate action.
This concept is fundamental in programming as it enables devlopers to write programs that can make decisions based on certain conditions, making thep programs more flexible and adaptable.

```python
if 5 > 10:
  print("5 is greater than 10")
elif 5 == 10:
  print("5 is equal to 10")
else:
  print("t is less than 10")
```

## Loops

Loops are control flow statements that allow you to repeat a given set of operations a number of times. There are two main types of loops:

### For loops

They are generally used to interate over the items in a data collection, such as a list, tuple, string, or dictionary. The basic syntax of a for loop is:

```python
for variable in iterable:
  statements(s)

my_list = ['a', 'b', 'c', 'd']

for letter in my_list:
  number_letter = my_list.index(letter) + 1
  print(f"Letter {number_letter}: {letter}")

for a, b in [[1, 2], [3, 4], [5, 6]]:
  print(a)
  print(b)

dic = {'c1': 'a', 'c2': 'b', 'c3':'c'}

for item in dic:
  print(item)

for item in dic.items:
  print(item)

for item in dic.values:
  print(item)

for a, b in dic.items:
  print(a)
  print(b)
```

### While loops

On the other hand these loops repeat as long as a certain boolean condition is met. For example:

```python
count = 0
while count < 5:
  print(count)
  count += 1

  break, continue and pass

coins = 5
while coins > 0:
  print(f"I have {coins} coins")
  coins -= 1
else:
  print("I don't have coins")

while coins > 0:
   pass # Save this site to write code later
else:
  print("I don't have coins")


while coins > 0:
  if coins == 3:
    break # Get out of the loop
else:
  print("I don't have coins")

while coins > 0:
  if coins == 3:
    continue # Break of this iteration but the loop continue with the next iteration
else:
  print("I don't have coins")
```

## Range

It is a function to create a collection of number like:

```python
my_list = list(range(100))

for n in range(1,20,2):
  print(n)
```

### Enumerator

This is a function that simplifies the process to access the index of the items in our list.

```python
my_list = ['a', 'b', 'c']
index = 0

for item in my_list:
  print(index, item)
  index += 1

for item in enumerate(my_list):
  print(item)

for index item in enumerate(my_list):
  print(index, item)
```

### Zip

It's a function that mix two or more lists mixing their elements in tuples:

```python
names = ["Ana", "Hugo", "Valeria"]
ages = [65, 29, 42]
cities = ["Lima", "Madrid", "Mexico"]

combined = list(zip(names, ages, cities))
print(combined)

for name, age, city in combined:
    print(f"{name} is {age} and live in {city}")
```

## Min and Max

They are functions that are used to obtain the minimum or maximum of a list, whether numeric or alphabetical.

```
mini = min(58, 96, 72, 64, 35)
maxi = max(58, 96, 72, 64, 35)
print(mini, maxi)
```

## Import modules

What is a module?
A module is a single file containing Python definitions and statements, typically used to organize related code into separate files for better maintenance and reusability.
What is a library:
A library refers to a collection of modules. It is a broader term that generally refers to a package or collection of related modules that provide specifig functionality.
How to import them?
To import a method: `from random import randint`
To import all: `from random import *`

## Random

```python
from random import *

# randint() #Random integer
random = randint(1, 50)
print(random)

# - uniform()
uniform = uniform(1, 5) # Random decimal
uniform = round(uniform(1, 5), 1) # Random number with a decimal
print(uniform)

# - random() # A number between 0 and 1
random = random()

# - choice() # Select a random item into a list
colors = ['blue', 'red', 'green', 'yellow']
choice = choice(colors)
print(choice)

# - shuffle() # Shuffle or mix a list
numbers = list(range(5, 50, 5))
shuffle(numbers)

print(numbers)
)
```

## List comprehension

Referst to a concise way to create lists using a specific syntax, allowing for the generation of new lists by applying an expression to each item in an existing iterable, such as a list or range. Example:

```python
pies = [10, 20, 30, 40, 50]
metros = [n / 3.281 for n in pies]
print(metros)

# Commun method
my_list = []
word = "python"
for letter in word:
  my_list.append(letter)

# Comprehension list
my_list = [letter for letter in word]

# Other comprehension lists
my_list = [letter for letter in 'python']
my_list = [n for n in range(0, 21, 2)]
my_list = [n/2 for n in range(0, 21, 2)]
my_list = [n for n in range(0, 21, 2) if n*2 > 10]
my_list = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
```

## Match

```python
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("That product doesn't exist")
```
