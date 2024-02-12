import random

# Generate 6 unique random lottery numbers between 1 and 50
lottery_numbers = random.sample(range(1, 51), 6)

# Display the generated lottery numbers
print("Lottery Numbers:", lottery_numbers)

# Iport the random module from the Python standard library. We use the random.sample() function to generate 6 unique
# random numbers between 1 and 50. The random.sample() function takes two arguments: a range of numbers (1 to 50) and
# the number of samples to be chosen (6). The range(1, 51) function generates numbers from 1 to 50 (inclusive). The
# random.sample() function returns a list containing 6 unique random numbers. Finally, we print the generated lottery
# numbers using the print() function.
