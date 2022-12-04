# strategy coding
 A = "rock"
 B = "paper"
 C = "scissors"
 X = "rock"
 Y = "paper"
 Z = "scissors"

# points
rock_score = 1
paper_score = 2
scissors_score = 3

win = 6
draw = 3
loss = 0

# Possibilities
A X = draw 4 points
A Y = Y win 8 points
A Z = A  lose 3 points
B X = B  lose 1 points
B Y = draw 5 points
B Z = Z win 9 points
C X = X win 7 points
C Y = C lose 2 points
C Z = draw 6 poionts