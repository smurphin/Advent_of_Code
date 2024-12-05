filename = 'day2_input.txt'
import re
import time

start_time = time.time()
cpu_start_time = time.process_time()

# Function to process each game's data
def process_game(game_data):
    game_name, parts = game_data.split(': ')
    parts = parts.split('; ')
    game_results = []
    game_id = int(game_name.strip('Game '))
    for part in parts:
        part_dict = {}
        items = part.split(', ')
        for item in items:
            number, color = item.split(' ')
            part_dict[color] = int(number)
        game_results.append(part_dict)
    return {game_id: game_results}

# Function to check if a game meets the criteria
def meets_criteria(game_data):
    for part in game_data:
        if part.get('red', 0) > 12 or part.get('green', 0) > 13 or part.get('blue', 0) > 14:
            return False
    return True

# Process each game from the file and filter based on criteria
valid_games = []
with open(filename, 'r') as file:
    for line in file:
        game_dict = process_game(line.strip())
        game_id, game_data = next(iter(game_dict.items()))
        if meets_criteria(game_data):
            valid_games.append(game_id)

print("Games that would have been possible:", valid_games)
print(f"Total: {sum(valid_games)}")


cpu_end_time = time.process_time()
end_time = time.time()
print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
print(f"CPU Execution time: {(cpu_end_time - cpu_start_time) * 1000} milliseconds")