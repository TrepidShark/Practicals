minimum_length = 5
password = input("Assign your password: ")
while len(password) < minimum_length:
    print("Invalid Password")
    password = input("Assign your password: ")
print("*" * len(password))