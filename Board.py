def winLoseDraw(pos):
	
    # @param  pos         (string) --> Input position.
    # @return winLoseDraw (int)    --> winner/loser/drawn/not final position.
    # If returns,  1: X wins
    # If returns, -1: O wins
    # If returns,  0: Tie 
    # If returns,  2: ERROR_CODE for Game did not end.

    rowsColsDiags = [       
                        pos[0]+pos[1]+pos[2],          
                        pos[3]+pos[4]+pos[5],
                        pos[6]+pos[7]+pos[8],
                        pos[0]+pos[4]+pos[8],
                        pos[2]+pos[4]+pos[6],   
                        pos[0]+pos[3]+pos[6],
                        pos[1]+pos[4]+pos[7],    
                        pos[2]+pos[5]+pos[8]
                    ]   
    if   "xxx" in rowsColsDiags: return  1;
    elif "ooo" in rowsColsDiags: return -1;
    elif  ' ' in pos :           return  2;
    return 0;

class Board:

    # This is a class that . . .
    # -> Sets up the board with initial position
    # -> Provides a function for making moves
    # -> Provides a function for drawing the board in the CLI.

    def __init__(self): 
	    # Setting up an empty board in the form of a string.
	    self.pos = "         "

    def makeMove(self, square, role):
	# Placing 'x' or 'o' in the said square.
	# If square invalid then return 1 for error, else return 0 for success.
        if square<0 or square>8 or self.pos[square]!=' ': return 1
        self.pos = self.pos[:square]+('x' if role else 'o')+self.pos[(square+1):]
        return 0

    def draw(self):
	# Draw the board with the current position.
        print('')
        print(f"\t   |   |\n\t {self.pos[0]} | {self.pos[1]} | {self.pos[2]}\n\t   |   |\n",
               "\t===========\n",
              f"\t   |   |\n\t {self.pos[3]} | {self.pos[4]} | {self.pos[5]}\n\t   |   |\n",
               "\t===========\n",
              f"\t   |   |\n\t {self.pos[6]} | {self.pos[7]} | {self.pos[8]}\n\t   |   |\n")


