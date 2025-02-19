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
