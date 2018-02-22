import random
import numpy as np
import time

# S = {}
# V = [
# [89, 42, 0, 2, 24, 20, 40, 37, 30, 77],
# [66, 75, 9, 59, 69, 66, 52, 14, 85, 36],
# [82, 68, 0, 81, 36, 25, 48, 53, 11, 68],
# [6, 96, 82, 53, 17, 70, 26, 12, 91, 82],
# [34, 86, 22, 18, 66, 73, 82, 88, 18, 36],
# [90, 43, 43, 93, 80, 96, 12, 28, 74, 93],
# [19, 75, 30, 48, 31, 76, 84, 29, 20, 15],
# [29, 73, 88, 9, 36, 40, 40, 19, 1, 45],
# [77, 31, 6, 68, 36, 40, 22, 43, 27, 61],
# [70, 21, 2, 89, 30, 91, 66, 74, 79, 92]]

#V = [[2,4,0],[1,5,0],[1,3,2]]

#V = np.random.randint(0,10)*100
# minV = 1000
# for row in V:
#     for col in row:
#         minV = min(minV,col)
# print minV
#print V
def runAuction(V):
    n = len(V)
    unassigned_agents = [i for i in range(n)]
    unassigned_objects = [i for i in range(n)]

    assignments = {}
    P = [0 for i in range(n)]
    epsilon = 1.0/n
    startingTime = time.time()
    while(len(unassigned_agents) != 0):
        # print unassigned_agents
        # print V
        # print P
        fav = float("-inf")
        secondFav = float("-inf")

        currentAgent = unassigned_agents.pop()

        #Calculate max(Aij - Pij)
        for index in range(len(V[currentAgent])):
            #print currentAgent
            #print index
            tmpFav = V[currentAgent][index]-P[index]
            if tmpFav > fav:
                fav = tmpFav
                objToAssign = index

        #Calculate second max(Aij - Pij)
        for index in range(len(V[currentAgent])):
            if index == objToAssign:
                continue
            tmpSecondFav = V[currentAgent][index]-P[index]
            if tmpSecondFav > secondFav:
                secondFav = tmpSecondFav

        #Calculate bid
        bid = fav - secondFav + epsilon

        #If object not assigned...
        if objToAssign in unassigned_objects:
            unassigned_objects.remove(objToAssign)
            assignments[currentAgent] = objToAssign
            P[objToAssign] += bid

        #If object already assigned...
        #Remove assignment from assignments and assign object to new agent
        elif objToAssign not in unassigned_objects:
            for key,value in assignments.items():
                if value == objToAssign:
                    del assignments[key]
                    unassigned_agents.append(key)

            assignments[currentAgent] = objToAssign
            P[objToAssign] += bid
        #print len(unassigned_agents)

    totalSum = 0
    for key,value in assignments.items():
            totalSum += V[key][value]
    #print "Time taken", time.time()-startingTime
    return assignments, totalSum, V

#print assignments
#print P

def randomAuction(n,M):
    V = [[random.randint(0,M-1) for i in range(n)] for i in range(n)]
    return runAuction(V)


#print randomAuction(10,100)
