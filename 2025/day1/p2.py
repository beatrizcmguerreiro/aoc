# day 1 (part 2)

with open("2025/day1/input.txt") as f:
    rotation_instructions = [line.strip() for line in f]

# initial arrow position is 50 and number of zeros passed while rotating is 0
inicial_arrow = 50
passing_zero = 0

# separate each line of the list of rotations
for rotation in rotation_instructions:
    direction = rotation[0] # first character of the string, either L or R
    distance = int(rotation[1:]) # take everything in the string AFTER the first character and convert to int

    if direction == 'L': # count groups of 100 starting from the flipped position
        flipping = (100 - inicial_arrow) % 100 # converting the LEFT move into a RIGHT move,, distance from x to 0 going left is the same as the distance from (100 - x) going right
        passes = (flipping + distance) // 100
        inicial_arrow = (inicial_arrow - distance) % 100

    else: # count groups of 100 starting from 0
        passes  = (inicial_arrow + distance) // 100
        inicial_arrow = (inicial_arrow + distance) % 100

    passing_zero += passes

print(passing_zero)