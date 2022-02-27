import sys
import math as m
import random 
from FunctionClasses import best, node
from PathCost import cost, probab, path_cost
from NextNeighbour import update_path_pheromones, choose_random_neighbour
import datetime
from itertools import combinations

def make_tour(sum_Tau_Eta,nodelist,Tau_Matrix,sum_Tau,N,start,adj):
    for node in nodelist:
        node.discov = 0
    discov_count = sum_Tau - sum_Tau *1
    current = choose_random_neighbour(nodelist,sum_Tau,N) 
    current.discov = sum_Tau
    path = [current] 
    while(discov_count <= len(nodelist)- (sum_Tau + sum_Tau)): 
        if int((datetime.datetime.now()-start).seconds) >= 294:
            return sum_Tau * (-1)
        neighbour = choose_random_neighbour(nodelist,sum_Tau,N)
        probability = probab(sum_Tau_Eta,current,neighbour,nodelist,Tau_Matrix,sum_Tau,adj)

        if random.uniform(0,1) <= probability: 
            neighbour.discov = 1
            discov_count = discov_count + 1
            path.append(neighbour)
            current = neighbour
    return path

def Ant_Opt(sum_Tau_Eta,nodelist,Tau_Matrix,m_ants,epochs,sum_Tau,N,start,adj):   
    best_path = best(float('inf'),[None]*len(nodelist))
    kth_path = []
    path_list = [[None]*len(nodelist)]*m_ants
    for iterat in range(0,epochs):
        for i in range (0,m_ants):
            kth_path = make_tour(sum_Tau_Eta,nodelist,Tau_Matrix,sum_Tau,N,start,adj)  
            
            if kth_path == sum_Tau * (-1): 
                return best_path

            path_list[i] = kth_path                         
            if path_cost(kth_path,sum_Tau,adj) < best_path.cost:    
                best_path.cost = path_cost(kth_path,sum_Tau,adj)
                best_path.path = kth_path

        update_path_pheromones(path_list,Tau_Matrix,sum_Tau,adj)    
    
    return best_path

def Ant(sum_Tau_Eta,nodelist,N,start,adj):   
    best_path = best(float('inf'),[None]*len(nodelist))
    kth_path = []
    path_list = [[None]*len(nodelist)]*2
    for iterat in range(0,4):
        for i in range (0,2):
            # kth_path = make_tour(sum_Tau_Eta,nodelist,Tau_Matrix,1,N,start,adj)  
            print(f"{kth_path}")
            
            if kth_path == -1: 
                return best_path

            path_list[i] = kth_path                         
            if path_cost(kth_path,1,adj) < best_path.cost:    
                best_path.cost = path_cost(kth_path,1,adj)
                best_path.path = kth_path

        update_path_pheromones(path_list,Tau_Matrix,1,adj)    
    
    return best_path