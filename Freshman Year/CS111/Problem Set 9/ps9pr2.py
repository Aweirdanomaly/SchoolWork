#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    """ A class that creates an object 'Player' with a string 'checker'
    representing the Player's checker type and the number of moves he's
    done so far shown by an int 'num_moves' """
    
    def __init__(self, checker):
        """ constructor that initializes the two attributes  
            in every Player object, checker and num_moves """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns the checker type of the player in string format """
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        """ takes in the checker type for a Player object and returns the 
        opposite checker type which represents the opponent's checker """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ Get a next move for the player that is valid
        for the board b. """

       
        self.num_moves += 1
        while True:
            line = int(input('Enter a column: '))
            if b.can_add_to(line) == True:
                break
            else:
                print('Try again!')
        return line
            
            