import random


def main():
    score = float(input("Enter score: "))
    while score <= 0:
        score = float(input("Enter score: "))
    # score = random.randint(1, 100)
    print(f"Your grade with a score of {score} is {gets_grade(score)}")


def gets_grade(score):
    if score > 100 or score < 0:
        return "Invalid score!"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()
