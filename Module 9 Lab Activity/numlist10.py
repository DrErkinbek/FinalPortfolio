"""
Erkinbek
12/6/2022
Create list which contains number from 0 to 10.
On each iteration, the loop should append the current value
 a counter variable to the list and then
increase the counter by 1. The while loop should stop
once the counter variable is greater than
10.
"""
L = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
new_list = []
while i < len(L):
    i += 1
    new_list.append(i + 1)
print(new_list)