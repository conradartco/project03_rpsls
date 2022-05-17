# give automated input on gesture choices
import random

from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        self.wins = int()
        self.chosen_gesture = ''

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        
