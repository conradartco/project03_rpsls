# give automated input on gesture choices
import random

from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def choice(self):
        self.ai_choice = str(random.choice(self.gestures()))
        print(self.ai_choice)
