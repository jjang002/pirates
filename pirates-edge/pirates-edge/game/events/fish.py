#Empty py intended as a suggestion for a type of event a student could add. For ease of merging, students should append their names or other id to this py and any classes, to reduce conflicts.
from game import event
import random
import game.config as config

class FishingEvent(event.Event):
    def __init__(self):
        self.name = "Fishing Event"

    def process(self, world):
        fish_types = ["Salmon", "Trout", "Bass"]
        caught_fish = random.choice(fish_types)
        input("You find a peaceful spot by the water to fish. Press Enter to cast your line...")

        msg = f"You caught a {caught_fish}!"


        result = {}
        result["message"] = msg
        return result
