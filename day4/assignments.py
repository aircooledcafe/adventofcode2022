data = open("input.txt", "r").read()
pairs = data.split("\n")

def assignment(pair):
  assignments = pair.split(",")
  return(assignments)

def dash_split(elf):
  split = elf.split("-")
  return split
  
assignment_pairs = []

for pair in pairs:
  assigned = assignment(pair)
  # print(assigned)
  temp_assignment = []
  for item in assigned:
    items = dash_split(item)
    count = 0
    for item in items:
      items[count] = int(item)
      count +=1
    temp_assignment.append(items)
  assignment_pairs.append(temp_assignment)

# print(assignment_pairs)
# print(type(assignment_pairs[0][0][0]))

contained_pairs_count = 0
overlap_count = 0

for pair in assignment_pairs:
  # print(pair[0][0])
  # print(pair[1][0])
  if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]):
    # print("Contained")
    contained_pairs_count += 1

print(contained_pairs_count)

for pair in assignment_pairs:
  if pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
    overlap_count +=1
  elif pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]:
    overlap_count += 1
  elif pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1]:
    overlap_count += 1
  elif pair[1][1] >= pair[0][0] and pair[1][1] <= pair[0][1]:
    overlap_count += 1


print(overlap_count)
