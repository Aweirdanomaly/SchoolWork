# ford_fulkerson.py


import sys
from collections import deque

############################

# DO NOT CHANGE THIS PART!!

############################

def readInput(input_file):
    with open(input_file, 'r') as f:
        raw = [[int(x) for x in s.split(',')] for s in f.read().splitlines()]
        # number of vertices
        N = raw[0][0]
        # number of edges
        m =  raw[1][0]
        # source
        s = raw[2][0]
        # sink
        t = raw[3][0]
        # intervals, with name of interval as an int
        directed_edges = raw[4:]

        return N, m, s, t, directed_edges
    

def writeOutput(max_flow, output_file):
    with open(output_file, 'w') as f:
        for edge in max_flow:
            f.write(str(edge[0]) + ',' + str(edge[1]) + ',' + str(edge[2]) + '\n')


def Run(input_file, output_file):
    N, m, s, t, directed_edges = readInput(input_file)
    max_flow = ford_fulkerson(N, m, s, t, directed_edges)
    writeOutput(max_flow, output_file)


############################

# ADD YOUR OWN METHODS HERE
# (IF YOU'D LIKE)

############################
#Copied BFS from PA1
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

    Q = []
    for x in s:
        Q.append([x])
        level[x] = 0
        Traversed[x] = True
    index = 0
    
    while (len(Q[index])!= 0):
        Q.append([])
        
        for node in Q[index]:
    
          for AdjNode in adj_list[node]:
              if Traversed[AdjNode] == False:
                  Traversed[AdjNode] = True
                  Q[index+1].append(AdjNode)
                  level[AdjNode] = index + 1
        index+=1
    return level

############################

# FINISH THIS METHOD

############################

def ford_fulkerson(N, m, s, t, directed_edges):
    # You are given the following variables:
    # N - the number of vertices in the graph (INT)
    # m - the number of edges in the graph (INT)
    # s - the name of the source node (INT)
    # t - the name of the sink node (INT)
    # directed_edges: a list of lists
    # ---> Each sublist contains 3 INTs representing a directed edge in the graph:
    # ---> 0) the name of the start vertex
    # ---> 1) the name of the end vertex
    # ---> 2) the weight of the directed edge (for simplicity, this will be a positive integer!)
    print(directed_edges)




    # return a list of lists called max_flow
    # max_flow should have m sublists, one for each edge in the graph:
    # ---> Each sublist should contain 3 INTs:
    # ---> 0) the name of the start vertex
    # ---> 1) the name of the end vertex
    # ---> 2) the max flow along this directed edge
    # the edges may be placed into max_flow in any order
    
    max_flow = []
    
    return max_flow




############################################

# CHANGE INPUT FILES FOR DEBUGGING HERE

############################################

def main(args=[]):
    # WHEN YOU SUBMIT TO THE AUTOGRADER, 
    # PLEASE MAKE SURE THE FOLLOWING FUNCTION LOOKS LIKE:
    # Run('input', 'output')
    Run('input', 'output')

if __name__ == "__main__":
    main(sys.argv[1:])    

