import time

t1 = time.time() * 1000

with open("../../2025/inputs/day3test.txt") as f:
    # Reads the file, splits lines, splits numbers, converts to int
    # All in one highly optimized pass
    data = [[int(digit) for digit in line.strip()]for line in f if line.strip()]
print(data)

# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")