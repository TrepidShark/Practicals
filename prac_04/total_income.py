"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        # income = float(input("Enter income for month " + str(month) + ": "))
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    compile_report(incomes, number_of_months)


def compile_report(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print_report(income, month, total)


def print_report(income, month, total):
    print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
