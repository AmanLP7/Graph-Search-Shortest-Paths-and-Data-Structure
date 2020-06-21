
#########--------------- Code to find strongly connected components in a graph --------------#########

# Importing required modules

from datetime import datetime
from collections import deque, defaultdict

# Importing data from the file
# startTime = datetime.now()


# Class containing functions to define graph and related functions
class graph:


    # Function to initialise parameters for a graph
    '''
    Input: Number of vertices
    '''
    def __init__(self, vertices):
        self.numVertices = vertices
        self.graph = defaultdict(list)
        self.visited = [False]*self.numVertices
        self.path = deque()
        self.order = deque()
        self.leader = None
        self.SCC = [0]*self.numVertices


    # Function to add edge to a graph
    '''
    Input: Key, value
    '''
    def addEdge(self, key, value):
        self.graph[key].append(value)
        

    # Function to create a graph from the input data
    '''
    Input: Text file containing vertices and connections
    Output: Graph as a dictionary
    '''
    def createGraph(self, file):
        with open(file) as scc:
            for line in scc:
                data = line.split()
                data = [int(v) for v in data]
                if len(data) > 1:
                    key = data[0]
                    for value in data[1:]:
                        self.addEdge(key, value)

        return self.graph


    # Function to reverse a graph
    '''
    Input: Graph
    Output: Input graph with all the arcs reversed
    '''
    def getReverse(self):

        self.revGraph = defaultdict(list)

        # Reverse the graph
        for key in self.graph.keys():
            for value in self.graph[key]:
                self.revGraph[value].append(key)

        return self.revGraph
        

    # Function to calculate finishing time for node using for loop
    '''
    Input: vertex to start with
    Output: dictionary with node as key and finishing time as value
    '''
    def calculateFinishingTime(self, s):

        # Push the current source node in the stack
        stack = deque()
        stack.append(s)

        while len(stack) > 0:
            # Pop an element from the stack
            v = stack.pop()
            if v not in self.path:
                self.path.append(v)
                stack.append(v)

                # Get all the adjacent vertices for the popped node
                # and check if it has been visited or not, if not
                # then append it to the stack
                for node in self.revGraph[v]:
                    if node not in self.path:
                        stack.append(node)
            else:
                if v not in self.order:
                    self.order.append(v)

        return self.order


    # Function to find strong components and their length
    '''
    Input: Finishing time for nodes as calculated in the first pass
    Output: Dictionary with leader node as key and length of the scc as value
    '''
    def getSCC(self):
        stack = deque()
        while self.order:
            self.leader = self.order.pop()
            if self.visited[self.leader - 1] == False:
                self.visited[self.leader-1] == True
                stack.append(self.leader)
            else:
                pass

                

##----------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    g = graph(int(input("Enter number of vertices: ")))
    loadTime = datetime.now()
    graph = g.createGraph("test.txt")
    revGraph = g.getReverse()
    endTime = datetime.now()
    print(f"\nTime taken to load the graph and reverse it = {endTime - loadTime}\n")
    print(f"Number of vertices in the graph = {g.numVertices}")

    startTime = datetime.now()
    for v in range(g.numVertices,0,-1):
        g.calculateFinishingTime(v)
    # print(g.finishingTimes)
    endTime = datetime.now()
    print(f"\nTime taken to calculate the finishing time = {endTime - loadTime}")

    print(g.order)

    g.getSCC()
    # startTime = datetime.now()
    # for v in range(g.numVertices,0,-1):
    #     g.calculateFinishingTime(v)

    # print(endTime - startTime)

    # print(g.finishingTimes[297])


