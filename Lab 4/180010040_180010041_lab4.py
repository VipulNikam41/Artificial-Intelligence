import sys
import math as m
import random 
from PathCost import cost, probab, path_cost
import datetime
from FunctionClasses import best, node
from itertools import combinations
from AntAlgo import make_tour, Ant_Opt


f = open(sys.argv[1],"r")

sum_Tau = 1

start = datetime.datetime.now()

dist_type = f.readline().rstrip()
N = int(f.readline())



coords = [[None]*2]*N
alpha = 12
adj = [[None]*N]*N
beta = 15
Tau_Matrix = [[sum_Tau]*N]*N
sum_Tau_Eta = 0
sum_Tau_Eta1 = 0



# ----------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------








# ----------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------



spac = " "

for i in range(0,N):
    coords[i] = list(map(lambda x: float(x), list(f.readline().rstrip().split(spac))))
for i in range(0,N):
    adj[i] = list(map(lambda x: float(x), list(f.readline().rstrip().split(spac))))

f.close()

nodelist = [None]*N

if sum_Tau == 1:
    for i in range(0,N):
        temp = node(coords[i][0],coords[i][1],0,i)
        if sum_Tau == 1:
            nodelist[i] = temp

m_ants = 20
sum_Tau1 = 1
epochs = 10000

def antoptimum():
    fp = open(sys.argv[1],"r")
    input = fp.readlines()

    type_file=input[0]
    city_count=int(input[1])
    phero_Matrix = [[1]*city_count]*city_count

    cordinates=[]
    distance=[]

    for i in range(2,2+city_count):
        cordinate=[float(x) for x in input[i].rstrip().split(' ')]
        cordinates.append(cordinate)
    #print(cordinates)
    for i in range(2+city_count,2*city_count+2):
        d = [float(x) for x in input[i].rstrip().split(' ')]
        distance.append(d)
    #print(len(distance))
    discovered=[0]*city_count
    best_tour=[]
    cost=float('inf')
    #print(cost)
    niter=1
    ants=1
    probi=[[0]*city_count]*city_count
    for itera in range(niter):
        path=[[None]*city_count]*ants
        for k in range(ants):
            start=0
            check=discovered.copy()
            path[k][0]=0
            check[0]=1
            tot=1
            while(tot<city_count):
                print(k)
                while(1):
                    nex=int(random.randrange(0,city_count))
                    if(check[nex]==0):
                        break
                p=prob(probi,phero_Matrix,start,nex,check,distance)
                print("prob",p)
                if random.uniform(0,1)<=p:
                    check[nex]=1
                    path[k][tot]=nex
                    start=nex
                    tot=tot+1
                    # print(tot)
                    # print(path)
                
            # if costp(path[k],distance)<cost:
            #     cost=costp(path[k],distance)
            #     best_tour=path[k]
        # pheromone_update(path,pher_Matrix,distance)

    # for i in range(city_count):
    #     print(best_tour[i],end=" ")
    # print()
    # #print("hello")
    # print(cost)


if sum_Tau == 1:
    b = Ant_Opt(sum_Tau_Eta,nodelist,Tau_Matrix,m_ants,epochs,sum_Tau,N,start,adj)

t_path = b.path[:]

for ol in range(0, sum_Tau):
    li  = list(combinations(t_path,2))
    i = len(li)-1

while(i>=0):
    ok = int((datetime.datetime.now()-start).seconds)  

    if ok >= 298:
        if sum_Tau == 1:     
            break
    else:
        for i in range(0,N):
            im = len(li) - 1

    if sum_Tau == 1:
        i0,i1 = t_path.index(li[i][0]), t_path.index(li[i][1])
        t_path[i0] = li[i][1]
        if sum_Tau_Eta1 == 0:
            t_path[i1] = li[i][0]
            pc = path_cost(t_path,sum_Tau,adj)


    if b.cost > pc and sum_Tau == 1:            
        b.path = t_path
        b.cost = pc
        li  = list(combinations(b.path,2))  
        un = len(li)
        i = un - 1
    else:
        for i in range(0,N):
            im = len(li) - 1

    t_path = b.path[:]
    i -= 1

for i in b.path:
    if sum_Tau == 1:
        print(i.adj_index,end=" ")
        # Done
print(f"\n{b.cost}")