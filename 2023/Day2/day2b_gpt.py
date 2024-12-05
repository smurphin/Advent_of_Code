filename = 'day2_input.txt'
import time

start_time = time.time()
cpu_start_time = time.process_time()

# Function to process each game's data
def process_game(game_data):
    game_name, parts = game_data.split(': ')
    parts = parts.split('; ')
    color_max = {'red': 0, 'green': 0, 'blue': 0}
    for part in parts:
        items = part.split(', ')
        for item in items:
            number, color = item.split(' ')
            color_max[color] = max(color_max[color], int(number))
    return color_max

# Process each game from the file and calculate power
sum_of_power = 0
with open(filename, 'r') as file:
    for line in file:
        color_max = process_game(line.strip())
        power = color_max['red'] * color_max['green'] * color_max['blue']
        sum_of_power += power

print('Sum of power of all games =', sum_of_power)

cpu_end_time = time.process_time()
end_time = time.time()
print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
print(f"CPU Execution time: {(cpu_end_time - cpu_start_time) * 1000} milliseconds")
