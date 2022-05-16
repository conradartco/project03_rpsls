# runs game


class Game():
    def __init__(self):
       gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
       self.display_welcome()
       self.display_rules()
       self.player_input()

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

    