file = open("input.txt", "r")
data = file.read()
alphabet = open("priorities.txt", "r")

rucksacks = data.split("\n")

priorities = alphabet.read().split("\n")
# print(rucksacks)

sum_priorities = 0

def compartment(rucksack):
  split_point = int(len(rucksack) / 2)
  left, right = rucksack[:split_point], rucksack[split_point:]
  return left, right

for rucksack in rucksacks:
  print(compartment(rucksack))

def comparison(left, right):
  for item in left:
    if item in right:
      return item

def comparison_right(left, right):
  for item in right:
    if item in left:
      return item

# for rucksack in rucksacks:
#   compartments = compartment(rucksack)
#   print(comparison_right(compartments[0], compartments[1]))

print(priorities)

def priority_score(item):
  score = 1
  for i in priorities:
    if i == item:
      return score
    else:
      score += 1

for rucksack in rucksacks:
  compartments = compartment(rucksack)
  print(comparison(compartments[0], compartments[1]))
  duplicate = comparison(compartments[0], compartments[1])
  print(priority_score(duplicate))
  sum_priorities = sum_priorities + priority_score(duplicate)

print(sum_priorities)
