#!/usr/bin/python3
import random

# Generate a random number between -10 and 10
number = random.randint(-10, 10)

# Print the number
print("The number is", number)

# Check if the number is positive, negative, or zero
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
