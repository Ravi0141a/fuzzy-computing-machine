# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

# Taking integer input from the user
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")