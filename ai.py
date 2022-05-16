# give automated input on gesture choices
import random

from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
    def choice(self):
        self.ai_choice = random.choice.self.gestures()
