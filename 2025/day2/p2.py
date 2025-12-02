# day 2 (part 2)

with open("2025/day2/input.txt", "r") as file:
    line = file.read()
    split_strings = line.split(",") # split the line into individual strings

    ranges = [] # created to separate the first and second ID in each range
    for id in split_strings:
        first_str, last_str = id.split("-") # split each range into first and last ID
        first_id = int(first_str)
        last_id = int(last_str)
        ranges.append([first_id, last_id]) # append the pair of IDs as a list

def is_invalid_repeat(product_id):
    s = str(product_id) # convert ID to string to check repeating chunks
    length = len(s)

    for chunk_len in range(1, length // 2 + 1): # try all possible chunk lengths (1 up to half of the full ID)
        if length % chunk_len != 0: # the full ID must be divisible into equal chunks
            continue

        repeats = length // chunk_len # how many chunks in total
        chunk = s[:chunk_len] # the base chunk to test

        if chunk * repeats == s: # build the repeated version: chunk * repeats
            return True
        
    return False

t_invalid = 0 # total of the invalid IDs
for first_id, last_id in ranges:
    for product_id in range(first_id, last_id + 1):
        if is_invalid_repeat(product_id):
            t_invalid += product_id

print(t_invalid)