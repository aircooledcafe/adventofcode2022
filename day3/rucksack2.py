file = open("input_groups.txt", "r")
data = file.read()
alphabet = open("priorities.txt", "r")
groups = data.split("\n\n")
priorities = alphabet.read().split("\n")

sum_priorities = 0
badges = []

def rucksack(group):
  rucksack = group.split("\n")
  return rucksack


def compare(group):
  rucksacks = rucksack(group)
  for item in rucksacks[0]:
    if item in rucksacks[1] and item in rucksacks[2]:
      badges.append(item)
      break


def priority_score(item):
  score = 1
  for i in priorities:
    if i == item:
      return score
    else:
      score += 1

# for group in groups:
#   rucksacks = rucksack(group)
#   for item in rucksacks[0]:
    # print(item)

for group in groups:
  compare(group)

print(badges)

for item in badges:
  sum_priorities = sum_priorities + priority_score(item)

print(len(badges))
print(sum_priorities)
# for rucksack in rucksacks:
#   compartments = compartment(rucksack)
#   print(comparison(compartments[0], compartments[1]))
#   duplicate = comparison(compartments[0], compartments[1])
#   print(priority_score(duplicate))
#   sum_priorities = sum_priorities + priority_score(duplicate)

# print(sum_priorities)
