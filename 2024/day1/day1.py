import pandas as pd
from collections import Counter
import time

t1 = time.time()

csv_file = "input.txt"

df = pd.read_csv(csv_file, header=None, sep='\s+', names=['A', 'B'])

list_A = list(df['A'])
list_B = list(df['B'])

#calculate difference between number A & B per row, add the value to the distance, then remove the numbers from the list.
distance = 0
while len(list_A) >0:
    sum = abs((min(list_A ))-(min(list_B ))) 
    if sum >0:
        distance += sum
    list_A.remove(min(list_A))
    list_B.remove(min(list_B))

print(f"distance = {distance}")

# Calc execution time
t2 = time.time()


### part B ####

#count occurences of number in list B and create a dictionary using "Counter", then multiply each number in list_A by the number of times it appears in list B.

list_A = list(df['A'])
list_B = list(df['B'])

count = Counter(list_B)

similarity = 0

for i in list_A:
    similarity += i * count[i]

print(f"similarity is {similarity}")

# Calc execution time
t3 = time.time()
print(f"Part 1 executed in {t2 - t1:0.4f} seconds")
print(f"Part 2 executed in {t3 - t2:0.4f} seconds")
print(f"Total execution time {t3 - t1:0.4f} seconds")

