import random

def create_board(board_type):

    board = []

    if board_type == "game":
        empty_space_char = "X"
    elif board_type == "user":
        empty_space_char = " "
    else:
        empty_space_char = "_"

    for row_num in range(0,7):
        generated_row = []
        for col_num in range(0,7):
            if row_num == 0 and col_num == 0:
                generated_row.append(" - ")
            elif row_num == 0:
                
                generated_row.append(" "+str(col_num)+" ")
            elif col_num==0:
                generated_row.append(" "+str(row_num)+" ")
            else:
                generated_row.append("["+empty_space_char+"]")
        board.append(generated_row)

    if board_type == "game":
        l_location_row = random.randint(1,6)
        l_location_col = random.randint(1,6)
        board[l_location_row][l_location_col] = " L "

        w_location_row = random.randint(1,6)
        w_location_col = random.randint(1,6)
        board[l_location_row][l_location_col] = " W "


    return board

def print_board(board):
    for row in board:
        formatted_row = ""
        for col in row:
            formatted_row += col
        print(formatted_row)

class Game:
    playing = False
    def __init__(self, score=0):
        self.score = score
        self.game_board = []
        self.user_board = []
        self.game_status = "not started"

    def display_game_home(self):
        print("")
        print("LETS PLAY SEEKER! :D")
        print("")
        start = input("PRESS ENTER TO START")
        print("")
        self.start_game()

    
    def start_game(self):
        self.game_status = "playing"
        self.game_board = create_board("game")
        self.user_board = create_board("user")
        self.get_player_turn_input()
    
    def print_game_board(self):
        print_board(self.game_board)
    
    def print_user_board(self):
        print_board(self.user_board)
    
    def get_player_turn_input(self):
        print("YOUR BOARD:")
        print("")
        game.print_user_board()
        print("")
        print("SELECT A SPACE TO PLAY. ENTER ROW AND COLUMN NUMBER.")
        print("")
        selected_row = input("SELECT A ROW: ")
        selected_col = input("SELECT A COLUMN: ")
        print("")
        print("YOU SELECTED ROW "+selected_row+" AND COLUMN "+selected_col)
        print("")
        self.play_space(int(selected_row),int(selected_col))

    def play_space(self, row, col):
        self.user_board[row][col] = self.game_board[row][col]
        if self.game_board[row][col] == " L ":
            print("OH NO - YOU GOT THE L! GAME OVER!")
            self.print_user_board()
        elif self.game_board[row][col] == " W ":
            print("YAY! YOU GOT THE W. YOU WIN!")
        else:
            print("NICE! YOU ARE SAFE...FOR THIS ROUND.")
            print("")
            self.get_player_turn_input()


game = Game()
game.display_game_home()


