import time
from itertools import pairwise

t1 = time.time()

with open("input.txt") as f:
    reports = [[int(x) for x in line.split()] for line in f]

def check_data(data):
    diffs = [b - a for a, b in pairwise(data)]
    return all(0 < d <= 3 for d in diffs) or all(-3 <= d < 0 for d in diffs)

def dampener(data):
    return any(check_data(data[:i] + data[i+1:]) for i in range(len(data)))

safe_part1 = sum(check_data(report) for report in reports)
print(f"The number of safe reports for part 1 = {safe_part1}")

safe_part2 = sum(dampener(report) for report in reports)
print(f"The number of safe reports for part 2 = {safe_part2}")

t2 = time.time()
print(f"Executed in {t2 - t1:0.4f} seconds")

'''
Here's a breakdown of the improvements:

`itertools.pairwise`:** This function efficiently generates pairs of consecutive items in a list, 
making the difference calculations more concise.
* **Simplified `check_data`:** The logic for checking increasing/decreasing differences is condensed 
using `pairwise` and chained comparisons (`0 < d <= 3`).
* **Concise `dampener`:** The subset generation and checking is streamlined using a generator expression within `any(...)`.
* **`with open(...)`:** This ensures the file is properly closed even if errors occur.
* **List comprehensions:** Used for more compact list creation in `reports` and the `sum(...)` calls.
* **Minor stylistic changes:** Improved variable names and spacing for better readability.

This version achieves the same functionality as your original code but with significantly reduced verbosity and i
mproved Pythonic style. It demonstrates the power of list comprehensions, generator expressions, 
and built-in functions like `pairwise` to write more concise and efficient code.
'''
