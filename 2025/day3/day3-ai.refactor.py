import time

def solve_constrained_greedy(line, length_needed):
    """
    Builds the largest possible number of 'length_needed' digits
    by greedily picking the max valid digit from left to right.
    """
    # Convert string to list of ints for easy comparison
    bank = [int(c) for c in line]
    
    current_pos = 0
    result = []
    print(f"The bank to process: {bank}")
    
    # We need to fill 'length_needed' slots
    for i in range(length_needed):
        remaining_slots_needed = (length_needed - 1) - i
        print(F"remaining slots needed: {remaining_slots_needed}")

        # Calculate the search window limit.
        # We must stop searching early enough to leave digits for the remaining slots.
        # Example: If len is 15 and we need 11 more, we can't search past index 3 (15-11=4).
        search_limit = len(bank) - remaining_slots_needed
        print(f"window size is {search_limit}, searching positions {current_pos} to {search_limit - 1}")
        
        # Extract the window we are allowed to look at
        window = bank[current_pos : search_limit]
        print(f"current window: {window}")
        
        # Find the max value in this window
        best_digit = max(window)
        
        # Add it to our result
        result.append(str(best_digit))
        print(f"result so far: {result}")
        
        # CRITICAL: Advance our current_pos.
        # We find the *first* occurrence of the best digit in the window
        # and start our next search immediately after it.
        relative_index = window.index(best_digit)
        current_pos += relative_index + 1
        
    return int("".join(result))

# --- Execution ---
t1 = time.perf_counter()

with open("../../2025/inputs/day3test.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

total_part1 = 0
total_part2 = 0

for line in lines:
    total_part1 += solve_constrained_greedy(line, 2)
    total_part2 += solve_constrained_greedy(line, 12)

t2 = time.perf_counter()

print(f"Part 1 Total: {total_part1}")
print(f"Part 2 Total: {total_part2}")
print(f"Executed in {(t2 - t1) * 1000:.3f} ms")