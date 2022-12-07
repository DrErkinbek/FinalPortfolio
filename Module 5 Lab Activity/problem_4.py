# Erkinbek
# 11/05/2022
# Write a program that does the following:
#  Print the numbers 1 through 50 to the screen
#  For numbers evenly divisible by 3, print “Divisible by 3” instead of the number
#  For numbers evenly divisible by 5, print “Divisible by 5” instead of the number
#  For numbers evenly divisible by both 3 and 5, print “Divisible by both”
for i in range(1, 50):
    print(i)
    if (i % 3 == 0 and i % 5 == 0):
        print(f' {i} Divisible both')
    elif(i % 3 == 0):
        print(f' {i} Divisible by 3')
    elif(i % 5 == 0):
        print(f' {i}  Divisible by 5')

print(7%3)