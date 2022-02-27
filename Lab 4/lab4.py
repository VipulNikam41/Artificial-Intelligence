import sys
import math as m
import random 


 #Pheromone depositite inititially with 1
def costp(path,dis):
	cost_p=0
	for i in range(len(path)-1):
		cost_p+=dis[path[i]][path[i+1]]
	return cost_p + dis[path[len(path)-1]][path[0]]

def prob(probi,pher_Matrix,start,end,discoverd,distance):
	tot_bot=0
	alpha=15
	beta=16
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
				print("hello")
				if(check[nex]==0):
					break
			p=prob(probi,phero_Matrix,start,nex,check,distance)
			print("prob",p)
			if random.uniform(0,1)<=p:
				check[nex]=1
				path[k][tot]=nex
				start=nex
				tot=tot+1
				print(tot)
				print(path)
			
		if costp(path[k],distance)<cost:
			cost=costp(path[k],distance)
			best_tour=path[k]
	pheromone_update(path,pher_Matrix,distance)

for i in range(city_count):
	print(best_tour[i],end=" ")
print()
#print("hello")
print(cost)
			
			
