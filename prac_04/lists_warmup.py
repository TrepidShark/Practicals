numbers = [3, 1, 4, 1, 5, 9, 2]

"""
Q1. 3
Q2. 2
Q3. 1
Q4. 3, 1, 4, 1, 5, 9
Q5. 1
Q6. True
Q7. False
Q8. 3, 1, 4, 1, 5, 9, 2, 6, 5, 3
"""
numbers[0] = "ten"
numbers[-1] = 1
print(numbers[1:-1])
if 9 in numbers:
    print(True)

