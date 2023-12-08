from game import event
import random
import game.config as config

class TreasureHunt(event.Event):
    def __init__(self):
        self.name = "Treasure Hunt Event"

    def process(self, world):
        paths = ["left", "right", "straight"]
        correct_path = random.choice(paths)

        player_choice = input("You come across a crossroads. Choose a path (left/right/straight): ").strip().lower()

        if player_choice == correct_path:
            msg = f"Congratulations! You chose the right path and found hidden treasure."
        else:
            msg = f"Oops! You chose the wrong path. No treasure this time."

        result = {}
        result["message"] = msg
        return result