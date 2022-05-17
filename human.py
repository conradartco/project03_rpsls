# give human input on gesture choices
from player import Player

class Human(Player):
    def __init__(self,wins):
       super().__init__()
       self.wins = wins
       self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    
    def player_vs_player(self):    
       pass

    def check_gesture(self, input_1, input_2):
        if input_1 == input_2:
            print("It's a tie")
        elif input_1 == 'Rock':
            if input_2 == 'Scissors':
                print("You win")
            else:
                print("You lose")
        elif input_1
       