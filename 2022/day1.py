with open("day1_input") as file:
    content = file.read()

elf_lists = content.split("\n\n")

elfs_calories = []

for elf in elf_lists:
    elfs_calories.append(sum(list(map(int, elf.strip().split("\n")))))


print("Total calories of the elf with the most =", max(elfs_calories))

################ Part 2 ############

elfs_calories.sort()

print("The calories of the 3 elves carrying the most =", elfs_calories[-3:])

print("Total calories of the 3 elves with the most =", sum(elfs_calories[-3:]))
