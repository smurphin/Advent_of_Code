file = open(r"mass.txt", "r").readlines()
data = []
result = []
extrafuelresult = []
for line in file:
    data.append(int(line.strip('\n')))

for mass in data:
    fuel = (mass/3)-2
    result.append(int(fuel))
subtotal = sum(result)
print('Mass of fuel =')
print(subtotal)

for fuelmass in result:
    while fuelmass > 6:
        #print(fuelmass)
        fuelmass = (fuelmass/3)-2
        extrafuelresult.append(int(fuelmass))

total = subtotal + sum(extrafuelresult)
print('Total mass of fuel =')
print(total)
