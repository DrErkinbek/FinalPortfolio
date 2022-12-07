# for i in range(10):
#     print(i)

# Conditional
# Evaluates to True or False
# <> == != <= =>

# While loops
# if 0 < 3:
#     print("True")
#
# while 0 < 3:
#     print("True")

i = 0
while i < 3:
    i += 1
    print(i)

def get_L_R():
    user_input = input("Do you want to go left (L) or right (R)?")
count = 0
user_input = input("Do you want to go left (L) or right (R)?")
# This loop will stop if the loop 3 times or enters "R"
while count < 3 and user_input != "R":
    #For user to give you L or R
    while user_input != "L" and user_input != "R":
        print("Invalid input!")
        user_input = input("Do you want to go left left (L) or right (R)?")
