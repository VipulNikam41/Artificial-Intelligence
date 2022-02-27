import sys
import math as m
import random 
import datetime
from itertools import combinations

alpha = 12
beta = 15

def cost(c,n,adj,sum_Tau = 1):
    if sum_Tau == 1:
        almc = c.adj_index
        almn = n.adj_index
        return adj[almc][almn]
    elif sum_Tau == 0:
        cost_p=0
        for i in range(len(path)-1):
            cost_p+=dis[path[i]][path[i+1]]
        return cost_p + dis[path[len(path)-1]][path[0]]

def pheromone(c,n,Tau_Matrix,sum_Tau = 1):
    if sum_Tau == 1:
        almc = c.adj_index
        almn = n.adj_index
        return Tau_Matrix[almc][almn]
    elif sum_Tau == 0:
        rho=0.2
        q=1
        c=len(pher_Matrix)
        for i in range(c):
            for j in range(c):
                pher_Matrix[i][j]=(1-rho)*pher_Matrix[i][j]
        for path in path_list:
            pher_Matrix[path[len(path)-1]][path[0]]+=q/costp(path,distance)
            for i in range(c-1):
                pher_Matrix[path[i]][path[i+1]]+=q/costp(path,distance)

def probab(sum_Tau_Eta,current,neighbour,nodelist,Tau_Matrix,sum_Tau,adj): 
    if sum_Tau == 1:
        betaC = cost(current,neighbour,adj)
        alphaC = pheromone(current,neighbour,Tau_Matrix)
        Tau_ = alphaC ** alpha
        Eta_ = sum_Tau/(betaC) ** beta
        
        for i in range(0,len(nodelist)):
            if nodelist[i].discov == 0 :
                tm1 = pheromone(current,nodelist[i],Tau_Matrix)**alpha
                tm2 = (sum_Tau/(cost(current,nodelist[i],adj)))**beta
                tm3 = tm1 + tm2
                tmf = tm1 * tm2
                sum_Tau_Eta = sum_Tau_Eta + tmf
        if sum_Tau_Eta == 0:
            if sum_Tau == 1:
                return sum_Tau
        p = ( Tau_* Eta_ )/( sum_Tau_Eta ) * sum_Tau
        return  p
    elif sum_Tau == 0:
        tot_bot=0
        num1=pher_Matrix[start][end] **alpha 
        num2=1/distance[start][end] **beta
        num=num1*num2
        for i in range(city_count):
            if discovered[i]==0 and i!=start:
                den1=pher_Matrix[start][i]**alpha
                
                den2=1/distance[start][i]**beta
                den=den1*den2
                tot_bot+=den
        if tot_bot==0:
            return 1
        else:
            p=num/tot_bot
            if(p<1):
                print(p)
        #print(num,tot_bot)
        return p

def path_cost(path,sum_Tau,adj):   
    cost_p = 0
    fnl = 0
    for i in range(0,len(path)-sum_Tau):
        cost_p = cost_p + cost(path[i],path[i+sum_Tau],adj)

    fnl = cost_p + cost(path[len(path)-sum_Tau],path[0],adj)
    return fnl
