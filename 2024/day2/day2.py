import time

t1 = time.time()

file = "input.txt"

reports = [[int(str) for str in lst.split()] for lst in open(file).readlines()]

def check_data(data):
        
    if all(a < b for a, b in zip(data, data[1:])):# check for increasing order in report
        if all(abs(a - b) <= 3 for a, b in zip(data, data[1:])):# check that increase is no more than 3
            return True
    elif all(a > b for a, b in zip(data, data[1:])):# check for decreasing order in list
        if all(abs(a - b) <= 3 for a, b in zip(data, data[1:])):# check that decrease is no more than 3
            return True
    
    return False

safe = sum([check_data(report) for report in reports])
print((f" The number of safe reports for part 1 = {safe}"))

### part 2 ###

def dampener(data):
    for index in range(len(data)):#computes the length of the line (elements in the list) and loops through each element (index 0 -> index -1)
        new_report = data[:index] + data[index + 1:]
        #print(new_report)
        #creates new list removing one element each time the loop runs by slicing before the index ID and after the index + 1
        #data[:index] This slices the data (list) from the beginning up to (but not including) the element at index
        #data[index + 1:] This slices the data (list) from the element after index to the end.  Both slices are then joined
        safe = check_data(new_report)#checks if new_report is now safe
        if safe:
            return True
    return False
             

safe = sum([dampener(report) for report in reports])
print((f" The number of safe reports for part 2 = {safe}"))

# Calc execution time
t2 = time.time()
print(f"Executed in {t2 - t1:0.4f} seconds")