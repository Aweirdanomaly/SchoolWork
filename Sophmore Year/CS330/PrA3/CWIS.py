# Hannah Catabia, catabia@bu.edu
# Solution code for PA2, CS330 Fall 2020
# Adapted from:
# Gavin Brown, grbrown@bu.edu
# CS330 Fall 2019, Programming Exercise Solution 


import heapq
import sys


############################

# DO NOT CHANGE THIS PART!!

############################

def readInput(input_file):
    with open(input_file, 'r') as f:
        raw = [[float(x) for x in s.split(',')] for s in f.read().splitlines()]
        # number of intervals
        N = int(raw[0][0])
        # max number to schedule
        k =  int(raw[1][0])
        # intervals, with name of interval as an int
        intervals = raw[2:]

        for i in range(len(intervals)):
            intervals[i][0] = int(intervals[i][0])
        return N, k, intervals
    

def writeOutput(schedule, output_file):
    with open(output_file, 'w') as f:
        for i in schedule:
            f.write(str(i) + '\n')


def Run(input_file, output_file):
    N, k, intervals = readInput(input_file)
    schedule = find_solution(N, k, intervals)
    assert all(isinstance(n, int) for n in schedule), "All items in schedule array should be type INT, otherwise the autograder will fail."
    writeOutput(schedule, output_file)


############################

# ADD YOUR OWN METHODS HERE
# (IF YOU'D LIKE)

############################
def Calculate_p(sorted_intervals):
    #pjs = []
   # print("\n", sorted_intervals)
    for interval in range(len(sorted_intervals)):
        x = interval
        #print("\n \n \n interval", sorted_intervals[interval], "\n \n \n")
        while True:
            x-=1
            if (x < 0):
                sorted_intervals[interval] = (sorted_intervals[interval][0], sorted_intervals[interval][1], sorted_intervals[interval][2], sorted_intervals[interval][3], -1) #was "Null"
                #pjs.append(('Null'))
                break
            if (sorted_intervals[x][0] <= sorted_intervals[interval][1]):
                sorted_intervals[interval] = (sorted_intervals[interval][0], sorted_intervals[interval][1], sorted_intervals[interval][2], sorted_intervals[interval][3], sorted_intervals[x][2])
                #pjs.append((sorted_intervals[x][2]))
                break
    
    return sorted_intervals
    #return pjs
    
def LocateP(p, intervals):
    #print("ordinary",p)
    #print("if you",intervals)
    for x in range(1, len(intervals)):
        #print("place", intervals[x][4])
        if intervals[x][2] == p:
            return x
    return 0

############################

# FINISH THESE METHODS

############################

def find_solution(N, k, intervals):
    # You are given the following variables:
    # N - the total number of intervals
    # k - the max number of intervals you can put on your schedule
    # intervals - a list of lists
    # ---> Each sublist in intervals has 4 items representing one interval:
    # ---> 0) an INT that is the NAME of the interval
    # ---> 1) a float that is the start time of the interval
    # ---> 2) a float that is the end time of the interval
    # ---> 3) a float that is the weight of an interval
    
    
    #sort without making p(j)
    sorted_intervals = []
    heapq.heapify(sorted_intervals)
    for interval in intervals:
        heapq.heappush(sorted_intervals,(interval[2], interval[1], interval[0], interval[3] )) #format: end, beginning, ID, weight, (future pjs)
    
    
    #put heap into array
    sorted_array = []
    while len(sorted_intervals) != 0:
        sorted_array.append(heapq.heappop(sorted_intervals))
        
    #print('sorted aray: ', sorted_array)
    
    
    #Calculate  and add p(j) to array
    Calculate_p(sorted_array)
    
    #print("\n \n \n sorted array", sorted_array, "\n \n \n")
    
    
    #Start of pseudocode translation
    p=[]
    for x in sorted_array:
        p.append(x[4])
    p.insert(0,-2)
    
    sorted_array.insert(0, -2)
        
    
    M = [[0 for x in range(k+1)]for y in range(N+1)]
    B = [[0 for x in range(k+1)]for y in range(N+1)]
    


    for i in range(1, N+1): 
        for j in range(1, k+1):

            weight = sorted_array[i][3]
            
            location = LocateP(p[i] ,sorted_array)


            if (((weight)+ M[location][j-1]) > M[i-1][j]):
                
                M[i][j] = (weight)+ M[location][j-1]
                B[i][j] = "choose this"
                
            else:
               
                M[i][j] = M[i-1][j]
                B[i][j] = "don't choose"


    S = {}
    S=set(S)
    i =N
    j=k

    while (i>0 and j>0):
        if B[i][j] == "choose this":
            location = LocateP(p[i] ,sorted_array)
            
            
            S.add(sorted_array[i][2])
            i = location
            j = j-1
        else:
            i = i-1
            #j stays the same
            
    
    #format: end, beginning, ID, weight, (future pjs)
    

    # return a list called schedule
    # each element in schedule should be 
    # an INT representing the NAME of an interval
    # you would like to place on your schedule

    schedule=(list(S))
    return schedule




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

