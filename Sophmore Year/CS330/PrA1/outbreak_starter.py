import sys
import random

############################

# DO NOT CHANGE THIS PART!!

############################

def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [line.split(',') for line in f.read().splitlines()]

    N = int(raw[0][0])
    sin = raw[1]
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

def writeOutput(output_file, prob_infect, avg_day):
    with open(output_file, 'w') as f:
        for i in prob_infect:
            f.write(str(i) + '\n')
        f.write('\n')
        for i in avg_day:
            f.write(str(i) + '\n')

 

def Run(input_file, output_file):
    N, s, adj_list = readGraph(input_file)
    prob_infect, avg_day =   model_outbreak(N, s, adj_list)
    writeOutput(output_file, prob_infect, avg_day)



def  BFS(N, s, adj_list):
    level = ['x']*N
    #######################################

    # COPY YOUR BFS CODE FROM PART 1 HERE

    ########################################
    Traversed = [False]* N
    #Not sure why s is a list but whatevs
    s = s[0]
    Q = [[s]]
    index = 0
    level[s] = 0
    Traversed[s] = True
    
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

    ############################################################

    # Le modified BFS FROM PART 1 HERE

    ########################################
    
    
def  pBFS(N, s, adj_list, p):
    level = ['x']*N
    #######################################

    # COPY YOUR BFS CODE FROM PART 1 HERE

    ########################################
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
                  x = random.uniform(0,1)
                  if (x<p):
                      Traversed[AdjNode] = True
                      Q[index+1].append(AdjNode)
                      level[AdjNode] = index + 1
        index+=1
    return level

#######################################

# WRITE YOUR SOLUTION IN THIS FUNCTION

########################################

def model_outbreak(N, s, adj_list):
    # Again, you are given N, s, and the adj_list
    # You can also call your BFS algorithm in this function,
    # or write other functions to use here.
    # Return two lists of size n, where each entry represents one vertex:
    prob_infect = [0]*N
    # the probability that each node gets infected after a run of the experiment
    avg_day = [0]*N #'inf'
    # the average day of infection for each node
    # (you can write 'inf' for infinity if the node is never infected)
    # The code will write this information to a single text file.
    # If you do not name this file at the command prompt, it will be called 'outbreak_output.txt'.
    # The first N lines of the file will have the probability infected for each node.
    # Then there will be a single space.
    # Then the following N lines will have the avg_day_infected for each node.
    days_infected = [100]*N
    p = .3
    

    
    levels = pBFS(N,s,adj_list, p)
    #print("levels:\n ", levels, "\n\n\n")
    for index in range(len(levels)):
        if (levels[index] != 'x'):    
            avg_day[index] = levels[index]
        else:
            days_infected[index] -= 1
    
        
    for iteration in range(99):
        levels = pBFS(N,s,adj_list, p)
        for index in range(len(levels)):   
            if (levels[index] != 'x'):
                avg_day[index] += levels[index]
            else:
                days_infected[index] -= 1
    

        
        
    for x in range(len(avg_day)):
        if (days_infected[x] == 0):
            avg_day[x] = 'inf'
        else:
            avg_day[x] = round(avg_day[x]/days_infected[x])
        
        prob_infect[x] = days_infected[x]/100 
        
        
    real = []
    for x in range(len(avg_day)):
        if avg_day[x] != 'inf':
             real.append(avg_day[x])
    avg_day = real
    
    print("Days:", days_infected, "\n\n\n",prob_infect, '\n Yardy:\n', avg_day)
    prob_infect.sort(reverse=True)
    return prob_infect, avg_day
############################

# DO NOT CHANGE THIS PART!!

############################


# read command line arguments and then run
def main(args=[]):
    filenames = []

    #graph file
    if len(args)>0:
        filenames.append(args[0])
        input_file = filenames[0]
    else:
        print()
        print('ERROR: Please enter file names on the command line:')
        print('>> python outbreak.py graph_file.txt output_file.txt')
        print()
        return

    # output file
    if len(args)>1:
        filenames.append(args[1])
    else:
        filenames.append('outbreak_output.txt')
    output_file = filenames[1]

    Run(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])    
