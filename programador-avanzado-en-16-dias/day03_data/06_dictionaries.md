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
