import random
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player score: {player_wins} Computer score: {computer_wins}")
	print ("...rock...\n...paper...\n...scissors..." )

	player = input ("Enter your choice, Player: ").lower()
	if player == "quit" or player =="q":
		break

	rand_num = random.randint(0,2)

	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"Computer plays {computer}")

	if player == computer:
		print("It is a tie!")
	elif player == "paper":
		if computer == "rock":
			print("You win!")
			player_wins += 1
		elif computer == "scissors":
			print("Computer is a winner.")
			computer_wins += 1
	elif player == "rock":
		if computer == "paper":
			print("Computer is a winner.")
			computer_wins += 1
		elif computer == "scissors":
			print("You win!")
			player_wins += 1
	elif player == "scissors":
		if computer == "paper":
			print("You win!")
			player_wins += 1
		elif computer == "rock":
			print("Computer is a winner.")
			computer_wins += 1
	elif player == computer:
		print("It is a tie!")
	else:
		print("please, write paper, rock or scissors")

print(f"FINAL SCORE: Player score: {player_wins} Computer score: {computer_wins}")
if player_wins > computer_wins:
	print("Congratulation")
elif player_wins == computer_wins:
	print("It is a tie.")
else:
	print("Computer won, try it next time")


#if player1 == "paper" and player2 == "rock":
#	print("Player1 is a winner")
#elif player1 == "rock" and player2 == "paper":
#	print("Player2 a winner")
#elif player1 == player2:
#	print("It is a tie!")
#elif player1 == "paper" and player2 == "scissors":
#	print("Player2 is a winner")
#elif player1 == "rock" and player2 == "scissors":
#	print("Player1 is a winner")
#elif player1 == "scissors" and player2 == "paper":
#	print("Player1 is a winner")
#elif player1 == "scissors" and player2 == "rock":
#	print("Player2 is a winner")
#else:
#	print("please, write paper, rock or scissors")
