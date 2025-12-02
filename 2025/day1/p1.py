# day 1 (part 1)

with open("2025/day1/input.txt") as f:
    rotation_instructions = [line.strip() for line in f]

# initial arrow position is 50 and number of zeros is 0
inicial_arrow = 50
zero_count = 0

# separate each line of the list of rotations
for rotation in rotation_instructions:
    direction = rotation[0] # first character of the string, either L or R
    distance = int(rotation[1:]) # take everything in the string AFTER the first character and convert to int

    if direction == 'L':
        inicial_arrow = (inicial_arrow - distance) % 100 # using modulo in case the number is negative
    else:
        inicial_arrow = (inicial_arrow + distance) % 100 # using modulo in case the number is negative
    
    if inicial_arrow == 0: # if the arrow is at position 0, increment the count
        zero_count += 1
        
print(zero_count)