import random
import math

def moves(agent, path, bound):
    moves = 0
    if (agent[0]+1, agent[1]) not in path and agent[0]+1 <= bound[1]:
        moves += 1
    if (agent[0]-1, agent[1]) not in path and agent[0]-1 >= bound[0]:
        moves += 1
    if (agent[0], agent[1]+1) not in path and agent[1]+1 <= bound[1]:
        moves += 1
    if (agent[0], agent[1]-1) not in path and agent[1]-1 >= bound[0]:
        moves += 1
    return moves

def finiteLattice(bound):
    agent = (0,0)
    path = set()
    steps = 0
    while moves(agent, path, bound) > 0:
        moving = True
        steps +=1
        while moving:
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
    return steps

def standard_deviation(samples, mean):
    f = lambda x: (x-mean)**2
    return math.sqrt(sum(map(f, samples))/len(samples))

def simulate(times, bound):
    steps = []
    for i in range(times):
        steps.append(finiteLattice(bound))

    total = sum(steps)
    mean = total/times
    # TODO:Still need to calculate standard deviation
    return (mean, standard_deviation(steps, mean))


if __name__ == "__main__":
    print(simulate(100, [-49, 50]))
