#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###
def mult_row(matrix, r, m):
    """ takes in input 2-D list 'matrix', row int 'r', and constant 'm'
    and multiplies every element in row 'r' in 'matrix' by 'm' """
    for c in range(len(matrix[r])):
        matrix[r][c] *= m 
        
def add_row_into(matrix, source, dest):
    """ takes in input 2-D list 'matrix', row int 'source', and row int
    'dest' and adds every element in row 'src' in to row 'dest' """
    for c in range(len(matrix[dest])):
        matrix[dest][c] += matrix[source][c]
        
def add_mult_row_into(matrix, m, source, dest):
     """ takes in input 2-D list 'matrix', row int 'source', row int 
     'dest', and int 'm' and adds every element in row 'src' 
     multiplied by m to row 'dest' """
     a = matrix [source][:]
     mult_row(matrix, source, m)
     add_row_into(matrix, source, dest)
     matrix [source]= a
     
def create_matrix(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    matrix = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        matrix += [row]

    return matrix

def transpose(matrix):
    """ takes in input 2-D list 'matrix' and switches its rows with its
    columns and vice versa"""
    matrix_temp = create_matrix(len(matrix[0]), len(matrix))
    for r in range(len(matrix_temp)):
        for c in range(len(matrix_temp[0])):
            matrix_temp[r][c] = matrix[c][r]
    return matrix_temp

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)

        ## add code to handle the other options here
        elif choice == 2:
            row = int(input('Choose a row: '))
            mult_by = float(input("Enter the number you'd like to multiply by: "))
            mult_row(matrix, row, mult_by)
        elif choice == 3:
            src = int(input('Index of source row:'))
            dest = int(input('Index of destination row:'))
            add_row_into(matrix, src, dest)
        elif choice == 4:
            src = int(input('Index of source row:'))
            mult_by = float(input("Multiplier: "))
            dest = int(input('Index of destination row:'))
            add_mult_row_into(matrix, mult_by, src, dest)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
            
