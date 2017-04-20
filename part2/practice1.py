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
    adjacency = [[0 for j in range(num_nodes)] for i in range(num_nodes)]
    for i in range(num_edges):
        line = f.readline().split(" ")
        # Changed to zero indexed
        adjacency[int(line[0])-1][int(line[1])-1] = 1
    return {"matrix":adjacency, "nodes":nodes, "num_nodes":num_nodes}


def getOutboundLinks(adj_matrix, index):
    return sum(adj_matrix[index])


def dist(dist1, dist2):
    nodes = len(dist1)
    diff = [dist2[i]-dist1[i] for i in range(nodes)]
    norm_sqared = sum([diff[i]**2 for i in range(nodes)])
    return math.sqrt(norm_sqared)

def pageRank(num_nodes, adj_matrix, old_dist, damp = 0.85, epsilon = 0.01):
    if len(old_dist)==0:
        old_dist = [(1.0/num_nodes) for i in range(num_nodes)]
    new_dist = [0.0 for i in range(num_nodes)]
    num_out_links = [getOutboundLinks(adj_matrix, i) for i in range(num_nodes)]
    for i in range(num_nodes):
        total = 0
        for j in range(num_nodes):
            if adj_matrix[j][i] == 1:
                total += old_dist[j]/num_out_links[j]
        new_dist[i] = ((1-damp)/num_nodes) + (damp*total)
    if dist(old_dist, new_dist)<epsilon:
        return new_dist
    else:
        return pageRank(num_nodes, adj_matrix, new_dist)


def output(result):
    num_nodes = len(result)
    paired = [((i+1), result[i]) for i in range(num_nodes)]
    output = sorted(paired, key = lambda x: x[1], reverse = True)
    for i in output:
        print("{0}: {1}".format(i[0],i[1]))


if __name__ == "__main__":
    data = parseInput()
    num_nodes = data["num_nodes"]
    nodes = data["nodes"]
    adj_matrix = data["matrix"]
    results = pageRank(num_nodes, adj_matrix, [])
    output(results)
