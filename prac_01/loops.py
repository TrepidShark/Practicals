for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 100, 10):
    print(i, end=' ')
print("Done")

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print("Done")

# c.
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()

# d.
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print("*" * i)
print()
