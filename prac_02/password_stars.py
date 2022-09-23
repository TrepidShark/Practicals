def main():
    minimum_length = 5
    password = get_password(minimum_length)
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password(minimum_length):
    password = input("Assign your password: ")
    while len(password) < minimum_length:
        print("Invalid Password")
        password = input("Assign your password: ")
    return password


main()
