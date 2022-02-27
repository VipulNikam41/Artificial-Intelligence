import sys
import math as m
import random 
import datetime
from itertools import combinations



class best:
    def __init__(self,cost,path):
        self.cost = cost
        self.path = path

class node:
    def __init__(self,x,y,discov,adj_index, lenght=None, prob=None, initial_cost=None):
        self.x = x
        self.prob = prob
        self.lenght = lenght
        self.y = y
        self.discov = discov
        self.initial_cost = initial_cost
        self.adj_index = adj_index

    def pheromone_update(path_list,pher_Matrix,distance):
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

    def display(self):
        print("x",self.x," y",self.y," discov",self.discov)

    def distanceCall(self):
        print("x",self.x, " discov",self.discov)

    def antOpt(self):
        print(" y",self.y," discov",self.discov)