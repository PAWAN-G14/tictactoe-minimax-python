from Board import * 
from AI import bestMove
from os import system

class Game:
	
    # This is a class that . . . 
    # -> Sets up our Board object
    # -> Asks the users role and starts the game
    # -> Provides a function the enables the user to make make moves
    # -> Provides a function that enables the computer to make moves
    # -> Updates the status of the game and checks whether the game ended
    # -> Displays the results
    # -> Asks for rematch
    # -> Handles misinputs in all cases. 

    def __init__(self):
        self.board  = Board()
        self.status = 2
        while 1:
            user_input = input("Which would you prefer being, X or O ? : ")
            if   user_input[0].lower()=='x': self.user = 1
            elif user_input[0].lower()=='o': self.user = 0
            else:
                print("Sorry, seems to be an invalid input . . . Try Again. \n")
                continue
            break

        if self.user: self.userTurn()
        self.computerTurn()    

    def userTurn(self):
        system("clear")
        self.board.draw()
        while 1:
            user_input = input("Please, input your move: ")
            if (not user_input.isdigit()) or self.board.makeMove(int(user_input)-1, self.user):
                print("Sorry, seems to be an invalid input . . . Try Again. \n")
                continue
            break

    def computerTurn(self): self.board.makeMove(bestMove(self.board.pos, not self.user), not self.user)

    def updateStatus(self): 
        self.status = winLoseDraw(self.board.pos)
        if   self.status==2: pass
        elif self.status==0:
            system("clear")
            self.board.draw()
            print("It's a TIE!\n")
        else:
            system("clear")
            self.board.draw()
            print("Computer Wins . . . Better luck next time")
    
    def askRematch(self):
        user_input = input("Would you like to have a rematch? : ")
        while 1:
            if   user_input[0].lower() == 'y': return 1
            elif user_input[0].lower() == 'n': return 0
            else: 
                print("Sorry, seems to be an invalid input . . . Try Again. ")
                continue
            break
        


