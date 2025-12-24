import time

t1 = time.time() * 1000

input = open("../../2025/inputs/day1.txt").read().strip().split("\n")
#print(f"elements in inputs are = {input}")
#print(f"inputs is a {type(input)}")
#print(f"elements in input are of type {type(input[0])}")

dial = 50
total = 0

for element in input:
    if dial == 0:
        total += 1
    #print(f"dial is at position {dial}")
    #print(f"element is {element}")
    direction = element[0]
    #print(f"direction is {direction}")
    steps = int(element.strip(direction))
    #print(f"steps is {steps}")
    if direction == "L":
        dial -= steps
        #print(f"dial is rotated {element}, move the dial -{steps} clicks, dial is now at position {dial % 100} dial = {dial}")
        #print(dial % 100 )
        dial = dial % 100
        
    elif direction == "R":
        dial += steps
        #print(f"dial is rotated {element}, move the dial {steps} clicks, dial is now at position {dial % 100} dial = {dial}")
        #print(dial % 100 )
        dial = dial % 100
        
print(total)

# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")