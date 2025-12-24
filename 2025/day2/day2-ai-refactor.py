import time

def solve_day2():
    t1 = time.perf_counter()

    # Read raw data (Don't expand ranges yet!)
    raw_ranges = open("../../2025/inputs/day2.txt").read().strip().split(",")
    
    total_part1 = 0
    total_part2 = 0

    # Process one range at a time
    for rng in raw_ranges:
        start, end = map(int, rng.split("-"))
        
        # Generator: Loop through numbers without storing them in a list
        for num in range(start, end + 1):
            s = str(num)
            length = len(s)
            
            # THE TRICK: Search for the string inside itself doubled
            # (s + s).find(s, 1) searches starting from the 2nd character
            p_len = (s + s).find(s, 1)

            # If p_len is the length of the string, it didn't find a repeat.
            if p_len < length:
                
                # Part 2: "Repeating at least twice"
                # If we found a pattern length smaller than the string, it's a repeat.
                total_part2 += num
                
                # Part 1: "Repeated EXACTLY twice"
                # If the string length is exactly 2x the pattern length
                if p_len * 2 == length:
                    total_part1 += num

    t2 = time.perf_counter()

    print(f"Part 1 Total: {total_part1}")
    print(f"Part 2 Total: {total_part2}")
    print(f"Executed in {(t2 - t1) * 1000:.3f} ms")

if __name__ == "__main__":
    solve_day2()