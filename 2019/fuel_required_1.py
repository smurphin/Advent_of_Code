file = open(r"mass.txt", "r").readlines()
data = []
result = []
for line in file:
    data.append(int(line.strip('\n')))

for mass in data:
    fuel = (mass/3)-2
    result.append(int(fuel))

print(result)

total = sum(result)
print(total)
