########-------------- Code for implementing depth first search --------------########

# Importing required modules
from collections import deque, defaultdict

## Class to create a graph object and search elements using depth first search
'''
Uses for loop instead of recursion.
'''

class graph:

    # Initialising adjacency list as a dictionary
    def __init__(self, vertices):
        self.numVertices = vertices
        self.adj = defaultdict(list)
        for key in range(vertices):
            self.adj[key+1] = []

    # Function to add edges to a vertex
    '''
    Input: Takes vertex and edge as input
    '''
    def addEdge(self, v, w):
        self.adj[v].append(w)

    # Function to print all reachable nodes from given vertex
    '''
    Input: Vertex
    '''
    def DFS(self, s):
        visited = [False for _ in range(self.numVertices)]

        # stack for DFS
        stack = deque()

        # Push the current source node in the stack
        stack.append(s)

        while len(stack) > 0:
            # Pop an element from the stack
            v = stack.pop()

            # Check if the element has been visited or not
            if visited[v-1] == False:
                print(v)
                visited[v-1] = True

            # Get all the adjacent vertices for the popped node
            # and check if it has been visited or not, if not
            # then append it to the stack
            for node in self.adj[v]:
                if visited[node-1] == False:
                    print(self.adj[v])


if __name__ == "__main__":

    G = graph(5)
    G.addEdge(2, 1)  
    G.addEdge(1, 3)  
    G.addEdge(3, 2)  
    G.addEdge(1, 4)  
    G.addEdge(2, 5)  

    G.DFS(3)
  








