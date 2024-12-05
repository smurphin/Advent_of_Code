def get_total_calories(calorie_list):
    elfs = calorie_list.split("\n\n")
    elfs_totals = []
    for elf in elfs:
        elfs_totals.append(sum(list(map(int, elf.strip().split("\n")))))

    return elfs_totals


def get_top_3(elfs_totals):
    elfs_totals.sort()
    return elfs_totals[-3:]


with open("elfs_calories.txt") as f:
    content = f.read()

elfs_totals = get_total_calories(content)

print(sum(get_top_3(elfs_totals)))
