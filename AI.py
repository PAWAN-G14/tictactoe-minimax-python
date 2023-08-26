from Board import winLoseDraw
from functools import lru_cache

# Using functools lru_cache to cut down the time for re-evaluating identical positions
# NOTE: lru_cache is completely optional. 
#       In simple words, memory is used up to reduce time. 

@lru_cache(maxsize=None)
def minimax(pos, depth, role):
    
    # @param pos  (str  ) --> The position to be evaluated.
    # @param role (bool ) --> The role of the player, i.e X or O. 
    # @return     (float) --> Evaluation of the position.

    # End the search tree if someone won or match is drawn.
    # Here the value of win/lose is divided by depth. 
    # This is because shallow wins/loses should be given more weight than deep wins/loses in the search tree.
    # The weight or the evaluation value becomes closer to zero with increasing depth.
    status = winLoseDraw(pos)
    if status!=2: return (status*(1.0 if role else -1.0))/depth

    # Necessary variables
    evaluation = 3.0               # Here, 1.0 >= evaluation >= 0.0 . 
                                   # evaluation is set to 3.0 as an exception to dentote that no value has been set yet.
    symbol = 'x' if role else 'o'  # Converting boolean notation of the player to character

    # The loop for calculating variations by iterating through each square and making move.
    for i,v in enumerate(pos):

        # To check if a move can be made (i.e is current square empty) and a variation can be created.
        if v!=' ': continue

        # Making a move and creating a variation
        variant =  pos[:i]+symbol+pos[(i+1):]

        # Recursively calling minimax and getting the evaluation of the variation
        # The reason for the negative sign is because the evaluation returned by minimax is from opponent's POV.
        # A bad move for our opponent is a good move for us.
        child_node_eval = -minimax(variant, depth+1, not role)

        # If current evaluation is greater than the best evaluation so far, or if no evaluation has been set (i.e evaluation==3)
        # Then the current evaluation (of the current variation) is set as the best evaluation
        if evaluation<child_node_eval or evaluation==3 : evaluation = child_node_eval

    # returning the evaluation
    return evaluation


def bestMove(pos, role): 

    # This function uses the minimax() to calculate the evaluation of the primary variations
    # and finds the best move.

    # @param pos  (str ) --> The position to be analysed.
    # @param role (bool) --> The role of the player, i.e X or O. 
    # @return     (int ) --> The square in which X or O has to be placed.

    evaluation = 3
    symbol = 'x' if role else 'o'
    bestSquare = 0
    for i,v in enumerate(pos):
        if v!=' ': continue
        variant =  pos[:i]+symbol+pos[(i+1):]
        child_node_eval = -minimax(variant, 1, not role)
        if evaluation<child_node_eval or evaluation==3 : 
            evaluation = child_node_eval
            bestSquare = i 
    return bestSquare


