import random

dice_art={
    1:("""
    +-------+
    |       |
    |   o   |
    |       |
    +-------+"""),
    2:("""
    +-------+
    | o     |
    |       |
    |     o |
    +-------+"""),
    3:("""
    +-------+
    | o     |
    |   o   |
    |     o |
    +-------+"""),
    4:("""
    +-------+
    | o   o |
    |       |
    | o   o |
    +-------+"""),
    5:("""
    +-------+
    | o   o |
    |   o   |
    | o   o |
    +-------+"""),
    6:("""
    +-------+
    | o   o |
    | o   o |
    | o   o |
    +-------+""")
}

# Clean up dice art by removing leading/trailing whitespace and splitting into lines
for key in dice_art:
    dice_art[key] = dice_art[key].strip().split('\n')

dice = []
total = 0
num_of_dice = int(input("how many dice do you want to roll: "))

for _ in range(num_of_dice):
    roll = random.randint(1, 6)
    dice.append(roll)
    total += roll

# Print dice side-by-side
# Each die in dice_art has 5 lines
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end="  ")
    print()

print(f"total: {total}")
