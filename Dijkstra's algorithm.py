import time
from collections import defaultdict
from heapq import *


class DirectedGraph:
    def __init__(self, fileName):
        self.fileName = fileName
        # one node has the next form: 1:{inbound: {2:45,3:22,4:12}, outbound:{5:45,2:45,3:23}}
        self.nodes = {}
        self.edges = []
        self._readEdges()

    def _readEdges(self):
        start = time.time()
        file = open(self.fileName, "r")
        firstLine = file.readline()[:-1].split(" ")
        nrOfEdges = int(firstLine[1])
        for i in range(nrOfEdges):
            currentLine = file.readline().split(" ")
            _from = currentLine[0]
            _to = currentLine[1]
            _cost = int(currentLine[2])
            self.edges.append((_from, _to, _cost))
        stop = time.time()
        print("Loaded file {0} in {1} seconds".format(self.fileName, stop - start))
        print(self.edges)


    def shortestPath(self, node1, node2):
        # in g we will have the graph
        g = defaultdict(list)
        for l,r,c in self.edges:
            g[l].append((c,r))
        # q is the priority queue
        q = [(0,node1,())]
        # seen is the set of visited nodes
        seen = set()
        #while the queue is not empty
        while q:
            # we pop the firt element from the queue
            # and turn it into a tupple of type(cost, node, currentPath)
            #path is the current path we are on
            (cost,v1,path) = heappop(q)
            if v1 not in seen:
                #if the node is not visited we add it to the seen-set
                seen.add(v1)
                # path becomed the current node and the nodes nodes before
                path = (v1, path)
                #if we reached our destination, we return the cost
                if v1 == node2:
                    return (cost,path)
                #we go through every cost and vertex that exists
                #and if we haven't visit it, we add it to the set
                for c, v2 in g.get(v1, ()):
                    if v2 not in seen:
                        heappush(q, (cost+c, v2, path))
        return ("No path")

if __name__ == '__main__':
    graph = DirectedGraph("graph1k.txt")
    print("The cost is:")
    print(graph.shortestPath("20","40"))
