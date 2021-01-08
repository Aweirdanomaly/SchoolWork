#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *


class AIPlayer(Player):
    """ inherits attributes from Player class and makes AIPlayer objects that
    place checkers according to an algorithm"""
    def __init__(self, checker, tiebreak, lookahead):
        """asserts that certain AIPlayer attributes are in order and initializes
        'checker', 'tiebreak', and 'lookahead' """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """ takes in AIPlayer object 'self' and returns a string describing
        'self's attributes """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ takes in a AIPlayer object 'self' and a list 'scores' and returns
        the max score in that list. If there are any ties, then it returns a 
        value based on whether its on the left of the list, right, or randomly """
        l = []
        m = max(scores)
        for i in range(len(scores)):
            if scores[i] == m:
                s = [i]
                l += s
        if self.tiebreak == 'LEFT':
            return l[0]
        elif self.tiebreak == 'RIGHT':
            return l[-1]
        else:
            return random.choice(l)
        
    def scores_for(self, b):
        """ Takes in AIPlayer object 'self' and Board object 'b' and returns
        a list of scores for the columns in 'b' """
        scores = [0]* b.width
        for x in range(len(scores)):
            if b.can_add_to(x) == False:
                scores[x] = -1
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[x] = 0
            elif b.is_win_for(self.checker) == True:
                scores[x] = 100
            elif self.lookahead == 0:
                scores[x] = 50
            else:
                b.add_checker(self.checker, x)
                pp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                op_scores = pp.scores_for(b)
                if max(op_scores) == 100:
                    scores[x] = 0
                elif max(op_scores) == 0:
                    scores[x] = 100
                elif max(op_scores) == 50:
                    scores[x] = 50
                b.remove_checker(x)
        return scores
            
    def next_move(self, b):
        """ takes in AIPlayer object 'self' and Board object 'b' and returns
        the max score in the list of scores for every column in 'b' """
        w = self.scores_for(b)
        return self.max_score_column(w)
    

                