import time

def solve_dial():
    t1 = time.perf_counter() # Higher precision timing

    # Read input
    with open("../../2025/inputs/day1.txt") as f:
        instructions = [line.strip() for line in f if line.strip()]

    current_pos = 50
    total_zeros = 0

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:]) # Safer than strip()
        
        prev_pos = current_pos
        
        if direction == "R":
            current_pos += steps
            # Logic: How many multiples of 100 exist between prev and current?
            # Floor division (// 100) tells us which "100-block" we are in.
            # If we moved from block 0 to block 1, we crossed 100 (which is 0 on the dial).
            total_zeros += (current_pos // 100) - (prev_pos // 100)
            
        elif direction == "L":
            current_pos -= steps
            # Logic: Same concept, but we offset by -1 for Left moves.
            # This ensures that starting ON 0 and moving Left doesn't count as a "hit",
            # but moving ONTO 0 from the right does.
            total_zeros += ((prev_pos - 1) // 100) - ((current_pos - 1) // 100)

    t2 = time.perf_counter()
    
    print(f"Total times 0 clicked: {total_zeros}")
    print(f"Executed in {(t2 - t1) * 1000:.3f} milliseconds")

if __name__ == "__main__":
    solve_dial()