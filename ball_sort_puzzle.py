import random
import copy

class BallSortPuzzle:
    def __init__(self, num_colors=4, tube_capacity=4):
        self.num_colors = num_colors
        self.tube_capacity = tube_capacity
        self.num_tubes = num_colors + 2  # extra empty tubes
        self.tubes = self._generate_tubes()

    def _generate_tubes(self):
        colors = ['R', 'G', 'B', 'Y', 'P', 'O', 'C', 'M'][:self.num_colors]
        balls = colors * self.tube_capacity
        random.shuffle(balls)

        tubes = []
        for i in range(self.num_colors):
            tube = balls[i*self.tube_capacity:(i+1)*self.tube_capacity]
            tubes.append(tube)

        for _ in range(self.num_tubes - self.num_colors):
            tubes.append([''] * self.tube_capacity)

        return tubes

    def instructions(self):
        print("Welcome to the Ball Sort Puzzle!")
        print("\nYou have 4 tubes with colored balls.")
        print("Your goal is to sort the balls so that each tube contains only one color.")
        print("You can move the top ball from one tube to another if the destination tube is either empty or has the same color on top.")
        print("Enter the tube numbers (1-4) to move balls between them.")

    def display(self):
        print("\nCurrent tubes:")
        for i, tube in enumerate(self.tubes, 1):
            print(f"Tube {i}: {tube}")
        print()

    def is_valid_move(self, from_idx, to_idx):
        if from_idx == to_idx:
            return False

        from_tube = self.tubes[from_idx]
        to_tube = self.tubes[to_idx]

        from_top = next((i for i in reversed(range(self.tube_capacity)) if from_tube[i] != ''), None)
        if from_top is None:
            return False
        moving_ball = from_tube[from_top]

        to_top = next((i for i in range(self.tube_capacity) if to_tube[i] == ''), None)
        if to_top is None:
            return False  # to_tube is full

        return True  # allow moving to any tube with space

    def move_ball(self, from_idx, to_idx):
        if not self.is_valid_move(from_idx, to_idx):
            print("❌ Invalid move!")
            return False

        from_tube = self.tubes[from_idx]
        to_tube = self.tubes[to_idx]

        for i in reversed(range(self.tube_capacity)):
            if from_tube[i] != '':
                ball = from_tube[i]
                from_tube[i] = ''
                break

        for i in range(self.tube_capacity):
            if to_tube[i] == '':
                to_tube[i] = ball
                break

        return True

    def is_solved(self):
        for tube in self.tubes:
            if all(ball == '' for ball in tube):
                continue
            if all(ball == tube[0] and ball != '' for ball in tube):
                continue
            return False
        return True

def play_game():
    game = BallSortPuzzle()
    game.instructions()
    game.display()

    while not game.is_solved():
        try:
            from_tube = int(input("Move from tube (1-{}): ".format(game.num_tubes))) - 1
            to_tube = int(input("Move to tube (1-{}): ".format(game.num_tubes))) - 1
            game.move_ball(from_tube, to_tube)
            game.display()
        except (ValueError, IndexError):
            print("⚠️ Invalid input! Please enter valid tube numbers.")

    print("🎉 Congratulations! You’ve solved the Ball Sort Puzzle.")

if __name__ == "__main__":
    play_game()
