##-------------------------------------- Djisktra's algorithm using minimum heap ---------------------------------##

# Thanks to - https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/

# Importing required modules
from collections import defaultdict

# Class to implement heap data structure
class Heap():

    # Function to initialise heap data structure
    def __init__(self, numVertices):
        self.array = [(-1, -float("inf"))]
        self.maxSize = numVertices 
        self.size = 0
        self.FRONT = 1
        self.location = [None]

    # Function to define new node in a minimum heap
    '''
    Input: Vertex, distance
    Output: New node as a list containing vertex and distance
    '''
    def minNewHeapNode(self, vertex, distance):
        minHeapNode = [vertex, distance]
        return minHeapNode

    # Function to swap nodes
    '''
    Input: Position for which element are to be swapped
    '''
    def swapNodes(self, first, second):
        self.array[first], self.array[second] = self.array[second], self.array[first]

    # Function to maintain minmum heap invariant in the heap for given position
    # also updates the new positions of the elements in the position array
    '''
    Input: Position to be heapified
    '''
    def minHeapify(self, position):

        parent = position
        leftChild = 2*parent
        rightChild = 2*parent + 1

        # Swap with the left child if less than parent and exists
        if (leftChild <= self.size) and (self.array[leftChild][1] < self.array[parent][1]):
            parent = leftChild
        
        # Swap with right child if less than parent and exists
        if (rightChild <= self.size) and (self.array[rightChild][1] < self.array[parent][1]):
            parent = rightChild

        # If original positions were changed
        if parent != position:
            # Swap positions
            self.location[self.array[parent][0]] = position
            self.location[self.array[position][0]] = parent
            # Swap nodes
            self.swapNodes(position, parent)
            self.minHeapify(parent)

    # Function to check if the heap is empty is not
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    # Function to extract minimum node from the heap
    def extractMinimum(self):

        # Return null if heap is empty
        if self.isEmpty() == True:
            return

        # Store root node
        root = self.array[self.FRONT]

        # Replace root node with the last node
        lastNode = self.array[self.size]
        self.array[self.FRONT] = lastNode

        # Update position of the last node
        self.location[lastNode[0]] = self.FRONT
        self.location[root[0]] = self.size

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(self.FRONT)

        return root

    # Function to decrease the key of elements in heap
    '''
    Input: Vertex and distance
    '''
    def decreaseKey(self, vertex, distance):

        # Get the position of vertex in heap
        position = self.location[vertex]

        # Get the node and update its distance value
        self.array[position][1] = distance

        # Travel up while the complete tree is not heapified [O(logn)]
        while position > 1 and self.array[position][1] < self.array[position // 2][1]:
            # Swap node and it's position with its parent
            self.location[self.array[position][0]] = position // 2
            self.location[self.array[position//2][0]] = position
            self.swapNodes(position, position//2)
            position = position//2

    # Function to check if a vertex is in minimum heap or not
    '''
    Input: Vertex to be checked
    Output: Boolean - True or False
    '''
    def isInHeap(self, vertex):
        if self.location[vertex] <= self.size:
            return True
        else:
            return False



# Class to create graph and implement djikstra's algorithm
class Graph():
    
    # Function to initialise values for graph
    def __init__(self, numVertices):
        self.vertices = numVertices
        self.graph = defaultdict(list)

    # Function to get data from the file
    '''
    Input: File containing data
    Output: Populates the graph array
    '''
    def getInput(self, filename):
        with open(filename, 'r') as data:
            for line in data:
                arr = [x for x in line.split("\t") if x != "\n"]
                key = int(arr[0])
                elements = list(map(lambda x: x.split(","), arr[1:]))
                self.graph[key] = [list(map(int,x)) for x in elements]

    # Function to calculate shortest distance using djikstra's algorithm
    '''
    Input: Source vertex
    Ouptut: Distance from source vertex to every vertex
    '''
    def djikstra(self, source):
        vertices = self.vertices
        distances = [None]

        minimumHeap = Heap(self.vertices)

        # Intialising minimum heap with all the edges and their distances
        for vertex in range(1, vertices+1):
            distances.append(float("inf"))
            minimumHeap.array.append(minimumHeap.minNewHeapNode(vertex, distances[vertex]))
            minimumHeap.location.append(vertex)

        # Make distance value of source vertex as 0 so that it is processed first
        minimumHeap.location[source] = minimumHeap.FRONT
        distances[source] = 0
        minimumHeap.decreaseKey(source, distances[source])

        # Initialise size of minimum heap
        minimumHeap.size = vertices

        # Following loop minimum heap contains all the nodes whose distance
        # is not yet finalised
        while minimumHeap.isEmpty() == False:

            # Extract the vertex with minimum distance value
            newHeapNode = minimumHeap.extractMinimum()
            element = newHeapNode[0]

            # Traverse through all the adjacent nodes and update their distances
            for node in self.graph[element]:
                adjacentNode = node[0]

                # If node is still in heap and distance to adjacent node from the element
                # is less than its previously calculated distance
                if (
                    (minimumHeap.isInHeap(adjacentNode) and distances[element] != float("inf")) and
                    ((node[1] + distances[element]) < distances[adjacentNode])
                ):
                    distances[adjacentNode] = node[1] + distances[element]

                    # Update distance value in heap
                    minimumHeap.decreaseKey(adjacentNode, distances[adjacentNode])

        return distances






## ---------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    graph = Graph(200)
    graph.getInput("djikstras.txt")

    answers = []
    for key in [7,37,59,82,99,115,133,165,188,197]:
        answers.append(graph.djikstra(1)[key])

    print("\n",",".join(map(str, answers)),"\n")
    
    

    

    






        




    


