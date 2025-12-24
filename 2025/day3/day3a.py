import time

t1 = time.time() * 1000

with open("../../2025/inputs/day3test.txt") as f:
    # Reads the file, splits lines, splits numbers, converts to int
    # All in one highly optimized pass
    data = [[int(digit) for digit in line.strip()]for line in f if line.strip()]
print(data)

def calc_joltage_pos_2(temp):
    del temp[:temp.index(max(temp)) + 1]
    joltage = str(max(temp))
    return joltage

def calc_2nd_high(temp):
    temp.remove(max(temp))
    joltage = str(max(temp))
    return joltage

total = 0

for bank in data:
    if max(bank) == bank[-1]:
        joltage2 = str(max(bank))
        joltage1 = calc_2nd_high(bank)
        total += int(joltage1 + joltage2)
        #print(f"exception joltage for bank {data.index(bank)}  = {joltage}")
    else:
        joltage1 = str(max(bank))
        joltage2 = calc_joltage_pos_2(bank)
        total += int(joltage1 + joltage2)
        #print(f"joltage for bank {data.index(bank)}  = {joltage}")

print(f"Total output joltage = {total}")

t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")

