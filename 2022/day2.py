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

data = pd.DataFrame(input_data.replace(to_values))

data['score'] = np.where((data[0] == data[1]), data[1]+3, # draw
                    np.where((data[0] == 1) & (data[1] == 3) |
                        (data[0] == 2) & (data[1] == 1) |
                            (data[0] == 3) & (data[1] == 2), data[1], # Elf A wins
                                np.where((data[0] == 1) & (data[1] == 2) |
                                    (data[0] == 2) & (data[1] == 3) |
                                        (data[0] == 3) & (data[1] == 1), data[1]+6, # Elf B wins
                                            0)))

total = sum(data['score'])

print("Elf B's total score =", total)