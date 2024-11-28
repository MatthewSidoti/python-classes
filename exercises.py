class Game:
    def __init__(self):
        # Initialize
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        # Render the board
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        
        if self.tie:
            print("It's a tie!")
        elif self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        
        self.print_board()
        self.print_message()

    def get_move(self):
        
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                return move
            else:
                print("Invalid move. Please try again.")

    def check_for_winner(self):
        # Check all winning combinations
        combos = [
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  # rows
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  # columns
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']                       # diagonals
        ]
        for combo in combos:
            if self.board[combo[0]] and all(self.board[spot] == self.board[combo[0]] for spot in combo):
                self.winner = self.board[combo[0]]
                return

    def check_for_tie(self):
        
        if all(self.board[spot] is not None for spot in self.board) and not self.winner:
            self.tie = True

    def switch_turn(self):
        
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        # Main game
        print("Welcome to Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        # Game over
        self.render()
        print("Game over!")



if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
