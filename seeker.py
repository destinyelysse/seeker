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
        print("L is at row "+str(l_location_row)+" and col "+str(l_location_col))

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
    
    def start_game(self):
        self.playing = True
        self.game_board = create_board("game")
        self.user_board = create_board("user")
    
    def print_game_board(self):
        print_board(self.game_board)
    
    def print_user_board(self):
        print_board(self.user_board)



game = Game()
game.start_game()
game.print_game_board()

print("")
print("LETS PLAY SEEKER! :D")
print("")
start = input("PRESS ENTER TO START")
print("")
print("HERE IS THE BOARD")
print("")
game.print_user_board()
print("")
selected_row = input("SELECT A ROW: ")
print("")
selected_column = input("SELECT A COLUMN: ")
print("")
print("YOU SELECTED ROW "+selected_row+" AND COLUMN "+selected_column)
print("")