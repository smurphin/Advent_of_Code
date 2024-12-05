import re
import time

t1 = time.time() * 1000

file = "input.txt"

data = open(file).read()
#print(data)

#create a list of strings with "mul(n,n)" 

pattern = r"mul\(\d{1,3},\d{1,3}\)"

numbers = re.findall(pattern, data)

#print(numbers)

#strip the numbers, create a list per pair and convert to integers to give a list of lists containing pairs of numbers
def format(numbers):
    new_list = []
    for str in numbers:
        #print(str)
        nums = [int(x) for x in str.replace('mul(', '').replace(')', '').split(',')]
        new_list.append(nums)
    return new_list

#calculate the total by looping through each list of pairs and multiplying the numbers together - code allows for lists longer than 2
def calc_total(number_list):    
    total = 0
    for pair in number_list:
        product = 1
        for value in pair:
            product = product * value
        #print(f"product = {product}")
        total += product
    return total

number_list = format(numbers)
#print(number_list)

total = calc_total(number_list)

print(f"Total for part 1 is = {total}")

### Part 2 ###

first_pattern = r"(.*?((?=do\(\))|(?=don't\(\))))"
include_pattern = r"(?s)(?<=do\(\)).*?(?=don't\(\))"

first_state = re.search(first_pattern, data, flags=0)#match everything up to the first "do()" or "don't()" by using re.search
#why you need to use match.group(0) from the result of re.search
#print(first_state.group(0)) #https://stackoverflow.com/questions/58151408/why-is-my-python-regex-pattern-not-matching-the-whole-string 
new_data = str(re.findall(include_pattern, data))#match all occurences after "do()"
#print(new_data)

# join first match plus all other matches
new_data = first_state.group(0) + new_data

#extract strings to be used for calculation
new_numbers = re.findall(pattern, new_data)
#print(new_numbers)

new_number_list = format(new_numbers)

new_total = calc_total(new_number_list)

print(f"Total for part 2 is = {new_total}")

# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.2f} milliseconds")