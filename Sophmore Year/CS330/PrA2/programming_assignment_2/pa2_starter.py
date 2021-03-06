
import sys
import heapq

############################

# DO NOT CHANGE THIS PART!!

############################

def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [[float(x) for x in s.split(',')] for s in f.read().splitlines()]
    N = int(raw[0][0])
    m = int(raw[1][0])
    s = int(raw[2][0])
    adj_list = [[] for foo in range(N)]
    for edge in raw[3:]:
        adj_list[int(edge[0])].append((int(edge[1]), edge[2]))
    return N, m, s, adj_list


def writeOutput(output_file, N, s, distances, parents, mst):
    with open(output_file, 'w') as f:
        # output dijkstra
        for i in range(N):
            if i == s:
                f.write('0.0,-\n')
            else:
                f.write(str(distances[i])+','+str(parents[i])+'\n')
        
        # blank space
        f.write('\n')

        #output MST (just neighbors, no edge weights)
        for j in range(N):
            neighbors = []
            for node in mst[j]:
                neighbors.append(str(node[0]))
            # sort for the autograder
            neighbors.sort()
            f.write(','.join(neighbors) +'\n')

# 
def make_undirected_graph(N, adj_list):
    G = {}
    for u in range(N):
        G[u] ={}

    # move our stuff in
    for u in range(N):
        for v in adj_list[u]:
            G[u][v[0]] = v[1]
            G[v[0]][u] = v[1]
    #back to list
    adj_list = ['x' for x in range(N)]
    for u in range(N):
        neighbors = []
        for v in G[u].keys():
            neighbors.append((v, G[u][v]))
        adj_list[u] = list(set(neighbors))
    return adj_list





def Run(input_file, output_file):
    N, m, s, adj_list = readGraph(input_file)
    distances, parents =   dijkstra(N, m, s, adj_list)
    undirected_adj_list = make_undirected_graph(N, adj_list)
    mst = kruskal(N, m, undirected_adj_list)
    writeOutput(output_file, N, s, distances, parents, mst)


############################

# ADD YOUR OWN METHODS HERE (IF YOU'D LIKE)

############################






############################

# FINISH THESE METHODS

############################



def dijkstra(N, m, s, adj_list):
    # You are given the following variables:
    # N = number of nodes in the graph
    # m = number of edges in the graph
    # s = source node for the algorithm
    # adj_list = a list of lists of size N, where each index represents a node n
    #               the sublist at index n has a list of two-tuples,
    #               representing outgoing edges from n: (adjacent node, weight of edge)
    #               NOTE: If a node has no outgoing edges, it is represented by an empty list
    #
    # WRITE YOUR CODE HERE:
    distances = [9999]* N
    parents = ['Null']* N
    distances[s] = 0
    
    
    nodes = []
    for x in range(len(adj_list)):
        nodes.append(x)

    seen = set()
    
    
    while (len(seen) < N):
        minimum = 99999
        for x in nodes:
            if (distances[x] < minimum):
                minimum = distances[x]
                min_node = x
        seen.add(nodes.pop(nodes.index(min_node)))
        
        
        for adjacent in range(len(adj_list[min_node])):
          
            if (distances[adj_list[min_node][adjacent][0]] > distances[min_node] + adj_list[min_node][adjacent][1]):
                distances[adj_list[min_node][adjacent][0]] = distances[min_node] + adj_list[min_node][adjacent][1]
                parents[adj_list[min_node][adjacent][0]]= min_node

    # Return two lists of size N, in which each index represents a node n:
    # distances: the shortest distance from s to n
    # parents: the last (previous) node before n on the shortest path
    return distances, parents

def kruskal(N, m, undirected_adj_list):
    # You are given the following variables:
    # N = number of nodes in the graph
    # PLEASE NOTE THAT THE ADJACENCY LIST IS FORMATTED ENTIRELY DIFFERENTLY FROM DIJKSTRA ABOVE
    # undirected_adj_list = a list of lists of size N, where each index represents a node n
    #                       the sublist at index n has a list of two-tuples, representing edges from n: (adjacent node, weight of edge)
    #                       NOTE: Since the graph is undirected, each edge (u,v) is now represented twice in this adjacency list:
    #                               once at index u and once at index v
    #
    # WRITE YOUR CODE HERE:
    mst_adj_list = []
    
    

    
    
    formatted_edges = []
    for source in range(len(undirected_adj_list)):
        for index in range(len(undirected_adj_list[source])):
            formatted_edges.append((source,undirected_adj_list[source][index][0], undirected_adj_list[source][index][1]))
                
    #print(formatted_edges)  
    unique_edges = set()
    for edge in formatted_edges:
        if edge[0] < edge[1]:
            unique_edges.add(edge)
        else:
            new_edge = (edge[1], edge[0], edge[2])
            unique_edges.add(new_edge)
            
    #print(unique_edges)

    
    list_sorted = sorted(unique_edges,key=GetKey)
    #print(list_sorted)
    
    
    
    visited = []
    
    groups = []
    for x in range(N):
        groups.append(x)
    
    visited.append(list_sorted[0][0])
    for test_edge in list_sorted:
        #if find(test_edge[0]) != find(test_edge[1]):
        if (groups[test_edge[0]] != groups[test_edge[1]]):
            #print('groups', groups)
            #print('edge', test_edge)
            mst_adj_list.append(test_edge)
            original = groups[test_edge[0]]
            for x in range(len(groups)):
                if groups[x] == original:
                    #print('Index: ', x)
                    groups[x] = groups[test_edge[1]]
            #merge(test_edge[0],test_edge[1])
        



    
    Retro_formatted = [[]]*N
    for x in range(len(mst_adj_list)):
        #print('x: ', x)
        #print('H: ', mst_adj_list[x])
        #print('Retro', Retro_formatted)
        Retro_formatted[mst_adj_list[x][0]] = [(mst_adj_list[x][1], mst_adj_list[x][2])]
        Retro_formatted[mst_adj_list[x][1]] = [(mst_adj_list[x][0], mst_adj_list[x][2])]
    #print("Retro", Retro_formatted)
    

    
    #print("\n Final: ", mst_adj_list)
    mst_adj_list = Retro_formatted
    # Return the adjacency list for the MST, formatted as a list-of-lists in exactly the same way as undirected_adj_list
    return mst_adj_list


def GetKey(item):
    return item[2]

def find(node):
    pass
    
def merge(u,v):
    pass    


#############################
# CHANGE INPUT FILES FOR PART 2 HERE

#############################

def main(args=[]):
    # WHEN YOU SUBMIT TO THE AUTOGRADER, 
    # PLEASE MAKE SURE THE FOLLOWING FUNCTION LOOKS LIKE:
    # Run('input', 'output')
    Run('input', 'output')

    # AFTER YOUR RUN THE AUTOGRADER,
    # you may change comment out the above line
    # and uncomment the Run commend for the graph from part 2
    # that you wish to work on:
    
    #Run('g_randomEdges.txt', 'output')
    #Run('g_donutEdges.txt', 'output')
    #Run('g_zigzagEdges.txt', 'output')

if __name__ == "__main__":
    main(sys.argv[1:])    