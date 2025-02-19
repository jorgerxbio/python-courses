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
