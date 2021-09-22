print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")
p1 = "Player 1 wins!"
p2 = "Player 2 wins!"
t = "It's a tie!"

if player1 == "Rock" and player2 == "Scissors":
	print(p1)
elif player1 == "Rock" and player2 == "Paper":
	print(p2)
elif player1 == player2:
	print(t)
elif player1 == "Paper" and player2 == "Scissors":
	print(p2)
elif player1 == "Paper" and player2 == "Rock":
	print(p1)
elif player1 == "Scissors" and player2 == "Rock":
	print(p2)
elif player1 == "Scissors" and player2 == "Paper":
	print(p1)
else:
	print("Something went wrong")