def main():
    choice = input("Do you want to convert to Celsius or Fahrenheit? ").lower()
    user_temperature = float(input("What is the temperature? "))
    while choice != "celsius" and "fahrenheit":
        print("Choose one: Celsius or Fahrenheit")
        user_temperature = float(input("What is the temperature? "))
    new_temperature = convert_temperature(choice, user_temperature)
    print(f"Your converted temperature is {new_temperature}")


def convert_temperature(choice, user_temperature):
    if choice == "celsius":
        new_temperature = (user_temperature - 32) * 5 / 9
    elif choice == "fahrenheit":
        new_temperature = (user_temperature * 9 / 5) + 32
    return new_temperature


main()
