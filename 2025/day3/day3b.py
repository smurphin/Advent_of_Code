import time
from collections import Counter

t1 = time.time() * 1000

with open("../../2025/inputs/day3.txt") as f:
    # Reads the file, splits lines, splits numbers, converts to int
    # All in one highly optimized pass
    data = [[int(digit) for digit in line.strip()]for line in f if line.strip()]
#print(data)

def calc_joltage_pos_2(temp):
    del temp[:temp.index(max(temp)) + 1]
    joltage = str(max(temp))
    return joltage

def calc_2nd_high(temp):
    temp.remove(max(temp))
    joltage = str(max(temp))
    return joltage

def calc_12_slot(temp):
    #high = max(temp)
    #print(f"This highest {high} at position {temp[:-12].index(high) + 1} is the start you are looking for")
    
    #print(f"new list = {temp}")
    counter = Counter(temp)
    #print(f"occurences of values in the list is {counter}")
    limit = 0
    #temp_list = []
    delete_list = sorted(counter.keys(), reverse=True)
    for key in sorted(counter.keys(), reverse=True):
        while limit < 12:          
            #print(f"there are {counter[key]} occurrences of value {key} in the list")
            limit += counter[key]
            #temp_list.append(key)
            delete_list.remove(key)
            #print(f"temp list is now {temp_list} with length {len(temp_list)} and total digits counted = {limit}")
            break
    #print(f"The only digits we need are {temp_list} and the limit is {limit}")
    #print(f"the numbers to be deleted are {delete_list}")
    for num in delete_list:
        while num in temp:
            temp.remove(num)
    #print(f"The new bank before deletions is {temp}")
    while len(temp) >12:
        temp.remove(min(temp))
    #print(f"The new bank after deletions is {temp}")
    result = int("".join(map(str, temp)))
    print(f"The value for this bank is {result}")
    return result

total = 0

for bank in data:
    if max(bank) == bank[-1]:
        joltage2 = str(max(bank))
        joltage1 = calc_2nd_high(bank)
        total += int(joltage1 + joltage2)
        #print(f"exception joltage for bank {data.index(bank)}  = {joltage1 + joltage2}")
    else:
        joltage1 = str(max(bank))
        joltage2 = calc_joltage_pos_2(bank)
        total += int(joltage1 + joltage2)
        #print(f"joltage for bank {data.index(bank)}  = {joltage1 + joltage2}")

t2 = time.time() * 1000

print(f"Total output joltage part 1 = {total}")

with open("../../2025/inputs/day3test.txt") as f:
    data = [[int(digit) for digit in line.strip()]for line in f if line.strip()]
#print(data)


total = 0
count = 0

for bank in data:
    print("-----")
    best_result = 0
    print(bank)
    high = max(bank)
    while high > 0:            
        if  high in bank and bank.index(high) <= len(bank) - 12: #Check current value of high is in the list during the loop, if not, skip it
            print(f"The highest is {high} at position {bank.index(high) + 1} this is the start you are looking for")
            bank_slice = bank[bank.index(high):]
            #print(bank)
            result = calc_12_slot(bank_slice)
            total += result
            count += 1
            
            #print(f"Total so far is {total}")
            break
        high -= 1
    print("-----")

#for bank in data:
#    best_result_for_line = 0
#    found_start = False
#    
#    # Check digits from 9 down to 0
#    for high in range(9, -1, -1):
#        if found_start: 
#            break # We found a valid start with a higher digit (e.g. 9), so we stop.
#
#        # 1. Find ALL positions of this digit, not just the first one
#        start_indices = [i for i, x in enumerate(bank) if x == high]
#        
#        # 2. Test each position to see which produces the biggest number
#        for start_index in start_indices:
#            
#            # Check length constraint
#            if len(bank) - start_index >= 12:
#                
#                # Create the slice (Copying it!)
#                current_slice = bank[start_index:] 
#                
#                # Run your filter on this specific slice
#                # Pass a copy list() because your function modifies it
#                result = calc_12_slot(list(current_slice))
#                
#                # Keep the max result seen for this line
#                if result > best_result_for_line:
#                    best_result_for_line = result
#                    found_start = True
#
#    total += best_result_for_line
#    count += 1

t3 = time.time() * 1000

print(f"Total output joltage part 2 = {total}")
print(f"Processed {count} banks")

# Calc execution time
print(f"Part 1 executed in {t2 - t1:0.3f} milliseconds")
print(f"Part 2 executed in {t3 - t2:0.3f} milliseconds")
print(f"Total executed in {t3 - t1:0.3f} milliseconds")
