from concorde.tsp import TSPSolver 
from time import time

pointsList=[]
for line in open("density_points.txt", "r").readlines():
    currentPoints = []
    for element in line[1:-3].split("), "):
        currentPoints.append((int(element[1:].split(",")[0]), int(element[1:].split(",")[1])))
    pointsList.append(currentPoints)
solutions=[]
times=[]
for element in pointsList:
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

output = open("density_output_solutions.txt","w")
timeOut = open("density_output_time.txt", "w")
for sol, time in zip(solutions, times):
    outputStream = "["
    for element in sol:
        outputStream += str(element) + ", "
    output.write(outputStream[:-2] + "]\n")
    timeOut.write(str(time) + "\n")
