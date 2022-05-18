# runs game
from ai import AI
from human import Human

class Game():
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.display_welcome()
        self.display_rules()
        self.player_input()
        self.run_game()

    def display_rules(self):
        print("\nThe rules are as follows:\nTwo opponents will face off and throw down their selected gesture:\nRock crushes Scissors and Lizard\nPaper covers Rock and disproves Spock\nScissors cuts Paper and decapitates Lizard\nLizard poisons Spock and eats Paper\nSpock vaporizes Rock and smashes Scissors\nA winner will be declared in the best of 3 games\n")

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")

    def player_input(self):
        self.player_choice = False
        while self.player_choice is False:
            player_input = input("How many players?\nEnter 1 for an AI opponent\nEnter 2 for Player vs. Player\nAnswer: ")
            if player_input == '1':
                self.set_ai()
                self.player_choice = True
            elif player_input == '2':
                self.set_opponent()
                self.player_choice = True
            else:
                print("Not a valid input, try again")

    def set_opponent(self):
        self.player_two = Human()

    def set_ai(self):
        self.player_two = AI()

    def run_game(self):
        self.round_counts = int(0)
        while self.player_one.wins < 3 or self.player_two.wins < 3:
            if self.player_one.wins == 3 or self.player_two.wins == 3:
                break
            self.round_counts += 1
            print(f"\nNow starting Round {int(self.round_counts)}")
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            print(f"\nPlayer One chose {self.player_one.chosen_gesture} and Player Two chose {self.player_two.chosen_gesture}")
            if self.player_one.chosen_gesture == self.player_one.gestures[0]:
                self.check_rock()
            elif self.player_one.chosen_gesture == self.player_one.gestures[1]:
                self.check_paper()
            elif self.player_one.chosen_gesture == self.player_one.gestures[2]:
                self.check_scissors()
            elif self.player_one.chosen_gesture == self.player_one.gestures[3]:
                    self.check_lizard()
            elif self.player_one.chosen_gesture == self.player_one.gestures[4]:
                self.check_spock()  
        if self.player_one.wins == 3:
            print("Player One wins the game!")
        elif self.player_two.wins == 3:
            print("Player Two wins the game!")
        
    def check_rock(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("It's a tie.")
        elif self.player_two.chosen_gesture == self.player_two.gestures[2]:
            print("Player One wins the round")
            self.player_one.wins += 1
        elif self.player_two.chosen_gesture == self.player_two.gestures[3]:
            print("Player One wins the round")
            self.player_one.wins += 1
        else:
            print("Player Two wins the round")
            self.player_two.wins += 1

    def check_paper(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("It's a tie.")
        elif self.player_two.chosen_gesture == self.player_two.gestures[0]:
            print("Player One wins the round")
            self.player_one.wins += 1
        elif self.player_two.chosen_gesture == self.player_two.gestures[4]:
            print("Player One wins the round")
            self.player_one.wins += 1
        else:
            print("Player Two wins the round")
            self.player_two.wins += 1

    def check_scissors(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("It's a tie.")
        elif self.player_two.chosen_gesture == self.player_two.gestures[1]:
            print("Player One wins the round")
            self.player_one.wins += 1
        elif self.player_two.chosen_gesture == self.player_two.gestures[3]:
            print("Player One wins the round")
            self.player_one.wins += 1
        else:
            print("Player Two wins the round")
            self.player_two.wins += 1

    def check_lizard(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("It's a tie.")
        elif self.player_two.chosen_gesture == self.player_two.gestures[1]:
            print("Player One wins the round")
            self.player_one.wins += 1
        elif self.player_two.chosen_gesture == self.player_two.gestures[4]:
            print("Player One wins the round")
            self.player_one.wins += 1
        else:
            print("Player Two wins the round")
            self.player_two.wins += 1

    def check_spock(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("It's a tie.")
        elif self.player_two.chosen_gesture == self.player_two.gestures[0]:
            print("Player One wins the round")
            self.player_one.wins += 1
        elif self.player_two.chosen_gesture == self.player_two.gestures[2]:
            print("Player One wins the round")
            self.player_one.wins += 1
        else:
            print("Player Two wins the round")
            self.player_two.wins += 1
