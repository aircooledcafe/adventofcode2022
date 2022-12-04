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


first = 0
second = 0
third = 0

for elf in elves:
  if elf > first:
    first = elf

elves.remove(first)

for elf in elves:
  if elf > second:
    second = elf

elves.remove(second)

for elf in elves:
  if elf > third:
    third = elf

print(first)
print(second)
print(third)

total = first + second + third

print(total)