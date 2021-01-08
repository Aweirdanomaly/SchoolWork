# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:31:26 2019

@author: Carlos
"""


class Board:
    """A class that stores the height and width of an object
    and represents it through characters in the console """
    
    def __init__(self, height, width):
        """ constructor that initializes the two attributes  
            in every Board object (height, width) """
        
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
    
    def  __repr__(self):
        """ Returns a string representation for a Board object.
        """
        num = 0
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row
            
            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
            
        for col in range((self.width *2)+1):
            s += '-'
        s += '\n'
        for col in range((self.width)):
            s += ' ' +str(num % 10)
            num += 1

        return s

    def add_checker(self, checker, col):
            """ takes in a Board object 'self', a string 'checker',
            and an int 'col' and returns the 'self' object with the 'checker'
            string on the 'col' column of itself at its first empty row """
            
            assert(checker == 'X' or checker == 'O')
            assert(0 <= col < self.width)
            row = self.height - 1
            for rows in range(self.height - 1):
                if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                    row -= 1
            self.slots[row][col] = checker
            
    def reset(self):
        """ takes in a Boasrd object 'self' and re-intializes it"""
        self.__init__(self.height, self.width)
        
        
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
            """
        checker = 'X'   # start by playing 'X'
            
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
                
                # switch to the other checker
                if checker == 'X':
                    checker = 'O'
                else:
                    checker = 'X'
    
    def can_add_to(self, col):
        """ takes in Board object 'self' and int 'col' and returns whether one
        can add a checker to a column depending on whether row 0 of that column 
        'col' is filled or not"""
        if 0 > col or col >= self.width:
            return False
        if self.slots[0][col] == 'X' or self.slots[0][col] == 'O':
            return False
        else:
            return True
        
    def is_full(self):
        """ takes in Board object 'self' and class can_add_to several times
        to see if all columns are full"""
        for col in range(self.width):
            if self.can_add_to(col) == True:
                break
            if col == self.width - 1:
                return True
        return False
        
    def remove_checker(self, col):
        """ takes in Board object 'self' and int 'col' and replaces the
        object's first instance of 'X' or 'O' in column 'col' with a ' ' """
        assert(0 <= col < self.width)
        for row in range(self.height):
            if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                self.slots[row][col] = ' '
                break
            



    def is_win_for(self, checker):
        """ Checks for four consecutive sting 'checkers' in the Board object
        'self' """
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) == True or self.is_down_diagonal_win(checker) == True\
           or self.is_up_diagonal_win(checker) == True or self.is_horizontal_win(checker) == True:
            return True
        else:
            return False
            
            
            
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker. """
        for row in range(self.height - 3):
             for col in range(self.width):
                 if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                        
                        return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for descending diagonal win for the specified checker. """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                 if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                        
                        return True
        return False
    def is_up_diagonal_win(self, checker):
        """ Checks for an ascending diagonal win for the specified checker. """
        for row in range(3,self.height):
            for col in range(self.width-3): #-3???
                 if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                        return True
        return False
    def is_horizontal_win(self, checker):
         """ Checks for a horizontal win for the specified checker.
         """
         for row in range(self.height):
             for col in range(self.width - 3):
                 # Check if the next four columns in this row
                 # contain the specified checker.
                 if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                        
                        return True

         # if we make it here, there were no horizontal wins
         return False







    
    