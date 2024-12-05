
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


# Process each game from the file and store in a list
all_games = []
with open(filename, 'r') as file:
    for line in file:
        game = process_game(line.strip())
        all_games.append(game)

#print(all_games)

#example for documentation / understanding
#game_data = [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
#[expression for item in iterable if condition]
#(x['red']): In each iteration, x is one of the dictionaries from game_data. 
# The expression x['red'] is accessing the value associated with the key 'red' in the dictionary x.
# This is the primary way to iterate through a dictionary in Python. You just need to put the dictionary directly into a for loop, and you’re done!
# If you use this approach along with the [key] operator, then you can access the values of your dictionary while you loop through the keys:
# https://realpython.com/iterate-through-dictionary-python/#looping-over-dictionary-items-the-items-method
#red = [x['red'] for x in game_data if 'red' in x]
#print('red =', red)
#print('max red =', max(red))

sum_of_power = 0
#def get_max_value(all_games):
for game_dict in all_games:
    for game_id, game_data in game_dict.items():
        #print('game_data', game_id, 'in game_dict =', game_data)
        red = [item['red'] for item in game_data if 'red' in item]
        green = [item['green'] for item in game_data if 'green' in item]
        blue = [item['blue'] for item in game_data if 'blue' in item]
        #print('red =', red)
        #print('green =', green)
        #print('blue =', blue)
        #print('Game ', game_id, 'max red =', max(red))
        #print('Game ', game_id, 'max green =', max(green))
        #print('Game ', game_id, 'max blue =', max(blue))
        power = max(red) * max(green) * max(blue)
        #print('Power of game ', game_id, '=', power)
        sum_of_power += power

print('Sum of power of all games =', sum_of_power)

cpu_end_time = time.process_time()
end_time = time.time()
print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
print(f"CPU Execution time: {(cpu_end_time - cpu_start_time) * 1000} milliseconds")








