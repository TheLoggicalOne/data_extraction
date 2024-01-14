from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Accessing enum values
print(Color.RED)  # Color.RED
print(Color.RED.value)  # 1

# Iterating over enum values
for color in Color:
    print(color)

# Comparing enum values
print(Color.RED == Color.GREEN)  # False
print(Color.RED == Color.RED)  # True


# Using an enum in a function
def print_color(color):
    if color == Color.RED:
        print("You selected the color red.")
    elif color == Color.GREEN:
        print("You selected the color green.")
    elif color == Color.BLUE:
        print("You selected the color blue.")


print_color(Color.GREEN)  # You selected the color green.
