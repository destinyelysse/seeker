def create_board(board_type):
    board = [[]]
    if board_type == "game":
        char = "X"
    elif board_type == "user":
        char = " "
    else:
        char = "_"
    for i in range(0,7):
        row = []
        for j in range(0,7):
            if i == 0 and j == 0:
                row.append(" - ")
            elif i == 0:
                
                row.append(" "+str(j)+" ")
            elif j==0:
                row.append(" "+str(i)+" ")
            else:
                row.append("["+char+"]")
        board.append(row)
    return board

class Game:
    playing = False
    user_board = [[]]
    def __init__(self, score=0):
        self.score = score
        self.game_board = []
    
    def start_game(self):
        self.playing = True

        self.game_board = create_board("game")
        self.user_board = create_board("user")

        # self.game_board = [["-",1,2,3,4,5],
        #                    [1,"[X]","[X]","[X]","[X]","[X]"],
        #                    [2,"[X]","[X]","[X]","[X]","[X]"],
        #                    [3,"X","X","X","X","X"],
        #                    [4,"X","X","X","X","X"],
        #                    [5,"X","X","X","X","X"]]
        # self.user_board = [["-",1,2,3,4,5],
        #                    [1," "," "," "," "," "],
        #                    [2," "," "," "," "," "],
        #                    [3," "," "," "," "," "],
        #                    [4," "," "," "," "," "],
        #                    [5," "," "," "," "," "]]
   
    def format_board_square(self, char):
        if char == "-":
            return " - "
        elif isinstance(char, int):
            return " "+str(char)+" "
        else:
            return "["+char+"]"

    def print_board(self,board):
        for row in board:
            formatted_row = ""
            for col in row:
                formatted_row += col
            print(formatted_row)



game = Game()
game.start_game()
game.print_board(game.game_board)

print("")
print("LETS PLAY SEEKER! :D")
print("")
start = input("PRESS ANY KEY TO START")
print("")
print("HERE IS THE BOARD")
print("")
game.print_board(game.user_board)
print("")
selected_row = input("SELECT A ROW: ")
print("")
selected_column = input("SELECT A COLUMN: ")
print("")
print("YOU SELECTED ROW "+selected_row+" AND COLUMN "+selected_column)
print("")