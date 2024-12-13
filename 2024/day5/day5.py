import time
import math

t1 = time.time() * 1000
file = "input.txt"

with open(file, "r") as f:
    input = [row.replace('\n', '') for row in f.readlines()]

rule_pairs = []
updates = []
rule_dict = {}

for list in range(len(input)):
    if "|" in input[list]:
        rule_pairs.append(input[list].split("|"))
        for string in range(len(rule_pairs[list])):
            rule_pairs[list][string] = int(rule_pairs[list][string])
    else:
        updates.append(input[list].split(", "))

for pair in rule_pairs:
    if pair[0] in rule_dict:
        rule_dict[pair[0]].append(pair[1])
    else:
        rule_dict[pair[0]] = [pair[1]]

updates.remove(updates[0])

for list in range(len(updates)):
        updates[list] = [int(string) for string in updates[list][0].split(",")]

#print(f"List of rules length = {len(rule_pairs)} = {rule_pairs}")
#print(f"list of updates {updates}")
#print(f"Rule dictionary = {rule_dict}")

def correct_order():
    
    for page in range(len(list)):
        if list[page] in rule_dict:
            for rule in range(page +1, len(list)):
                if list[rule] not in rule_dict[list[page]]:
                    return False
    if list[-1] in rule_dict:
        for rule in range(0, len(list) -1):
            if list[rule] in rule_dict[list[page]]:
                    return False       
            
    return True

sum = 0
incorrect = []

for list in updates:
    correct = (correct_order())
    if correct is True:
        middle_page = list[math.ceil(len(list) / 2) -1]
        sum += middle_page
    else:
        incorrect.append(list)
        

print(f"Total for part 1 = {sum}")

for list in incorrect:
    for page in range(len(list)):
        if list[page] in rule_dict:
            for rule in range(page +1, len(list)):
                if list[rule] not in rule_dict[list[page]]:
                    if list[rule] in rule_dict:
                        if list[page] in rule_dict[list[rule]]:
                            page_id = list[rule]
                            list.pop(rule)
                            list.insert(page, page_id)
        else:
            page_id = list[page]
            list.pop(page)
            list.append(page_id)

new_sum = 0
for list in incorrect:
    new_middle_page = list[math.ceil(len(list) / 2) -1]
    new_sum += new_middle_page

print(f"Total for part 2 = {new_sum}")

# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")
print(f"Executed in {(t2 / 1000) - (t1 / 1000):0.4f} seconds")