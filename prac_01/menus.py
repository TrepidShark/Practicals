
username = input("What is your name? ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {username}!")
    elif choice == "G":
        print(f"Goodbye {username}")
    else:
        print("invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input("Choice: ").upper()
print(f"We are done here user {username}!")
