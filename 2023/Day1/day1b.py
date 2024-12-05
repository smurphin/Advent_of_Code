import re
import time

start_time = time.time()
cpu_start_time = time.process_time()

number_map = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
#https://www.educative.io/answers/what-is-the-resub-function-in-python
def replace_written_numbers(line):
    for word, digit in number_map.items():
        #pattern = r'one|two|three|four|five|six|seven|eight|nine'
        line = re.sub(word, digit, line, flags=re.IGNORECASE)
    return line

def extract_numbers(line):
    numbers = re.findall(r'\d', line)
    if not numbers:
        return 0
    return int(numbers[0] + numbers[-1])

def process_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            print(line)
            line = replace_written_numbers(line.strip())
            value = extract_numbers(line.strip())
            print(f"Processed line: {line.strip()} -> {value}")
            total += value
    return total

# Replace 'your_file.txt' with your actual file name
filename = 'day1_input.txt'
total = process_file(filename)
print(f"Total: {total}")

cpu_end_time = time.process_time()
end_time = time.time()
print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
print(f"CPU Execution time: {(cpu_end_time - cpu_start_time) * 1000} milliseconds")
