import time

t1 = time.time() * 1000
file = "input.txt"

with open(file, "r") as f:
    input = ['#' + row.replace('\n', '') + '#' for row in f.readlines()]
    ##print(data)


def add_border(data):
    formatted_data = [[]]
    for char in range(len(data[0])):
        formatted_data[0].append('#')

    for row in range(len(data)):
        formatted_data.append(list(data[row]))

    formatted_data.append([])

    for char in range(len(data[0])):
        formatted_data[-1].append('#')

    return formatted_data

def get_directions(posx, posy):

    dict = {
    "N": [[posx-1],[posy]],
    "NE": [[posx-1],[posy +1]],
    "E": [[posx],[posy+1]],
    "SE": [[posx+1],[posy+1]],
    "S": [[posx+1],[posy]],
    "SW": [[posx+1],[posy-1]],
    "W": [[posx],[posy-1]],
    "NW": [[posx-1],[posy-1]],
    }

    return dict

new_data = add_border(input)

#print(new_data)

xmas_count = 0

for row in range(1, len(new_data )):
    for col in range(1, len(new_data )):
        #print(f"Current position = {posx} {posy} char = {char}")
        if new_data[row][col] == "X":
            #print("It's an X!")
            directions = get_directions(row, col)
            for dir in directions:
                posx = row
                posy = col
                directions = get_directions(posx, posy)
                #print(f"{dir} position = {directions[dir][0][0]} {directions[dir][1][0]}")               
                if new_data[directions[dir][0][0]][directions[dir][1][0]]== "M":
                    #print("It's an M!")
                    new_posx = directions[dir][0][0]
                    #print(new_posx)
                    new_posy = directions[dir][1][0]
                    #print(new_posy)
                    directions = get_directions(new_posx, new_posy)
                    #new_pos = [new_posx, new_posy]
                    ##print(dir)
                    ##print(new_pos)
                    #print(f"{dir} position = {directions[dir][0][0]} {directions[dir][1][0]} is an {new_data[directions[dir][0][0]][directions[dir][1][0]]} " )
                    if new_data[directions[dir][0][0]][directions[dir][1][0]] == "A":
                        #print("It's an A!")
                        new_posx = directions[dir][0][0]
                        #print(f"new posx = {new_posx}")
                        new_posy = directions[dir][1][0]
                        #print(f"new posy = {new_posy}")
                        directions = get_directions(new_posx, new_posy)
                        ##print(dir)
                        ##print(new_pos)
                        #print(f"{dir} position = {directions[dir][0][0]} {directions[dir][1][0]} is an {new_data[directions[dir][0][0]][directions[dir][1][0]]} " )
                        if new_data[directions[dir][0][0]][directions[dir][1][0]] == "S":
                            #print("It's an S!")
                            new_posx = directions[dir][0][0]
                            #print(f"new posx = {new_posx}")
                            new_posy = directions[dir][1][0]
                            #print(f"new posy = {new_posy}")
                            xmas_count += 1
                
           
print(f" count of 'xmas' = {xmas_count}")

# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.2f} milliseconds")