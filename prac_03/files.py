# 1
name = input("What is your name? ")
for line in name:
    with open("name.txt", 'w') as out_file:
        print(name, file=out_file)

# 2
name = input("What is your name? ")
for line in name:
    with open("name.txt", 'w') as out_file:
        print("Your name is", name, file=out_file)

# 3
numbers = open("numbers.txt", 'r')
number1 = int(numbers.readline())
number2 = int(numbers.readline())
numbers.close()
total = number1 + number2
print(total)

# 3 extension
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    total = total + int(line)
print(total)


