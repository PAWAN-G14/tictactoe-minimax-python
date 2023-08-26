from Board import * 
from AI import bestMove
from os import system

class Game:
	
    # This is a class that . . . 
    # -> Sets up our Board object
    # -> Asks the users role and starts the game
    # -> Provides a method the enables the user to make make moves
    # -> Provides a method that enables the computer to make moves
    # -> Updates the status of the game and checks whether the game ended
    # -> Displays the results
    # -> Asks for rematch
    # -> Handles misinputs in all cases. 

    def __init__(self):

	# Initializes the Game.
	# Prompts the user to select a role.
	# Makes the first move of the user and the computer
	
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

	# This method enables the user to make moves
	    
	# Step 1: Draw the board.
	# Step 2: Prompt user and get move input.
	# Step 3: Check whether input is valid. If invalid, the leave a kind message and return to Step 2.
	# Step 4: After getting the valid input, make the move using Board.makeMove()
	    
        system("clear")
        self.board.draw()
        while 1:
            user_input = input("Please, input your move: ")
            if (not user_input.isdigit()) or self.board.makeMove(int(user_input)-1, self.user):
                print("Sorry, seems to be an invalid input . . . Try Again. \n")
                continue
            break

    def computerTurn(self): 
	    # Gets the best move using bestMove() function. and makes the move using Board.makeMove()
	    self.board.makeMove(bestMove(self.board.pos, not self.user), not self.user)

    def updateStatus(self): 

	# This method analyses the position, checks if the game ended and updates the results by changing self.status
	# If game ended then the results are displayed in the CLI.
	# If, self.status==2 : Game did not end
	# If, self.status==0 : Tie
	# If, self.status!=2 : Computer won. (Only computer could win.)
	
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
	    
	# This method requests the user for a rematch.
	    
	# Step 1: Request the user for a rematch.
	# Step 2: Get user input in the form of y/n.
	# Step 3: Check whether input is valid. If invalid, the leave a kind message and return to Step 2.
	# Step 4: After getting the valid input, return the appropriate boolean value i.e true for yes and false for no.
	    
        user_input = input("Would you like to have a rematch? : ")
        while 1:
            if   user_input[0].lower() == 'y': return 1
            elif user_input[0].lower() == 'n': return 0
            else: 
                print("Sorry, seems to be an invalid input . . . Try Again. ")
                continue
            break
        
