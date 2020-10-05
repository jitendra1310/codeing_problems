#!/usr/bin/python3.8
'''
Let us code “The Game of Dice"
The "Game of Dice" is a multiplayer game where N players roll a 6 faced dice in a round-robin
fashion. Each time a player rolls the dice their points increase by the number (1 to 6) achieved
by the roll.

As soon as a player accumulates M points they complete the game and are assigned a rank.
Remaining players continue to play the game till they accumulate at least M points. The game
ends when all players have accumulated at least M points.

Rules of the game
- The order in which the users roll the dice is decided randomly at the start of the game.
- If a player rolls the value "6" then they immediately get another chance to roll again and move
ahead in the game.
- If a player rolls the value "1" two consecutive times then they are forced to skip their next turn
as a penalty.

Implementation Details
- Implement a standalone program in your favorite programming language which takes the
values N (number of players) and M (points of accumulate) as command line arguments.
- Name the players as Player-1 to Player-N and randomly assign the order in which they
will roll the dice.
- When it's the turn for Player-X to roll the dice prompt a message like “Player-3 its your
turn (press ‘r’ to roll the dice)
- Randomly simulate a dice roll, display the points achieved and add the points to the
user’s score.
- Print the current rank table which displays the points of all users and their rank after
each roll.
- If the user gets another chance because they rolled a ‘6’ or they are penalised because
they rolled ‘1’ twice consecutively then print appropriate message on standard output to
inform the user.
- If a user completes the game, print an appropriate message on the output displaying
their rank.
'''
from random import randint

class GameOfDice:
    player_accumulates_points_msg = "Please enter valid player accumulates points more than 10 ex. 10,13,21..etc:"
    number_of_players_msg = "Please enter valid the players more than 1 ex. 2,19 ..etc : "
    player_accumulates_points = ""
    dices = 1
    ranking = 1
    def __init__(self):
        
        # Please Enter Valid Players
        number_of_players = ""
        while(not isinstance(number_of_players, int) or number_of_players <= 1  ):
            try:
                number_of_players = input(self.number_of_players_msg)
                number_of_players = int(number_of_players)
            except ValueError:
                pass 
            
        # Get Accumulates Points                   
        while(not isinstance(self.player_accumulates_points, int) or self.player_accumulates_points <= 10  ):
            try:
                self.player_accumulates_points = int(input(self.player_accumulates_points_msg))      
            except ValueError:
                pass
            
            
        players_dict = {}
        for i in range(1,number_of_players+1):
            players_dict['Player-'+str(i)] = {'rank':0,'score':0,"dice_occurrence":[]}
        
        self.players_dict = players_dict
        self.players = list(players_dict.keys())
        
        #Start Game
        self.start_game()
        
        
    def start_game(self):       
            if(len(self.players)>1):
                for player in self.players:
                    self.get_dice_number(player)                                    
                self.print_game_rating()
                self.start_game()                
            else:
                print("\n ############ Game has Over #############!!")
                self.print_game_rating()
                
                
                
    def get_dice_number(self,player_name):
        turn_value = ""
        while turn_value !='r':
            print("\n")
            turn_value = input(player_name + " its your turn press ‘r’ to roll the dice: ")
            if turn_value == 'r':
                dice_value = 0 
                i = 0
                while ((i<self.dices) and len(self.players)>1):            
                    dice_occurrence_length = len(self.players_dict[player_name]['dice_occurrence'])
            
                    #Set 0 on the two consecutive 1
                    if(dice_occurrence_length >=2 
                    and self.players_dict[player_name]['dice_occurrence'][dice_occurrence_length-1] == 1 
                    and self.players_dict[player_name]['dice_occurrence'][dice_occurrence_length-2] == 1):
                        randint_val = 0
                    else:
                        randint_val = randint(1, 6)        
                        
                    self.players_dict[player_name]['dice_occurrence'].append(randint_val)
                    dice_value += randint_val
            
                    self.players_dict[player_name]['score']+= dice_value
                    print(player_name+" : "+ str(randint_val))
                    if(self.players_dict[player_name]['score']>= int(self.player_accumulates_points) ):
                        if (player_name in self.players): 
                            self.players.remove(player_name)
                            
                        self.players_dict[player_name]['rank'] = self.ranking
                        self.ranking = self.ranking + 1
                        if(len(self.players) == 1):
                            self.players_dict[self.players[0]]['rank'] = self.ranking 
                    # More chance on get 6
                    i = i+1
                    if (randint_val == 6):
                        self.get_dice_number(player_name)                    
                        
                        

    def print_game_rating(self):
        print("\n Player accumulates points more than or equal: "+str(self.player_accumulates_points))
        for player_key in self.players_dict:
            print(" Name: "+player_key
                  +" , \t Rating : "+str(self.players_dict[player_key]["rank"])
                  +" , \t Score : "+str(self.players_dict[player_key]["score"])
                  +" , \t Dice Occurrence : "+str(self.players_dict[player_key]["dice_occurrence"]))       

obj = GameOfDice()