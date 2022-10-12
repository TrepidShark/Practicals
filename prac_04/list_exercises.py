MAX_NUMBERS = 5
total = 0
numbers = []
valid_user = False
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input = input("What is your username? ")
if user_input in usernames:
    valid_user = True

if valid_user is True:
    for i in range(MAX_NUMBERS):
        number = int(input("Number: "))
        numbers.append(number)
    # print(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    for number in numbers:
        total = total + number
    average_numbers = total / MAX_NUMBERS
    print(f"The average of the numbers is {average_numbers}")
