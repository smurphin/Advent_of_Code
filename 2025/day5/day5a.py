import time

t1 = time.time() * 1000

with open("../../2025/inputs/day5.txt") as f:
    data = [[line.strip()]for line in f]
    
data_split = data.index([''])
ingredient_ranges_raw = data[: data_split]
avail_ingredients_raw = data[data_split + 1 :]
#print(ingredient_ranges_raw)
#print(avail_ingredients_raw)

ingredient_ranges = []

for string in ingredient_ranges_raw:
    ingredient_ranges.append(string[0].split("-"))

fresh_ingredients = set()

for entry in ingredient_ranges:
    for ingredient in avail_ingredients_raw:
        if int(ingredient[0]) in range(int(entry[0]), int(entry[-1]) + 1):
            fresh_ingredients.add(int(ingredient[0]))

#print(fresh_ingredients)

total = len(fresh_ingredients)

print(f"Total available ingredients that are fresh: {total}")
# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")