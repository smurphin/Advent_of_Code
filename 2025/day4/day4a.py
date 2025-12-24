import time


t1 = time.time() * 1000

with open("../../2025/inputs/day4test.txt") as f:
    # Reads the file, splits lines, splits numbers, converts to int
    # All in one highly optimized pass
    print(f)
    data = [[digit for digit in line.strip()]for line in f if line.strip()]

def get_coordinates(pos, current_data):
    width = len(current_data[0])
    col = pos % width
    row = pos // width
    north = current_data[row-1][col]
    north_east = current_data[row-1][col+1]
    east = current_data[row][col+1]
    south_east = current_data[row+1][col+1]
    south = current_data[row+1][col]
    south_west = current_data[row+1][col-1]
    west = current_data[row][col-1]
    north_west = current_data[row-1][col-1]
    return [north, north_east, east, south_east, south, south_west, west, north_west]

def count_rolls(input_data):
    current_pos = 0
    total1 = 0
    for row in input_data:
        for symbol in row:
            if symbol == '#' or symbol == '.':
                current_pos += 1
                continue
            check = get_coordinates(current_pos, input_data)
            #print(f"Pos {current_pos} is [{position}] -> Neighbors: {check}")
            if check.count('@') < 4:
                total1 += 1
                #print(f"  -> Has {check.count('@')} neighbors with '@'")
            current_pos += 1
    return total1

bordered_data = []
len_row = len(data[0]) + 2
bordered_data.append(['#'] * len_row)
for line in data:
    bordered_data.append(['#'] + line + ['#'])
bordered_data.append(['#'] * len_row)

total = count_rolls(bordered_data)

print(f"Total neighbors with '@': {total}")
# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")