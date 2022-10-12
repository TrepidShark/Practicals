import random


number_of_picks = int(input("how many quick picks? "))
for quick_pick in range(number_of_picks):
    list_of_picks = []
    for i in range(6):
        random_number = random.randint(1, 45)
        while random_number in list_of_picks:
            random_number = random.randint(1, 45)
            # print("------------------------------------------------------------------")
        list_of_picks.append(random_number)
    print(*list_of_picks, sep=" ")

