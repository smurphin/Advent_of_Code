import numpy as np
import pandas as pd

filename = 'test_input.txt'

#grid = np.random.rand(3, 3)
#print(grid)

#value = grid[0, 1]
#print(value)

#df= pd.read_fwf(filename, header=None)
#grid = df[0].str.split('', expand=True)  
#print(grid)

#row = int(input('enter row location: '))
#col = int(input('enter column location: '))
#print(row, col)
#print('the character at your location = ', grid.iloc[row, col])

#start = grid.iloc[row, col]
#grid[start].str.not.contains(".", int)

with open(filename, 'r') as file:
    input = file.read()

grid = [[i for i in line] for line in input.split('\n')]
print(grid)


print (grid[2][2])