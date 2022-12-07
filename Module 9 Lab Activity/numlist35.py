"""
Erkinbek
12/6/2022
Using a while loop, ask the user to enter a number. Append each entered number
to a list and add them together. Continue asking for a number until the sum of the list of
numbers is greater than 100.
"""

i = 0
num_list = []
while i < 100:
    i += 1
    user_input = int(input("Enter any number "))
    num_list.append(user_input)
    if sum(num_list) == 100:
        break
print(num_list)
