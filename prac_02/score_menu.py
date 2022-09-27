def main():
    print("(G)rade")
    print("(Q)uit")
    choice = input("Choice: ").upper()
    while choice != "Q":
        score = int(input("Enter score: "))
        score = get_valid_score(score)
        print(f"Your grade with a score of {score} is {get_grade(score)}")
        print("*" * score)
        choice = input("Choice: ").upper()
    print("GOODBYE")


def get_valid_score(score):
    while score < 0 or score > 100:
        score = int(input("Enter score: "))
    return score


def get_grade(score):
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
