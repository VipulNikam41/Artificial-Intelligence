from string import ascii_lowercase
import random
from itertools import combinations
import numpy as np
import os.path
from os import path


filew = open("output.txt","w")

# number of clauses
m = 5
# number of variables in a clause
k = 3
# number of variables
n = 4
data = []

hAssigns = []
beam_penetration = []
v_n = []
temp = []
var_penetration = []
tabu_penetration = []
bAssigns = []
vAssigns = []
h_n = []
initials = []
b_var = []
b_n = []
assigns = []
problems = []
i = 0

positive_var = (list(ascii_lowercase))[:n]
forPositive = list(np.random.choice(2,n))
forNegative = [abs(1-i) for i in forPositive]
negative_var = [c.upper() for c in positive_var]

variables = positive_var + negative_var
assign = forPositive + forNegative

allCombs = list(combinations(variables, k))

c = random.sample(allCombs, m)

if c not in problems:
    i = i + 1
    problems.append(list(c))
    # print(f"v: {variables}\tp: {problems}")
# return problems

problems_new = []
for c in problems:
    for sub in c:
        temp.append(list(sub))
    problems_new.append(temp)
# for i in range(len(problems_new)):
#     print(problems_new[i])

# for i in range(len(problems)):
    # filew.write(f"{problems[i]}")
    # print(f"p: {problems[i]}")createProblem

if path.exists("problems.txt"):
	filer = open("problems.txt", "r")
	data.append(filer.read())
	# print("k: " + data[0])
	filer.close()
else:
	print("'problems.txt' does not exist. Create it by running 'problem.py' or './run.sh'.")
	exit()


li = [9,9,9,9,9,8,8,9,9,9,9,9,9,9,9,9,9,9,10]
stp = random.choice(li)
data[0] = problems[0]

def assignment():
    var_assign = dict(zip(variables, assign))
    return var_assign

assign = assignment()
filew.write(f"{assign}\n")
filew.write(f"{data}\n")

def solve(assign):
    count = 0
    for sub in data[0]:
        l = [assign[val] for val in sub]
        count = count + any(l)
    return count

def beamSearch(assign,  b, stepSize):
    bestAssign = assign.copy()    
    stp = random.choice(li)  
    assignValues = list(assign.values())
    assignKeys = list(assign.keys())
    possibleAssigns = []
    possibleScores = []
    steps = []
    editAssign = assign.copy()
    initail = solve(assign)
    if initial == len(data[0]):
        p = str(stepSize) + "/" + str(stepSize)
        p = str(stepSize)
        return assign, p
    
    for i in range(len(assignValues)):
        stepSize += 1
        editAssign[assignKeys[i]] = abs(assignValues[i]-1)
        c = solve(editAssign)
        possibleAssigns.append(editAssign.copy())
        possibleScores.append(c)
        steps.append(stepSize)
    
    selected = list(np.argsort(possibleScores))[-b:]
    
    if len(data[0]) in possibleScores:
        index = [i for i in range(len(possibleScores)) if possibleScores[i]==len(data[0])]
        p = str(steps[index[0]]) + "/" + str(steps[-1])
        p = str(steps[-1])
        return possibleAssigns[ index[0] ], p
    else:
        selectedAssigns = [possibleAssigns[i] for i in selected]
        for a in selectedAssigns:
            return beamSearch(a, b, stepSize)

def tabu(assign, parentNum, received, step):
    bestAssign = assign.copy()      
    assignValues = list(assign.values())
    assignKeys = list(assign.keys())
    maxNum = parentNum
    maxAssign = assign.copy()
    editAssign = assign.copy()
    
    for i in range(len(assignValues)):
        step += 1
        editAssign[assignKeys[i]] = abs(assignValues[i]-1)
        c = solve(editAssign)
        if maxNum<c:
            received = step
            maxNum = c
            maxAssign = editAssign.copy()
            
    if maxNum==parentNum:
        s = str(received) + "/" + str(step-len(assignValues))
        s = str(step-len(assignValues))
        return bestAssign, maxNum, s
    else:
        parentNum = maxNum
        bestassign = maxAssign.copy()
        return tabu(bestassign, parentNum, received, step)

def variableNeighbor(assign, b, step):
    bestAssign = assign.copy()      
    assignValues = list(assign.values())
    stp = random.choice(li)
    assignKeys = list(assign.keys())
    steps = []
    possibleAssigns = []
    possibleScores = []
    
    editAssign = assign.copy()
    
    initail = solve(assign)
    stp =9
    if initial == len(data[0]):
        p = str(step) + "/" + str(step)
        p = str(step)
        return assign, p, b
    
    for i in range(len(assignValues)):
        step += 1
        editAssign[assignKeys[i]] = abs(assignValues[i]-1)
        c = solve(editAssign)
        possibleAssigns.append(editAssign.copy())
        possibleScores.append(c)
        steps.append(step)
    
    selected = list(np.argsort(possibleScores))[-b:]
    
    if len(data[0]) not in possibleScores:
        selectedAssigns = [possibleAssigns[i] for i in selected]
        for a in selectedAssigns:
            return variableNeighbor(a, b+1, step)
    
    else:
        index = [i for i in range(len(possibleScores)) if possibleScores[i]==len(data[0])]
        p = str(steps[index[0]]) + "/" + str(steps[-1])
        p = str(steps[-1])
        return possibleAssigns[index[0]], p, b


i += 1
l =[]
initial = solve(assign)

bw = int(input("Enter beam width: "))
tt = int(input("Enter tabu tenure: "))

bestAssign, score, hp = tabu(assign, initial, 1, tt)
hAssigns.append(bestAssign)
assigns.append(assign)
h_n.append(score)
initials.append(initial)
tabu_penetration.append(hp)

h3, b3p = beamSearch(assign, 3, bw)
# h4, b4p = beamSearch(assign, 4, bw)

bAssigns.append(h3)
beam_penetration.append(b3p)

v, p, bb = variableNeighbor(assign, 1, 1)
var_penetration.append(p)
b_var.append(bb)
vAssigns.append(v)

filew.write(f"Problem {i}: {data[0]}\n")
filew.write(f'Beam search : {h3}\n\tStates Explored: {b3p}\n')
# filew.write(f'Beam search (4): {h4}\n\tStates Explored: {b4p}\n')
filew.write(f'Variable Neighbourhood: {v}\n\tStates Explored: {p}\n')
filew.write(f'Tabu searxh: {bestAssign}\n\tStates Explored: {hp}\n')
filew.close()