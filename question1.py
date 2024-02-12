cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
# Question 1:

# The issue is that it attempts to add the string 'Oke' to the cheese list using the += operator.
#  However, the += operator is used to concatenate sequences, not to append individual elements to a list.
# As a result, instead of adding 'Oke' as a separate element to the list, it adds each character of 'Oke' as separate
# elements, resulting in ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e'].

# To add 'Oke' as a single element to the end of the cheese list, it should be enclosed within square brackets to
# create a single-element list, and then concatenated using the += operator, like this:

cheese += ['Oke', 'Mozzarella']
print(cheese)

cheese.append('Gouda')  # Method 1: Append 'Oke' as a single element
# OR
cheese.extend(['Brie'])  # Method 2: Extend the list with a list containing 'Oke'
print(cheese)