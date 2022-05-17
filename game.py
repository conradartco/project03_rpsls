# runs game
from ai import AI
from human import Human
from player import Player

class Game():
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human()
        self.other_player = AI()
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
        # check rock, check paper, etc after we require input
        print(self.player_one.gestures)
        player_one_input = input("What gesture do you choose?\nFor 'Rock' choose 1\nFor 'Paper' choose 2\nFor 'Scissors' choose 3\nFor 'Lizard' choose 4\n For 'Spock' choose 5\nAnswer: ")
        ai_input = self.other_player.ai_choice
        if player_one_input == '1':
            self.check_rock(ai_input)
        elif player_one_input == '2':
            self.check_scissors()
        
        print(f"You chose {player_one_input} and computer chose {ai_input}")
        


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
        
    def check_rock(self, user_input, other_input):
        if user_input is 'Rock' and other_input is 'Scissors':
            self.player_one.wins + 1
        elif user_input is 'Rock' and other_input is 'Lizard':
            self.player_one.wins + 1
        elif user_input is 'Rock' and other_input is 'Rock':
            print("It's a tie.")
        else:
            self.other_player + 1

    


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