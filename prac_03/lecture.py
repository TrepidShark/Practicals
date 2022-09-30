# filename = input("What is the filename? ")
# in_file = open(filename, "r")
# for line in in_file:
#     # if line[0] == "#":
#     if line.startswith("#"):
#         print(line.strip())
# in_file.close()

# in-c
# total = 0
# line_number = 0
# error_list = []
# filename = input("What is the filename? ")
# in_file = open(filename, "r")
# for line in in_file:
#     line_number += 1
#     try:
#         total = total + int(line)
#     except ValueError:
#         error_list.append(line_number)
# in_file.close()
# print(total)
# print("The following numbers are where there were errors:", end='')
# print("".join([str(line) for line in error_list]))

# filenames = ["Monkey", "Ape", "Human"]
# for name in filenames:
#     with open(name + ".txt", 'w') as out_file:
#         print(name, file=out_file)

