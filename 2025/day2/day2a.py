import time

t1 = time.time() * 1000

data = open("../../2025/inputs/day2test.txt").read().strip().split(",")

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
    print(seq)
    for id_string in seq:
        if len(id_string) % 2 == 0:
            a, b = id_string[:len(id_string)//2], id_string[len(id_string)//2:]
            if a == b:
                print(f"True {id_string} is {a} & {b}")
                total += int(id_string)

print(f"total of all invalid IDs = {total}")

# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")
