file = open("elves_calories.txt", "r")

data = file.read()

elves = []

groups = data.split("\n\n")
# print(groups)

for elf in groups:
  calories = elf.split("\n")
  total = 0
  for c in calories:
    # print(c)
    # print(type(c))
    total = total + int(c)
  elves.append(total)


highest = 0

for elf in elves:
  if elf > highest:
    highest = elf

print(highest)