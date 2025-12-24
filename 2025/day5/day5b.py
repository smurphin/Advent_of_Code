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
#print(ingredient_ranges)

fresh_ingredients = set()

for entry in ingredient_ranges:
    for ingredient in avail_ingredients_raw:
        if int(ingredient[0]) in range(int(entry[0]), int(entry[-1]) + 1):
            fresh_ingredients.add(int(ingredient[0]))

#print(fresh_ingredients)

ingredient_ranges = [[int(i) for i in ingredients] for ingredients in ingredient_ranges]
ingredient_ranges.sort()
#print(ingredient_ranges)

merged_ranges = []

current_start, current_end = ingredient_ranges[0]

for next_start, next_end in ingredient_ranges[1:]:    
    if next_start <= current_end +1:
        current_end = max(current_end, next_end)
        #print(f"True, current start = {current_start} current end = {current_end} ")
    else:
        merged_ranges.append([current_start, current_end])
        current_start, current_end = next_start, next_end

merged_ranges.append([current_start, current_end])

#print(f" merged ranges: {merged_ranges}")

total = len(fresh_ingredients)

fresh_ingredient_ids = 0

for entry in merged_ranges:
    fresh_ingredient_ids += entry[-1] - entry[0] + 1

print(f"Total available ingredients that are fresh: {total}")
print(f"Total fresh ingredient IDs: {fresh_ingredient_ids}")
# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")