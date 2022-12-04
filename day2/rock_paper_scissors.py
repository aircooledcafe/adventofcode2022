file = open("input.txt", "r")
data = file.read()

total_score = 0

rounds = data.split("\n")

# print(rounds)

def player_score(round):
  if "X" in round:
    return 1
  elif "Y" in round:
    return 2
  elif "Z" in round:
    return 3


def round_score(round):
  if round == "A X" or round == "B Y" or round == "C Z":
    round_score = player_score(round) + 3
    return round_score
  elif round == "A Z" or round == "B X" or round == "C Y":
    round_score = player_score(round)
    return round_score
  elif round == "A Y" or round == "B Z" or round == "C X":
    round_score= player_score(round) + 6
    return round_score

for round in rounds:
  total_score = total_score + round_score(round)

print(total_score)