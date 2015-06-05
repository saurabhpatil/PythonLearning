# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# moves_type_list = [(0,'rock'),
                 # (1,'Spock'),
                 # (2,'paper'),
                 # (3,'lizard'),
                 # (4,'scissors')]
moves_list = ['rock','Spock','paper','lizard','scissors']

def name_to_number(name):
	move_number = [move_idx for move_idx, move in enumerate(moves_list) if move == name][0]
	#move = [move[0] for move in moves_type_list if name in move[1] ][0]
	return move_number

def number_to_name(number):
	move_name = [move for move_idx, move in enumerate(moves_list) if move_idx == number][0]
	#move_name = dict(moves_type_list)[number]
	return move_name

def rpsls(player_choice): 
	print ("Player chooses {}".format(player_choice))
	player_number = name_to_number(player_choice)
	
	computer_number = random.randrange(5)
	comp_choice = number_to_name(computer_number)
	print("Computer chooses {}".format(comp_choice))
	
	if player_number == computer_number:
		print("Player and computer tie! \n")
	elif (computer_number - player_number) % 5 > 2:
		print("Player Wins! \n")
	else:
		print("Computer Wins! \n")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


