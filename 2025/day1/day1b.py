import time

t1 = time.time() * 1000

input = open("../../2025/inputs/day1test.txt").read().strip().split("\n")

dial = 50
total = 0
passes = 0

for element in input:
    
    #print(f"dial is at position {dial}")
    
    direction = element[0]
    
    steps = int(element.strip(direction))
    #print(f"steps is {steps}")
    if direction == "L":
        if dial > 0:
            dial -= steps
            if dial < 0:
                spin = abs(dial) // 100 + 1
                passes += spin

                #print(f"passed 0, {spin} times. dial is rotated {element}, move the dial {steps} clicks, dial is now at position {dial % 100} dial = {dial}")
                dial = dial % 100
            elif dial == 0:
                total += 1
                #print(f"added 1 to total for L")
        elif dial == 0:
            dial -= steps
            spin = abs(dial) // 100
            passes += spin

            #print(f"passed 0, {spin} times. dial is rotated {element}, move the dial {steps} clicks, dial is now at position {dial % 100} dial = {dial}")
            dial = dial % 100
        else:
            dial -= steps
            dial = dial % 100
            if dial == 0:
                total += 1
                #print(f"added 1 to total for L")
        
    elif direction == "R":
        dial += steps
        if dial > 100:
            spin = dial // 100
            passes += spin

            #print(f"passed 0, {spin} times. dial is rotated {element}, move the dial {steps} clicks, dial is now at position {dial % 100} dial = {dial}")
            dial = dial % 100
        else:
            dial = dial % 100
            if dial == 0:
                total += 1
                #print(f"added 1 to total for R")

    
        
print(f"total pointing to 0: = {total}")
print(f"Total passes over 0: = {passes}")
print(f"Total times 0 clicked: = {total + passes}")

# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")