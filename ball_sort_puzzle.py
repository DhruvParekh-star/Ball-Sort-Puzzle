import copy

class BallSortPuzzle:
    def __init__(self, tubes):
        self.tubes = tubes
        self.max_height = len(tubes[0])

    def display(self):
        print("\nWelcome to the Ball Sort Puzzle!")
        print("\nCurrent tubes:")
        for i, tube in enumerate(self.tubes, 1):
            print(f"Tube {i}: {tube}")
        print()

    def is_valid_move(self, from_tube, to_tube):
        if from_tube == to_tube:
            return False

        from_stack = self.tubes[from_tube]
        to_stack = self.tubes[to_tube]

        # Find top ball in from_tube
        for i in reversed(range(self.max_height)):
            if from_stack[i] != '':
                moving_ball = from_stack[i]
                break
        else:
            return False  # from_tube is empty

        # Find first empty slot in to_tube
        for j in range(self.max_height):
            if to_stack[j] == '':
                # Can only move if top of to_stack is empty or same color
                if j == 0 or to_stack[j - 1] == moving_ball:
                    return True
                else:
                    return False
        return False  # to_tube is full

    def move_ball(self, from_tube, to_tube):
        if not self.is_valid_move(from_tube, to_tube):
            print("❌ Invalid move!")
            return False

        # Remove top ball from from_tube
        for i in reversed(range(self.max_height)):
            if self.tubes[from_tube][i] != '':
                ball = self.tubes[from_tube][i]
                self.tubes[from_tube][i] = ''
                break

        # Place ball in to_tube
        for j in range(self.max_height):
            if self.tubes[to_tube][j] == '':
                self.tubes[to_tube][j] = ball
                break

        return True

    def is_solved(self):
        for tube in self.tubes:
            color = tube[0]
            if color == '':
                continue
            if any(ball != color and ball != '' for ball in tube):
                return False
        return True

def play_game():
    tubes = [
        ['Y', 'R', 'B', ''],
        ['R', 'B', 'R', ''],
        ['Y', 'G', 'G', ''],
        ['Y', 'G', 'B', '']
    ]

    game = BallSortPuzzle(copy.deepcopy(tubes))
    game.display()

    while not game.is_solved():
        try:
            from_tube = int(input("Move from tube (1-4): ")) - 1
            to_tube = int(input("Move to tube (1-4): ")) - 1
            game.move_ball(from_tube, to_tube)
            game.display()
        except (ValueError, IndexError):
            print("⚠️ Invalid input! Please enter a number between 1 and 4.")

    print("🎉 Congratulations! You've solved the Ball Sort Puzzle.")

if __name__ == "__main__":
    play_game()
