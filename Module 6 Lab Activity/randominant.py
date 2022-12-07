# Erkinbek
# 11/8/2022

# Use random.radrange to print an odd integer between 0 and 100
import random

for i in range(0, 101):
    if i % 2 == 0:
        print(random.randrange(0, 100))
