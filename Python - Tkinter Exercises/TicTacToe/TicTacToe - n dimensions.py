# Import necessary modules
import tkinter as tk
import random

class TicTacToe:
    # Initialize the game
    def __init__(self):
        # Game state variables
        self.game_state = 1
        self.n_size = 4  # Size of the game board (4x4)
        self.players = ["X", "O"]  # Players

        # Load the game
        self.root = tk.Tk()
        self.load_assets()
        self.generate_winning_combos()
        
        # Determine the first player randomly
        self.current_player = random.choice(self.players)

    # Load the game assets and UI components
    def load_assets(self):
        self.root.title("TicTacToe v2 by Ryan")
        # self.root.geometry("800x800")

        # Main layout; container for label and restart button
        menu = tk.Frame(self.root)
        menu.pack()

        # Player turn label
        player_turn = tk.StringVar(value="XYZ")
        player_turn_label = tk.Label(menu, 
                                     font=("Arial", 24),
                                     textvariable=player_turn)
        player_turn_label.pack(pady=10)

        # Restart button
        restart_button = tk.Button(menu, text="Restart Game",
                                   font=("Arial, 16"),
                                   command=lambda: self.restart_game())
        restart_button.pack(pady=5)

        # Create game board
        game_board = tk.Frame(self.root)
        game_board.pack(padx=20,
                        pady=20,
                        fill="both",
                        expand=True)

        # Create game buttons
        n = self.n_size
        self.buttons = []
        for row in range(0, n):
            for col in range(0, n):
                index = n * row + col
                button = tk.Button(game_board, 
                                   height=8,
                                   width=15,
                                   text="",
                                   command=lambda ind=index: self.button_press(ind)) 
                button.grid(row=row,
                            column=col)
                self.buttons.append(button)

    # Handle button press events
    def button_press(self, index):
        button = self.buttons[index]

        if button['text'] == "":
            button.config(text=self.current_player)

            # Switch player
            if self.current_player == self.players[0]:
                self.current_player = self.players[1]
            elif self.current_player == self.players[1]:
                self.current_player = self.players[0]

        self.check_winner()

    # Generate winning combinations
    def generate_winning_combos(self):
        n = self.n_size
        self.win_conditions = []

        # Generate button indexes
        numbers = list(range(n ** 2))

        # Winning diagonals
        diagLR = [num for num in numbers if num % (n + 1) == 0]
        self.win_conditions.append(diagLR)

        RL = []
        for i in range(0, n):
            RL.append((i + 1) * (n - 1))
        self.win_conditions.append(RL)

        # Winning rows
        for i in range(0, n):
            rows = numbers[i * n: (i + 1) * n]
            self.win_conditions.append(rows)

        # Winning columns
        for i in range(0, n):
            cols = [num for num in numbers if num % n == i]
            self.win_conditions.append(cols)

    # Check if there is a winner
    def check_winner(self):
        n = self.n_size
        # Check all win conditions
        for condition in self.win_conditions:
            winner = [""] * n  # Initialize list for each win condition

            for i in range(0, len(condition)):
                mark = self.buttons[condition[i]]['text']
                if mark != "":
                    winner[i] = mark

            if all(element == winner[0] for element in winner) and any(element != "" for element in winner):
                self.end_game()
                return

    # End the game and disable all buttons
    def end_game(self):
        print('Game over!')

        for button in self.buttons:
            button['state'] = "disabled"

    # Restart the game
    def restart_game(self):
        for button in self.buttons:
            button['text'] = ""
            button['bg'] = "#F0F0F0"
            button['state'] = "normal"

    # Start the game loop
    def start_game(self):
        self.root.mainloop()

# Main entry point
if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()