from coffee import Coffee

# Valid
latte = Coffee("Latte")
print(latte.name)  # "Latte"

# Invalid (too short)
try:
    bad = Coffee("AB")
except ValueError as e:
    print(e)  # Name must be a string with at least 3 characters

# Try changing the name (should fail)
try:
    latte.name = "Mocha"
except AttributeError as e:
    print(e)  # Can't set attribute
