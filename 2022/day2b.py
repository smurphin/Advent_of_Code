# A == X = Rock = 1
# B == Y = Paper = 2
# C == Z = Scissors = 3
#
# 1 > 3
# 2 > 1
# 3 > 2
#
#
# if a = 1 + b = 1 then score = 1 + 3 = D
# if a = 1 + b = 2 then score = 2 + 6 = B
# if a = 1 + b = 3 then score = 3 + 0 = A
#
# if a = 2 + b = 1 then score = 1 + 0 = A
# if a = 2 + b = 2 then score = 2 + 3 = D
# if a = 2 + b = 3 then score = 3 + 6 = B
#
# if a = 3 + b = 1 then score = 1 + 6 = B
# if a = 3 + b = 2 then score = 2 + 0 = A
# if a = 3 + b = 3 then score = 3 + 3 = D

# if column a and column b are == then score = value + 3 (10, 15, 20)
# if column A is bigger than column B then (14,18 or 19)
# if column A is smaller than column B then (11, 12, 16)

import pandas as pd
import numpy as np

input_data = pd.read_csv("day2_input", header=None, delim_whitespace=True)

to_values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
columns= {0: "A", 1: "B"}

data = pd.DataFrame(input_data.replace(to_values).rename((columns), axis=1))

#scores function
def calculate_scores(file, new_column, col_1, col_2):
    file[new_column] = np.where((file[col_1] == file[col_2]), file[col_2]+3, # draw
                        np.where((file[col_1] == 1) & (file[col_2] == 3) |
                            (file[col_1] == 2) & (file[col_2] == 1) |
                                (file[col_1] == 3) & (file[col_2] == 2), file[col_2], # Elf A wins
                                    np.where((file[col_1] == 1) & (file[col_2] == 2) |
                                        (file[col_1] == 2) & (file[col_2] == 3) |
                                            (file[col_1] == 3) & (file[col_2] == 1), file[col_2]+6, # Elf B wins
                                                0)))
    return file

scores = calculate_scores(data, 'score', 'A', 'B')

total = sum(data['score'])

print("Elf B's total score =", total)


################ Part 2 ############
# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3
#
# X = lose = 1
# Y = draw = 2
# Z = win = 3
#
# 1 > 3
# 2 > 1
# 3 > 2

# the plays
#  A  B 
#  1  D = 1
#  1  W = 2
#  2  L = 1
#  2  D = 2
#  2  W = 3
#  3  L = 2
#  3  D = 3
#  3  W = 1
#  1  L = 3

#play function
def plays(file, new_column, col_1, col_2):
    file[new_column] = np.where((file[col_1] == 1) & (file[col_2] == 2) |
                        (file[col_1] == 2) & (file[col_2] == 1) |
                            (file[col_1] == 3) & (file[col_2] == 3), 1, # Play a 1 (rock)
                                np.where((file[col_1] == 1) & (file[col_2] == 3) |
                                    (file[col_1] == 2) & (file[col_2] == 2) |
                                        (file[col_1] == 3) & (file[col_2] == 1), 2, # Play a 2 (paper)
                                            np.where((file[col_1] == 1) & (file[col_2] == 1) |
                                                (file[col_1] == 2) & (file[col_2] == 3) |
                                                    (file[col_1] == 3) & (file[col_2] == 2), 3, # Play a 3 (scissors)
                                                        0)))
    return file

play = plays(data, 'play', 'A', 'B')

new_score = calculate_scores(data, 'new_score', 'A', 'play')

new_total = sum(data['new_score'])

print("Elf B's new total score =", new_total)



