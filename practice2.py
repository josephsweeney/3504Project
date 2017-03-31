import math
import random
import practice1

# print(practice1.simulate(100, [-math.inf, math.inf]))

moves = practice1.moves

def median(l):
    l.sort()
    return l[int(len(l)/2)]

def infiniteLattice(iterations):
    agent = (0,0)
    bound = [-math.inf, math.inf]
    xBound = [0,0]
    yBound = [0,0]
    path = set()
    steps = 0
    while moves(agent, path, bound) > 0:
        moving = True
        steps +=1
        while moving and steps < iterations:
            r = random.random()
            if r < 0.25:
                if (agent[0]+1, agent[1]) not in path and agent[0]+1 <= bound[1]:
                    agent = (agent[0]+1, agent[1])
                    moving = False

            elif 0.25 <= r < 0.5:
                if (agent[0]-1, agent[1]) not in path and agent[0]-1 >= bound[0]:
                    agent = (agent[0]-1, agent[1])
                    moving = False

            elif 0.5 <= r < 0.75:
                if (agent[0], agent[1]+1) not in path and agent[1]+1 <= bound[1]:
                    agent = (agent[0], agent[1]+1)
                    moving = False

            elif 0.75 <= r:
                if (agent[0], agent[1]-1) not in path and agent[1]-1 >= bound[0]:
                    agent = (agent[0], agent[1]-1)
                    moving = False
        path.add(agent)
        xBound[0] = agent[0] if agent[0] < xBound[0] else xBound[0]
        xBound[1] = agent[0] if agent[0] > xBound[1] else xBound[1]
        yBound[0] = agent[1] if agent[1] < yBound[0] else yBound[0]
        yBound[1] = agent[1] if agent[1] > yBound[1] else yBound[1]
    size = (xBound[1]-xBound[0])*(yBound[1]-yBound[0])
    dist = abs(agent[0])+abs(agent[1])
    return (steps, dist, size)


def simulate(times):
    steps = []
    dists = []
    sizes = []
    for i in range(times):
        (step, dist, size) = infiniteLattice(5000)
        steps.append(step)
        dists.append(dist)
        sizes.append(size)

    total = sum(steps)
    meanDist = sum(dists)/times
    meanSize = sum(sizes)/times
    devDist = practice1.standard_deviation(dists, meanDist)
    devSize = practice1.standard_deviation(sizes, meanSize)
    varDist = devDist**2
    varSize = devSize**2
    medDist = median(dists)
    medSize = median(sizes)
    print("Distance Mean: "+str(meanDist))
    print("Distance Median: "+str(medDist))
    print("Distance Variance: "+str(varDist))
    print("Distance Standard Deviation: "+str(devDist))
    print("Size Mean: "+str(meanSize))
    print("Size Median: "+str(medSize))
    print("Size Variance: "+str(varSize))
    print("Size Standard Deviation: "+str(devSize))

if __name__ == "__main__":
    (steps, dist, size) = infiniteLattice(5000)
    print("1 Run of Simulation of 5000 steps:\n")
    print("Distance traveled: " + str(dist))
    print("Lattice Size: "+ str(size)+"\n")

    print("Simulate 10 Times:\n")
    simulate(10)
    print()
    print("Simulate 100 Times:\n")
    simulate(100)
    print()
    print("Simulate 1000 Times:\n")
    simulate(1000)
