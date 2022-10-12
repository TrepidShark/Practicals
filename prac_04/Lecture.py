names = ["Cian", "AdA", "Piyush"]
print(", ".join(names))
name = input("Who do you want to remove? ")
while name != "":
    try:
        names.remove(name)
    except ValueError:
        print(f"{name} is not in the list")
    print(", ".join(names))
    name = input("Who do you want to remove? ")
print("Thanks for your input")

values = [[3, 4, 5, 1], [33, 6, 1, 2]]

v = values[0][0]
for row in range(len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]
print(v)

def main():
    numbers = get_numbers()
    # square_numbers(numbers)
    # display_numbers(numbers)
    print(numbers)


def get_numbers():
    text = input("Enter numbers seperated by a comma: ")
    strings = text.split(",")
    return [float(string) for string in strings]


def square_numbers(numbers):
    for i, number in enumerate(numbers):
        numbers[i] = number ** 2


main()
