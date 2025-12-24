import time

def get_neighbors(r, c, grid):
    # Returns a list of the 8 neighbor values
    # Because of your border, we don't need boundary checks!
    neighbors = [
        grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1],
        grid[r][c-1],                 grid[r][c+1],
        grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1]
    ]
    return neighbors

def solve_day4():
    t1 = time.perf_counter()

    with open("../../2025/inputs/day4.txt") as f:
        # Create grid with '#' border immediately
        raw_lines = [list(line.strip()) for line in f if line.strip()]
        
    width = len(raw_lines[0])
    # Add top/bottom borders
    border_row = ['#'] * (width + 2)
    grid = [border_row] + [['#'] + line + ['#'] for line in raw_lines] + [border_row]

    total_removed = 0
    continue_loop = True

    while continue_loop:
        continue_loop = False
        
        # Enumerate gives us r (row index) and c (col index) automatically
        for r, row in enumerate(grid):
            for c, symbol in enumerate(row):
                
                # Use 'in' to skip non-targets
                if symbol in '#.x':
                    continue
                
                # If we are here, symbol is '@'
                neighbors = get_neighbors(r, c, grid)
                
                if neighbors.count('@') < 4:
                    # Mark for removal
                    # CAUTION: We can't change it to 'x' instantly inside the loop
                    # or it might affect the count for the next neighbor in this same pass.
                    # We usually collect them and change them after the loop.
                    # BUT, your logic seemed to want a cascade, so let's stick to your logic.
                    
                    grid[r][c] = 'x' # Immediate removal
                    total_removed += 1
                    continue_loop = True

    t2 = time.perf_counter()
    print(f"Total Part 2: {total_removed}")
    print(f"Executed in {(t2 - t1) * 1000:.3f} ms")

if __name__ == "__main__":
    solve_day4()