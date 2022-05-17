# runs game
from ai import AI
from human import Human
from player import Player

class Game():
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.display_welcome()
        self.display_rules()
        self.player_input()
        self.run_game()

    def display_rules(self):
        print("Rules")

    def display_welcome(self):
        print("Welcome")

    def player_input(self):
        player_input = input("How many players?\nEnter 1 for AI, Enter 2 for Player vs. Player")
        if player_input == 1:
            self.set_ai()
        else:
            self.set_opponent()

    def set_opponent(self):
        self.player_two = Human()

    def set_ai(self):
        self.player_two = AI()

    def run_game(self):
        # match will happen here
        # check rock, check paper, etc after we require input
        print(self.player_one.gestures)
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        # ai_input = self.other_player.ai_choice
        if self.player_one.chosen_gesture == self.player_one.gestures[0]:
            self.check_rock()
        elif self.player_one.chosen_gesture == self.player_one.gestures[1]:
            self.check_scissors()
        
        print(f"You chose {player_one_input} and computer chose {ai_input}")
        
        
    def check_rock(self):
        if self.player_one.chosen_gesture == self.player_one.chosen_gesture:
            print("It's a tie.")
        elif self.player_two.chosen_gesture[1]:
            self.player_one.wins + 1
        elif self.player_two.chosen_gesture == self.player_two.gestures[2]:
            self.player_one.wins + 1
        else:
            self.other_player + 1
            self.player_two.wins +1

    


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