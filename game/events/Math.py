from game import event
import random
import game.config as config

class MathEvent(event.Event):
    def __init__(self):
        self.name = "Math Puzzle Event"

    def process(self, world):
        # Ask a math puzzle to the player
        puzzle = self.generate_math_puzzle()
        player_answer = input(f"Solve the math puzzle: {puzzle['question']} ")

        # Check if the player's answer is correct
        if player_answer.strip().lower() == str(puzzle['answer']):
            msg = "Congratulations! You solved the math puzzle."
        else:
            msg = "Oops! Your answer is incorrect. Better luck next time."

        result = {}
        result["message"] = msg
        return result

    def generate_math_puzzle(self):
        # Generate a simple addition puzzle
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2

        return {'question': question, 'answer': answer}