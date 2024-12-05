# A == X = Rock = 1
# B == Y = Paper = 2
# C == Z = Scissors = 3
#
# 1 > 3
# 2 > 1
# 3 > 2
#
#
# if a = 1 + b = 1 then score = 1 + 3
# if a = 1 + b = 2 then score = 1 + 0
# if a = 1 + b = 3 then score = 1 + 6
#
# if a = 2 + b = 1 then score = 2 + 6
# if a = 2 + b = 2 then score = 2 + 3
# if a = 2 + b = 3 then score = 2 + 0
#
# if a = 3 + b = 1 then score = 3 + 0
# if a = 3 + b = 2 then score = 3 + 6
# if a = 3 + b = 3 then score = 3 + 3


with open("day2_input_test") as file:
    content = file.read()

rounds = content.split('\n')
print(rounds)
choice = []
to_values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
values = []

for play in rounds:
    choice.append(list(play.strip().split()))
print(choice)
#choice = [[string.replace('A', '1').replace('B', '2') for string in list] for list in choice]
for char in to_values.keys():
    choice = [[string.replace(char, to_values[char]) for string in list] for list in choice]
print(choice)
for string in choice:
    values.append(list(map(int, choice)))

print(values)




# mask_0 = (data.loc[:,0] == data.loc[:,1])
# mask_1 = ((data.loc[:,0] == 3) & (data.loc[:,1] == 1))

# data.loc[mask_0, 'score'] = (data[1]+3).apply(int)
# data.loc[mask_1, 'score'] = data[1]+6

#data.head()

convert = {
    "X": 0,
    "Y": 1,
    "Z": 2,
    "A": 0,
    "B": 1,
    "C": 2 
}
​
# First puzzle
tot = 0 
with open('second', 'r') as f:
    for line in f:
        e, y = line.strip().split(" ")
        if convert[y] == (convert[e] + 1) % 3:
            tot += convert[y] + 1 + 6
        elif convert[y] == convert[e]:
            tot += convert[y] + 1 + 3
        else:
            tot += convert[y] + 1
print(tot)
​
# Second puzzle
tot = 0 
with open('second', 'r') as f:
    for line in f:
        e, y = line.strip().split(" ")
        if y == "X":
            tot += (convert[e] - 1) % 3 + 1
        elif y == "Y":
            tot += convert[e] + 1 + 3
        else:
            tot += (convert[e] + 1) % 3 + 1 + 6
print(tot)