import time
import re

t1 = time.time() * 1000

data = open("../../2025/inputs/day2.txt").read().strip().split(",")

id_list = []
total = 0

for string in range(len(data)):
    temp_list = data[string].split("-")
    temp_list = range(int(temp_list[0]), int(temp_list[-1]) + 1)
    new_temp_list = []
    for id_int in temp_list:
        new_temp_list.append(str((id_int)))
    id_list.append(new_temp_list)

for seq in id_list:
    #print(seq)
    for id_string in seq:
        if len(id_string) % 2 == 0:
            a, b = id_string[:len(id_string)//2], id_string[len(id_string)//2:]
            if a == b:
                #print(f"True {id_string} is {a} & {b}")
                total += int(id_string)

t2 = time.time() * 1000

print(f"total of all invalid IDs = {total}")

total = 0

for seq in id_list:
    for id_string in seq:
        counter = 1
        limit = len(id_string) // 2
        while counter < limit + 1:
            pattern = id_string[0:counter]
            match = re.search(f"^({pattern}){{2,}}$", id_string)
            if match:
                #print(f"Found match in ID: {id_string} with pattern {pattern}")
                total += int(id_string)
                break
            counter += 1

t3 = time.time() * 1000

print(f"total of all invalid IDs = {total}")

# Calc execution time
print(f"Part 1 executed in {t2 - t1:0.3f} milliseconds")
print(f"Part 2 executed in {t3 - t2:0.3f} milliseconds")
print(f"Total executed in {t3 - t1:0.3f} milliseconds")
