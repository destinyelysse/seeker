class Game:
    playing = False
    game_board = [[]]
    user_board = [[]]
    def __init__(self, score=0):
        self.score = score
    
    def start_game(self):
        self.game_board = [[" ",1,2,3,4,5],
                           [1," "," "," "," "," "],
                           [2," "," "," "," "," "],
                           [3," "," "," "," "," "],
                           [4," "," "," "," "," "],
                           [5," "," "," "," "," "]]
        self.user_board = [[" ",1,2,3,4,5],
                           [1," "," "," "," "," "],
                           [2," "," "," "," "," "],
                           [3," "," "," "," "," "],
                           [4," "," "," "," "," "],
                           [5," "," "," "," "," "]]
   
    def print_board_square(self, char):
        if isinstance(char, int):
            print("  "+str(char)+"  ")
        else:
            print("["+char+"]")

    def print_user_board(self):
        for row in self.user_board:
            for col in row:
                self.print_board_square(col)

game = Game()
game.start_game()

print("")
print("LETS PLAY SEEKER! :D")
print("")
start = input("PRESS ANY KEY TO START")
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