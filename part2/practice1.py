import random
import math
import csv

class PageRank:

    def parseInput(self, filestr):
        f = open(filestr)
        first_line = f.readline().split(" ")
        num_nodes = int(first_line[0])
        num_edges = int(first_line[1])
        nodes = {}
        for i in range(num_nodes):
            line = f.readline().split(" ")
            nodes[int(line[0])] = line[1]
        adjacency = [[0 for j in range(num_nodes)] for i in range(num_nodes)]
        incoming = [[] for i in range(num_nodes)]
        outBoundLinks = [0 for i in range(num_nodes)]
        for i in range(num_edges):
            line = f.readline().split(" ")
            # Changed to zero indexed
            start = int(line[0])-1
            end = int(line[1])-1
            adjacency[start][end] = 1
            incoming[end].append(start)
            outBoundLinks[start] += 1
        for i in range(num_nodes):
            if outBoundLinks[i] == 0:
                adjacency[i] = [1 for j in range(num_nodes)]
                outBoundLinks[i] = num_nodes
                for row in incoming:
                    row.append(i)
        self.adj_matrix = adjacency
        self.nodes = nodes
        self.num_nodes = num_nodes
        self.incoming = incoming
        self.num_out_links = outBoundLinks
        return {"matrix":adjacency, "nodes":nodes, "num_nodes":num_nodes}


    def getOutboundLinks(self, index):
        # No longer need, calculate in parsing
        return sum(self.adj_matrix[index])


    def dist(self,dist1, dist2):
        nodes = len(dist1)
        diff = [dist2[i]-dist1[i] for i in range(nodes)]
        norm_sqared = sum([diff[i]**2 for i in range(nodes)])
        return math.sqrt(norm_sqared)

    def neighbors(self, i):
        # No longer need, calculate in parsing
        neighbors = []
        for j in range(self.num_nodes):
            if self.adj_matrix[j][i] == 1:
                neighbors.append(j)
        return neighbors


    def pageRank(self, old_dist, damp = 0.85, epsilon = 0.001):
        num_nodes = self.num_nodes
        if len(old_dist)==0:
            old_dist = [(1.0/num_nodes) for i in range(num_nodes)]
        new_dist = [0.0 for i in range(self.num_nodes)]
        for i in range(num_nodes):
            total = 0.0
            for j in self.incoming[i]:
                total += old_dist[j]/self.num_out_links[j]
            new_dist[i] = ((1.0-damp)/num_nodes) + (damp*total)
        if self.dist(old_dist, new_dist)<epsilon:
            self.ranks = new_dist
            return new_dist
        else:
            # print("PR0: {0}  PR1: {1}".format(new_dist[0], new_dist[1]))
            return self.pageRank(new_dist, damp = damp)


    def output(self):
        num_nodes = self.num_nodes
        result = self.ranks
        paired = [((i+1), result[i]) for i in range(num_nodes)]
        output = sorted(paired, key = lambda x: x[1], reverse = True)
        for i in output:
            print("{0} {1}".format(i[0],self.nodes[i[0]]))

    def sort(self, rank):
        paired = [((i+1), rank[i]) for i in range(self.num_nodes)]
        output = sorted(paired, key = lambda x: x[1], reverse = True)
        return [x[0] for x in output]

    def outputCSV(self):
        csvfile = open('practice1.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        first = self.sort(self.pageRank([], damp = 0.85))
        second = self.sort(self.pageRank([], damp = 0.95))
        third = self.sort(self.pageRank([], damp = 0.50))
        header = ["rank", "d=0.85","d=0.95","d=0.50"]
        writer.writerow(header)
        rows = [[i+1, first[i], second[i], third[i]] for i in range(self.num_nodes)]
        writer.writerows(rows)


if __name__ == "__main__":
    pr = PageRank()
    data = pr.parseInput("hollins.dat")
    results = pr.pageRank([], damp = 0.85)
    # pr.outputCSV()
