from prac_06.guitar import Guitar


my_guitar = Guitar("My_guitar", 1922, 1000000)
other_guitar = Guitar("Other_guitar", 2013, 1000)

print(f"Gibson L-5 CES get_age() - Expected 100. Got {my_guitar.get_age()}")
print(f"My other guitar get_age() - Expected 9. Got {other_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {my_guitar.is_vintage()}")
print(f"My other guitar is_vintage() - Expected False. Got {other_guitar.is_vintage()}")
