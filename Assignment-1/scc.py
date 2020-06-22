
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
        self.graph = [[] for i in range(self.numVertices+1)]
        self.revGraph = [[] for i in range(self.numVertices+1)]
        self.color = ["white"]*(self.numVertices+1)
        self.visited = [False]*(self.numVertices+1)
        self.allChildsDiscovered = False
        self.time = 0
        self.order = deque()
        self.leader = None
        self.SCC = [0]*(self.numVertices+1)
        

    # Function to create a graph from the input data
    # and reverse it
    '''
    Input: Text file containing vertices and connections
    Output: Graph as a dictionary
    '''
    def createGraph(self, file):
        with open(file) as scc:
            for line in scc:
                data = line.split()
                data = [int(v) for v in data]
                self.graph[data[0]] += [data[1]]
                self.revGraph[data[1]] += [data[0]]


    # Function to calculate finishing time for node using for loop
    '''
    Input: vertex to start with
    Output: dictionary with node as key and finishing time as value
    '''
    def calculateFinishingTime(self, s):

        # Push the current source node in the stack
        stack = deque()
        stack.append(s)

        while stack:
            # Pop an element from the stack
            v = stack.pop()
            if self.color[v] != "black":
                stack.append(v)
                if self.color[v] == "white":
                    self.color[v] = "grey"
                self.allChildsDiscovered = True
                for node in self.revGraph[v]:
                    if self.color[node] == "white":
                        stack.append(node)
                        self.allChildsDiscovered = False

                if self.allChildsDiscovered == True:
                    self.color[v] = "black"
                    self.order.append(v)
                    stack.pop()      

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
            if self.visited[self.leader] == False:
                self.visited[self.leader] = True
                stack.append(self.leader)
                self.SCC[self.leader] += 1
                while stack:
                    for node in self.graph[stack.pop()]:
                        if self.visited[node] == False:
                            self.visited[node] = True
                            stack.append(node)
                            self.SCC[self.leader] += 1

        self.SCC.sort(reverse = True) 

                

##----------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    g = graph(int(input("Enter number of vertices: ")))
    print(f"\nNumber of vertices in graph = {g.numVertices}")
    loadTime = datetime.now()
    g.createGraph("SCC.txt")
    print(f"\nTime taken to load the graph and reverse it = {datetime.now()-loadTime}")

    finishTime = datetime.now()
    # print(g.calculateFinishingTime(9))
    for node in range(g.numVertices,0,-1):
        g.calculateFinishingTime(node)
    print(f"\nTime taken to calculate the finishing time = {datetime.now()- finishTime}\n")
    g.getSCC()
    print(g.SCC[:5])
    

    


