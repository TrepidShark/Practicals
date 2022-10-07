"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the values entered are invalid, such as characters "f".
2. When will a ZeroDivisionError occur? When the user input 0 in the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, use a while loop to check the
value of the denominator, if the value == 0 than print error and ask again.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("ERROR")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")