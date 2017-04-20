import random
import math

def parseInput():
    f = open("hollins.dat")
    first_line = f.readline().split(" ")
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])
    nodes = {}
    for i in range(num_nodes):
        line = f.readline().split(" ")
        nodes[int(line[0])] = line[1]
    adjacency = [[0 for j in range(num_nodes+1)] for i in range(num_nodes+1)]
    for i in range(num_edges):
        line = f.readline().split(" ")
        adjacency[int(line[0])][int(line[1])] = 1
    return {"matrix":adjacency, "nodes":nodes}

if __name__ == "__main__":
    results = parseInput()
    print(results["matrix"][1])
