#         [M]     [B]             [N]
# [T]     [H]     [V] [Q]         [H]
# [Q]     [N]     [H] [W] [T]     [Q]
# [V]     [P] [F] [Q] [P] [C]     [R]
# [C]     [D] [T] [N] [N] [L] [S] [J]
# [D] [V] [W] [R] [M] [G] [R] [N] [D]
# [S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
# [N] [M] [F] [D] [R] [C] [W] [T] [M]
#  1   2   3   4   5   6   7   8   9

storage = {
  "stack1": ["N","S","D","C","V","Q","T"],
  "stack2": ["M","F","V"],
  "stack3": ["F","Q","W","D","P","N","H","M"],
  "stack4": ["D","Q","R","T","F"],
  "stack5": ["R","F","M","N","Q","H","V","B"],
  "stack6": ["C","F","G","N","P","W","Q"],
  "stack7": ["W","F","R","L","C","T"],
  "stack8": ["T","Z","N","S"],
  "stack9": ["M","S","D","J","R","Q","H","N"]
}


storage_test = {
  "stack1": ["Z", "N"],
  "stack2": ["M", "C", "D"],
  "stack3": ["P"]
}


file = open("input.txt", "r").read()

moves_raw = file.split("\n")
moves_integer = []

def obtain_digits(movement):
  temp_list = movement.split()
  integer_list = []
  integer_list.append(int(temp_list[1]))
  integer_list.append(int(temp_list[3]))
  integer_list.append(int(temp_list[5]))
  return integer_list

for item in moves_raw:
  moves_integer.append(obtain_digits(item))

def move_object(move):
  count = 0
  count2 = 0
  source_string = "stack" + str(move[1])
  dest_string = "stack" + str(move[2])
  temp_storage = []
  while count < move[0]:
    temp_storage.append(storage[source_string][len(storage[source_string]) - 1])
    # storage[dest_string].append(storage[source_string][len(storage[source_string]) - 1])
    if len(storage[source_string]) > 0:
      storage[source_string].pop(len(storage[source_string]) - 1)
      count += 1
  while count2 < move[0]:
    storage[dest_string].append(temp_storage[len(temp_storage) - 1])
    if len(temp_storage) > 0:
      temp_storage.pop(len(temp_storage) - 1)
      count2 += 1
  
  print(temp_storage)
# move_object(moves_integer[0])
# print(storage["stack1"][0])

for move in moves_integer:
  move_object(move)
print(storage)

top_item_string = ""

for key, value in storage.items():
  # print(key, value[len(value) - 1])
  top_item_string = top_item_string + value[len(value) - 1]

print(top_item_string)