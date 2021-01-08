
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
                neighbors.append(node[0])
            # sort for the autograder
            neighbors.sort()
            f.write(','.join([str(i) for i in neighbors]) +'\n')

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
    parents = {}
    distances[s] = 0
    solved = [(0,s)]
    parents[s] = "Null"
    seen =  {}
    
 
   # print("list ", adj_list)
   
     
    while (len(solved) > 0): 
        distance, node = heapq.heappop(solved)
        #print(node)
        #print(solved)
        #print(distances)
        seen[float(node)] = (distances[node])
        
        
    
        for adjacent in adj_list[node]:
            (adj_node, adj_distance) = adjacent
            if (distances[adj_node] > (distances[node] + adj_distance)):
                distances[adj_node] = (distances[node] + adj_distance)                
                parents[adj_node] = node
                heapq.heappush(solved, (distances[adj_node], adj_node))
                
    #print("seen: ", seen)            
    distances = seen

    sorted_keys = sorted(parents.keys())  
    Formatted_parents = [0]* N
    Formatted_distances = [0]* N
    #print("before parents: ", parents, "\n sorted_items: ", sorted_keys)
    for x in sorted_keys:
        Formatted_parents[x] = parents[x]
        Formatted_distances[x] = distances[x]
        
    parents = Formatted_parents
    distances = Formatted_distances
            
    #print("distances: ", distances, "\n parents: ", parents)
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
    
    
    to_sort = []
    
    heapq.heapify(to_sort)
    
    for x in range(len(undirected_adj_list)):
        for tuples in undirected_adj_list[x]:
            heapq.heappush(to_sort,(tuples[1],x, tuples[0])) 
    
    
    
    IDs = []
    for y in range(len(undirected_adj_list)):
        IDs.append(y)   
    
    #print("IDS: ", IDs)
    
    mst_adj_list = []
    for x in range(N):
        mst_adj_list.append([])
    
    
    #simp_ans = []
    while len(to_sort) != 0:
        edge = heapq.heappop(to_sort)
        if (find(edge[1],edge[2],IDs) == False):
            #simp_ans.append(edge)
            #print("appended: ", (edge[2], edge[0]))
            #print('\n original: ', mst_adj_list[edge[2]])
            mst_adj_list[edge[1]].append((edge[2], edge[0]))
            mst_adj_list[edge[2]].append((edge[1], edge[0]))
            merge(edge[1],edge[2],IDs)
    #print("to sort: ", to_sort)
    #print('\n original: ', undirected_adj_list)
    

    
    #print ("\n result: ", mst_adj_list)
    return mst_adj_list


def find(u,v,groups):
    if groups[u] != groups[v]:
        return False
        
    
def merge(u,v, groups):
    copy = []
    for index in (groups):
        copy.append(index)
    
    for x in range(len(copy)):
        if copy[x] == copy[u]:
            groups[x] = groups[v]
    #print("merge", u,v,groups)




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
