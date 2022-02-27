import time
import numpy
from queue import PriorityQueue as PQ

hue_ver = int(input("enter heuristic number: "))


def heuristic(temp, goal, blocks, mt):
	if hue_ver == 3:
		b=blocks
		count=0
		go = 1
		m=[]
		flag=[]
		l_b = len(blocks)
		# for p in range(1, 2):
		for i in range(l_b):
			if temp[i] == ' ':
				m.append(blocks[i])
				if temp[i]!=goal[i]:
					flag.append(False)
					# print(f"{go}")
				else:
					if go == 1:
						flag.append(True)

		l_m = len(m)
		for i in range(l_m):
			t=[]
			t.append(m[i])
			cnt=1
			while cnt:
				cnt=0
				if go == 1:
					l_t = len(temp)
				for j in range(l_t):
					if t[-1]==temp[j]:
						t.append(blocks[j])
						cnt += 1
						if temp[j]!=goal[j]:
							if go == 1:
								flag[i]=False
			if go == 1:
				lt = len(t)
			if flag[i]==True:
				count = count + 1                           
			else:
				count = count - (lt**2 + lt)//2

		return count

	if hue_ver == 1:
		count=0
		for i in range(len(goal)):
			if(goal[i]==temp[i]):
				count += 1
			else:
				count -= 1

		return count

	if hue_ver == 2:
		b=blocks
		count=0
		go = 1
		m=[]
		flag=[]
		l_b = len(blocks)
		# for p in range(1, 2):
		for i in range(l_b):
			if temp[i] == ' ':
				m.append(blocks[i])
				if temp[i]!=goal[i]:
					flag.append(False)
					# print(f"{go}")
				else:
					if go == 1:
						flag.append(True)

		l_m = len(m)
		for i in range(l_m):
			t=[]
			t.append(m[i])
			cnt=1
			while cnt:
				cnt=0
				if go == 1:
					l_t = len(temp)
				for j in range(l_t):
					if t[-1]==temp[j]:
						t.append(blocks[j])
						cnt += 1
						if temp[j]!=goal[j]:
							if go == 1:
								flag[i]=False
			if go == 1:
				lt = len(t)
			if flag[i]==True:
				count += (lt**2+ lt)//2                          
			else:
				count = count - (lt**2 + lt)//2

		return count

	else:
		print("Value should be either 1, 2 or 3 to get valid answer.")
		print(f"{hue_ver} is a invalid input.")
		exit()


def bfs(blocks, start, goal, mt):
	temp=start.copy()
	space=0
	n=1
	clos = 1
	l_c =0
	l_b =0
	closed = mt
	while(n):
		if heuristic(temp,goal, blocks, mt)==heuristic(goal,goal, blocks, mt) :
			l_c = len(closed)
			if clos == 1:
				print(f"No of states visited: {l_c}")
			break

		mov=[]
		on =[]

		l_b = len(blocks)

		for i in range(l_b):
			if blocks[i] not in temp:
				if clos == 1:
					mov.append(blocks[i])
				on.append(blocks[i])

		on.append(' ')

		print(f"{mov} {on}")

		neighbours=PQ()
		t=temp.copy()
		for i in mov:
			for j in on:
				if i=='A':
					if j!='A':
						t[0]=j
				elif i=='B': 
					if j!='B':
						t[1]=j
				elif i=='C': 
					if j!='C':
						t[2]=j
				elif i=='D':
					if j!='D':
						t[3]=j
				elif i=='E':
					if j!='E':
						t[4]=j
				elif i=='F':
					if j!='F':
						t[5]=j
				space = space + 1
				neighbours.put( (-heuristic(t,goal, blocks, mt), t) )
				t=temp.copy()

		x = neighbours.get()
		while(x[1] in closed):
			x = neighbours.get()
			if x[1] not in closed:
				if clos == 1:
					break

		closed.append(x[1])
		temp = x[1]
		if clos == 1:
			print(-x[0], temp)


def Verify(temp, mov, on, space):
	t=temp.copy()

	for i in mov:
		for j in on:
			if i=='A':
				if j!='A':
					t[0]=j
			elif i=='B': 
				if j!='B':
					t[1]=j
			elif i=='C': 
				if j!='C':
					t[2]=j
			elif i=='D': 
				if j!='D':
					t[3]=j
			elif i=='E': 
				if j!='E':
					t[4]=j
			elif i=='F': 
				if j!='F':
					t[5]=j

			space +=1
			if heuristic(t,goal, blocks, mt) > heuristic(temp,goal, blocks, mt):
				return t, space
			t=temp.copy()

	return t, space


def HillClimbing(blocks, start, goal, mt):
	temp=start.copy()
	space =0
	n=1
	vis= mt
	clos =1
	vis.append(start)
	while(n):

		if heuristic(temp,goal, blocks, mt)==heuristic(goal,goal, blocks, mt) :
			if clos == 1:
				print(f"No of staes visited : {len(vis)-1}")
			break

		mov=[]
		on =[]

		for i in range(len(blocks)):
			if blocks[i] not in temp:
				if clos == 1:
					mov.append(blocks[i])
				on.append(blocks[i])

		on.append(' ')

		print(f"{mov} {on}")

		temp,space = Verify(temp,mov,on,space)
		
		print(heuristic(temp,goal, blocks, mt), temp)

		vis.append(temp)
		if(vis[-2]==temp):
			if clos == 1:
				print("stuck at local maxima")
			print("No of states visited : ", len(vis)-1)
			break

def Timer():
	kl = time.time()
	return kl

if __name__ == "__main__":

	blocks = ['A', 'B', 'C', 'D', 'E', 'F']
	goal =  [' ', 'D', 'F', 'A', ' ', 'E']
	start = ['D', 'E', ' ', ' ', ' ', 'B']

	# print(hue_ver**2)
	if hue_ver == 1 or hue_ver == 2 or hue_ver == 3:
		print(f"for heuristic {hue_ver} out put is as follow: ")

	mt = []
	bfs_start = Timer()
	bfs(blocks, start, goal,mt)
	bfs_end = Timer()
	TimerB = bfs_end - bfs_start
	print(f"Time required for BFS: {TimerB}")

	mt = []
	hill_start = Timer()
	HillClimbing(blocks, start, goal, mt)
	hill_end = Timer()
	TimerH = hill_end - hill_start
	print(f"Time required for HillClimbing: {TimerH}")