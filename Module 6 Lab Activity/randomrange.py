# Erkinbek
# 11/8/2022

# Use a for loop and random.range to print
# 10 random integers between 25 and 35
from random import randrange
import random
list_nums = []
for i in range(1, 10):
    list_nums.append(random.randint(25, 35))
    print(random.randint(25, 35))
print(list_nums)


