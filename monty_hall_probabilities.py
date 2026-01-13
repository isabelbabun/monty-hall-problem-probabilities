import math
import random

# what is in the chunk below will always happen in any iteration

def winning_choice_funct():
	return random.randrange(1,4)

def player_choice1_funct():
	return random.randrange(1,4)

def monty_choice_funct(winning_choice, player_choice1):
	set_of_outcomes = [1, 2, 3]
	if player_choice1 == winning_choice:
		set_of_outcomes.remove(winning_choice)
		return random.choice(set_of_outcomes)
	else:
		set_of_outcomes.remove(winning_choice)
		set_of_outcomes.remove(player_choice1)
		return set_of_outcomes[0]



# different strategies

def player_choice2_strategy1(player_choice1):
	return player_choice1

def player_choice2_strategy2(player_choice1, monty_choice):
	set_of_outcomes = [1,2,3]
	set_of_outcomes.remove(player_choice1)
	set_of_outcomes.remove(monty_choice)
	return set_of_outcomes[0]	

def player_choice2_strategy3(monty_choice):
	set_of_outcomes = [1,2,3]          				
	set_of_outcomes.remove(monty_choice)		
	return random.choice(set_of_outcomes)


# play game with strategy

def game_strategy1(attempts):
	counter = 0
	for i in range(attempts):
		winning_choice = winning_choice_funct()
		player_choice1 = player_choice1_funct()
		if player_choice1 == winning_choice:
			counter += 1
	return ("{}/{}".format(counter,attempts)) 

def game_strategy2(attempts):
	counter = 0
	for i in range(attempts):
		winning_choice = winning_choice_funct()
		player_choice1 = player_choice1_funct()
		monty_choice = monty_choice_funct(winning_choice, player_choice1)
		player_choice2 = player_choice2_strategy2(player_choice1, monty_choice)
		if player_choice2 == winning_choice:
			counter += 1
	return ("{}/{}".format(counter,attempts))

def game_strategy3(attempts):
	counter = 0
	for i in range(attempts):
		winning_choice = winning_choice_funct()
		player_choice1 = player_choice1_funct()
		monty_choice = monty_choice_funct(winning_choice, player_choice1)
		player_choice2 = player_choice2_strategy3(monty_choice)
		if player_choice2_strategy3(monty_choice) == winning_choice:
			counter += 1
	return ("{}/{}".format(counter,attempts))

print(game_strategy1(10000))
print(game_strategy2(10000))
print(game_strategy3(10000))