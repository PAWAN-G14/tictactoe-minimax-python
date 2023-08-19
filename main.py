from Game import Game

run = 1                       
while run:                     # Loop in which a single game is contained
    game = Game()              # Initializing our Game Object
    while game.status==2:      # Main loop of the game
        game.userTurn()        # Asks the user to make move
        game.computerTurn()    # Computer makes a move
        game.updateStatus()    # Checks and updates the status
    run = game.askRematch()    # Asks for rematch

