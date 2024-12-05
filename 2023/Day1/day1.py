import re

def extract_numbers(line):
    numbers = re.findall(r'\d', line)
    if not numbers:
        return 0
    return int(numbers[0] + numbers[-1])

def process_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            value = extract_numbers(line.strip())
            print(f"Processed line: {line.strip()} -> {value}")
            total += value
    return total

# Replace 'your_file.txt' with your actual file name
filename = 'day1_input.txt'
total = process_file(filename)
print(f"Total: {total}")
