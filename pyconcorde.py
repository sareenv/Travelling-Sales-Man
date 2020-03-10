from concorde.tsp import TSPSolver 
from time import time

pointsList=[]
for line in open("input_points.txt", "r").readlines():
    currentPoints = []
    for element in line[1:-3].split("), "):
        currentPoints.append((int(element[1:].split(",")[0]), int(element[1:].split(",")[1])))
    pointsList.append(currentPoints)
solutions=[]
times=[]
for element in pointsList:
    if len(element)<=3:
        options=([0], [0,1], [0,1,2])
        solutions.append(options[len(element)-1])
        times.append(0)
        continue
    print("\n\nMOVING ON TO ", len(solutions))
    print("\n\n")
    solver = TSPSolver.from_data(*zip(*element), "EUC_2D")
    start = time()
    solution = solver.solve()
    while not solution.found_tour:
        pass #wait until we find tour
    totalTime = time()-start
    solutions.append(solution.tour)
    times.append(totalTime)

output = open("output_solutions.txt","w")
timeOut = open("output_time.txt", "w")
for sol, time in zip(solutions, times):
    outputStream = "["
    for element in sol:
        outputStream += str(element) + ", "
    output.write(outputStream[:-2] + "]\n")
    timeOut.write(str(time) + "\n")
