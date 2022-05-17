# give human input on gesture choices
from player import Player

class Human(Player):
    def __init__(self):
       super().__init__()
       self.wins = int()
       self.chosen_gesture = ''

    def choose_gesture(self):
        self.chosen_gesture = input("What gesture do you choose?\nFor 'Rock' choose 1\nFor 'Paper' choose 2\nFor 'Scissors' choose 3\nFor 'Lizard' choose 4\n For 'Spock' choose 5\nAnswer: ")
        if self.chosen_gesture == '1':
            return self.gestures[0]
        elif self.chosen_gesture == '2':
            return self.gestures[1]
        elif self.chosen_gesture == '3':
            return self.gestures[2]
        elif self.chosen_gesture == '4':
            return self.gestures[3]
        elif self.chosen_gesture == '5':
            return self.gestures[4]

    
    

   
       