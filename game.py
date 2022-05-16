# runs game
from ai import AI
from human import Human
from player import Player

class Game():
    def __init__(self):
      player_one = Player
      playe=Human
      notplayer=AI
      self.display_welcome()
      self.display_rules()
       # self.player_input()
      self.evaluate()

    def display_rules(self):
        print("Rules")

    def display_welcome(self):
        print("Welcome")

    def player_input(self):
        player_input = input("How many players?\nEnter 1 for AI, Enter 2 for Player vs. Player")
        if player_input == 1:
     # go to AI
            pass
        else:
            # go to pvp
            pass

    def run_game(self):
        # match will happen here
        if player_one > player_two:
            # player one gets +1 to wins
            print("Player one wins!")
        elif player_two > player_one:
            # player two gets +1 to wins
            print("Player two wins!")
        else:
            print("it's a tie")
            # loop back to play again
        pass

    def evaluate(self):
        # this function will take in player one and player two gesture inputs and declare an output (win, lose, tie)
        if user_input == 'Rock' and ai_input == 'Scissors':
            # +1 to user win
    
        'Rock' > 'Scissors'
        'Rock' > 'Lizard'
        'Scissors' > 'Paper'
        'Scissors' > 'Lizard'
        'Paper' > 'Rock'
        'Paper' > 'Spock'
        'Lizard' > 'Spock'
        'Lizard' > 'Paper'
        'Spock' > 'Rock'
        'Spock' > 'Scissors'
        

    # GESTURES
    # (Rock, Paper, Scissors, Lizard, Spock)

    # GAME RULES
    # Rock > Scissors
    # Rock > Lizard
    # Scissors > Paper
    # Scissors > Lizard
    # Paper > Rock
    # Paper > Spock
    # Lizard > Spock
    # Lizard > Paper
    # Spock > Rock
    # Spock > Scissors

    # rock = "0"
    # scissors = 1
    # lizard = 2
    # paper = 3
    # spock = 4