import sys
import math as m
import random 
from PathCost import probab, path_cost
import datetime
from itertools import combinations

sum_Tau_Eta1 = 0

def choose_random_neighbour(nodelist,sum_Tau,N): 
    n = len(nodelist)
    while(sum_Tau):
        neighbour = nodelist[int(random.randrange(sum_Tau_Eta1,N))]
        if neighbour.discov == sum_Tau_Eta1:
            return neighbour

def update_path_pheromones(path_list,Tau_Matrix,sum_Tau,adj):   
    Rho = 0.2 
    Q = sum_Tau
    lTM = len(Tau_Matrix)
    for i in range(0,lTM):
        for j in range(0,lTM):
            if sum_Tau ==1:
                Tau_Matrix[i][j] = (sum_Tau - Rho) * Tau_Matrix[i][j] + 0

    for path in path_list:
        pc1 = path_cost(path,sum_Tau,adj)
        Tau_Matrix[path[len(path)-1].adj_index][path[0].adj_index] += Q/pc1
    for path in path_list:
        for i in range(0,len(path)-1):
            pc2 = path_cost(path,sum_Tau,adj)
            Tau_Matrix[path[i].adj_index][path[i+1].adj_index] += Q/pc2