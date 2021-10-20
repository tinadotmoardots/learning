# This is a version of rock, paper, scissors that you can plan against a computer opponent
import random

player_wins = 0
computer_wins = 0

print("Rock...")
print("Paper...")
print("Scissors...")


while player_wins < 2 and computer_wins < 2:
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
	player = input("Make your move: ")
	if player == "quit" or player == "q":
		break
	rand_num = random.randint(0,2)

	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	p = "You win!"

	t = "It's a tie!"

	c = "Computer wins!"

	if player == computer:
		print(t)
	elif player == "rock":
		if computer == "scissors":
			print(p)
			player_wins += 1
		elif computer == "paper":
			print(c)
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print(p)
			player_wins += 1
		elif computer == "scissors":
			print(c)
			computer_wins += 1
	elif player == "scissors":
		if computer == "rock":
		 	print(c)
		 	computer_wins += 1
		elif computer == "paper":
	 		print(p)
	 		player_wins += 1
	else:
		print("Something went wrong")

print("Thanks for playing!")
print(f"Final score: Player {player_wins} Computer: {computer_wins}")
