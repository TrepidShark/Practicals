"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
# FIXED!

score = float(input("Enter score: "))
while score <= 0:
    score = float(input("Enter score: "))
if score > 100:
    print("Invalid score!")
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

