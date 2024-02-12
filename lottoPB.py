import random

lotto_numbers = list(range(1,50))
# print(lotto_numbers)

print(random.choices(lotto_numbers, k=6))
