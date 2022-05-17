# give human input on gesture choices
from player import Player

class Human(Player):
    def __init__(self):
       super().__init__()
       self.wins = int()
       self.chosen_gesture = ''
       self.gesture_input = False

    def choose_gesture(self):
        while self.gesture_input is False:
            self.gesture_input = input("What gesture do you choose?\nFor 'Rock' choose 1\nFor 'Paper' choose 2\nFor 'Scissors' choose 3\nFor 'Lizard' choose 4\nFor 'Spock' choose 5\nAnswer: ")
            if self.gesture_input == '1':
                self.chosen_gesture = self.gestures[0]
                self.gesture_input is True
            elif self.gesture_input == '2':
                self.chosen_gesture = self.gestures[1]
                self.gesture_input is True
            elif self.gesture_input == '3':
                self.chosen_gesture = self.gestures[2]
                self.gesture_input is True
            elif self.gesture_input == '4':
                self.chosen_gesture = self.gestures[3]
                self.gesture_input is True
            elif self.gesture_input == '5':
                self.chosen_gesture = self.gestures[4]
                self.gesture_input is True
            else:
                print('Not a valid input, try again')
            

    
    

   
       