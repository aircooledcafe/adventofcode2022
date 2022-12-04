data = open("input2.txt", "r").read()
output = open("input_groups.txt", "a")

rucksacks = data.split("\n")

print(rucksacks)

count = 0

for rucksack in rucksacks:
  output.write(rucksack)
  output.write("\n")
  count += 1
  if count % 3 == 0:
    output.write("\n")

