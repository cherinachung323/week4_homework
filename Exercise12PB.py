## Q1: What is wrong with this?
## ANSWER
## there is a separator after each character when "Oke" is added to the list.
## need to concatenate a list, not a string.
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
print(type(cheese))
print("\n" + "#" * 50)

## How should 'Oke' be added to the end of the list?
## Append new item(s) to the end of your list by wrapping them in []
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke','Brie']
print(cheese)
print("\n" + "#" * 50)

## Q2: What's going on here? Can you explain the output?
## len function is counting the number of characters in 'Hello' as a string.
tup = 'Hello'
print(len(tup))
# print(type(tup))
## the comma after 'Hello' makes this object a tuple.
## len function is counting the number of items in the tuple.
tup = 'Hello',
print(len(tup))
# print(type(tup))