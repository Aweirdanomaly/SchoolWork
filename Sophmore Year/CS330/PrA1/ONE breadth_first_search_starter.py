import sys
from collections import deque
############################

# DO NOT CHANGE THIS PART!!

############################

def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [line.split(',') for line in f.read().splitlines()]

    N = int(raw[0][0])
    #s = int(raw[1])
    sin = int(raw[1])
    s = []
    for st in sin:
        s.append(int(st))
    adj_list = []
    for line in raw[2:]:
        if line == ['-']:
            adj_list.append([])
        else:
            adj_list.append([int(index) for index in line])
    return N, s, adj_list

def writeOutput(output_file, level):
    with open(output_file, 'w') as f:
        for i in level:
            f.write(str(i) + '\n')

 

def Run(input_file, output_file):
    N, s, adj_list = readGraph(input_file)
    level =   BFS(N, s, adj_list)
    writeOutput(output_file, level)


############################

# READ THIS:

############################

def  BFS(N, s, adj_list):
    # We give you three variables:
    # N = the number of vertices in the graphfile
    # s = the start node
    # adj_list = a list of lists:
    # The 0th item is a list of the vertices adjecent to vertex 0.
    # The 1st item is a list of the vertices adjecent to vertex 1.
    # The 2nd item is a list of the vertices adjecent to vertex 2.
    # And so forth.

    # We also give you a variable called level, 
    # which is a list containing N x's as placeholders:
    level = ['x']*N
    # You will write the BFS level of each node here.
    # The 0th item will be the level of vertex 0 in your BFS tree.
    # The 1st item will be the level of vertex 1.
    # Et cetera.

    # PLEASE DO NOT SUBMIT CODE WITH PRINT STATEMENTS.
    # IT WILL MESS UP THE AUTOGRADER.

    ############################

    # WRITE YOUR CODE HERE!!

    ############################
    Traversed = [False]* N
    Q = deque()
    
    Q.append(s)
    level[s] = 0
    Traversed[s] = True
    while (len(Q)!= 0):
        node = Q[0]
        Q.popleft
        
    for AdjNode in adj_list[node]:
        if Traversed[AdjNode] == False:
           Traversed[AdjNode] = True
           Q.append(AdjNode)
           level[AdjNode] = level[node] + 1
    return level

 

############################

# DO NOT CHANGE THIS PART!!

############################



def main(args=[]):
    Run('input', 'output')


if __name__ == "__main__":
    main(sys.argv[1:])    
