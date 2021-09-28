# 2 human player rock, paper, scissors with nested conditionals and a cheat shield
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
print("***NO CHEATING!\n" * 50)
player2 = input("Player 2, make your move: ")
p1 = "Player 1 wins!"
p2 = "Player 2 wins!"
t = "It's a tie!"

if player1 == player2:
	print(t)
elif player1 == "rock":
	if player2 == "scissors":
		print(p1)
	elif player2 == "paper":
		print(p2)
elif player1 == "paper":
	if player2 == "rock":
		print(p1)
	elif player2 == "scissors":
		print(p2)
elif player1 == "scissors":
	if player2 == "rock":
	 	print(p2)
	elif player2 == "paper":
 		print(p1)
else:
	print("Something went wrong")
