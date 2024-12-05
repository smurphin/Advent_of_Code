
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

#print(f'List of dictionaries for each game, with a list of dictionaries, 1 for each part of the game')
#print(f'{all_games}')
#for game in all_games:
 #   print(game[0])
  #  print(game[1])

print('Games that would have been possible:')

total = 0

# print only the IDs of the games that have less than 12 red and less than 13 green and less than 14 blue
# add the ID of each game to total, then remove the ID of each game that has more than 12 red or more than 13 green or more than 14 blue ## Is this efficient?
for game_dict in all_games:
    for game_id, game_data in game_dict.items():
        total += game_id
        #print(total)
        for part in game_data:
            if part.get ('red', 0) > 12 or part.get ('green', 0) > 13 or part.get ('blue', 0) > 14:
                #print(f"Game ID : {game_id}")
                total -= game_id
                break  # Break if any part of the game meets the condition
        
print(f"Total: {total}")


cpu_end_time = time.process_time()
end_time = time.time()
print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
print(f"CPU Execution time: {(cpu_end_time - cpu_start_time) * 1000} milliseconds")








