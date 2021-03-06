import random
import math

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number (name):
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "You have entered an invalid choice."

def number_to_name (number):
   
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "You have entered an invalid choice."

def rpsls (player_choice): 
    
    print "Player chooses", player_choice
    player_number = name_to_number (player_choice)
    
    comp_number = random.randrange (0,5)
    comp_choice = number_to_name (comp_number)
    print "Computer chooses", comp_choice 
    
    diff_choices = (comp_number - player_number) % 5
    if diff_choices == 1 or diff_choices == 2:
        print "Computer wins!\n"
    elif diff_choices == 3 or diff_choices == 4:
        print "Player wins!\n"
    else:
        print "Player and computer tie!\n"
 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
