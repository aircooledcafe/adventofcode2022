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

def rock(round):
  if "A" in round:
    return 4
  elif "B" in round:
    return 1
  elif "C" in round:
    return 7

def paper(round):
  if "A" in round:
    return 8
  elif "B" in round:
    return 5
  elif "C" in round:
    return 2

def scissors(round):
  if "A" in round:
    return 3
  elif "B" in round:
    return 9
  elif "C" in round:
    return 6

def round_score(round):
  if round == "A Y" or round == "B X" or round == "C Z":
    return rock(round)
  elif round == "A Z" or round == "B Y" or round == "C X":
    return paper(round)
  elif round == "A X" or round == "B Z" or round == "C Y":
    return scissors(round)


for round in rounds:
  total_score = total_score + round_score(round)

print(total_score)