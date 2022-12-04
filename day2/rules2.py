# strategy coding
 A = "rock"
 B = "paper"
 C = "scissors"
 X = "loose"
 Y = "draw"
 Z = "win"

# points
rock_score = 1
paper_score = 2
scissors_score = 3

win = 6
draw = 3
loss = 0

# Possibilities
A X = loose play scissors
A Y = draw play rock 
A Z = win play paper
B X = loose play rock
B Y = draw play paper
B Z = win play scissors
C X = loose play paper
C Y = draw play scissors
C Z = win play rock