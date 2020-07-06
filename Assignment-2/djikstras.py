#####--------------------------- Djikstra's algorithm ---------------------------#####

# Importing required modules
import sys


# Class to create a heap data structure
class minimumHeap():

    # Initialising class variab
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.heap = [0]*(self.maxSize + 1)
        self.heap[0] = (0,-1*sys.maxsize)
        self.FRONT = 1


    # Function to return the position of parent node of node 
    # currently at given position
    '''
    Input: Position of the current node
    Output: Returns parent node position
    '''
    def parent(self, position):
        return position // 2


    # Function to return the position of left child 
    # of the node at given position
    '''
    Input: Position of the current node
    Output: Position of the left child
    '''
    def leftChild(self, position):
        return 2*position


    # Function to return the position of right child 
    # of the node at given position
    '''
    Input: Position of the current node
    Output: Position of the right child
    '''
    def rightChild(self, position):
        return (2*position) + 1


    # Function that return true if passed node 
    # is the leaf node
    '''
    Input: Position of the node
    Output: Whether or not the node is a leaf node
    '''
    def isLeaf(self, position):
        if position > (self.size//2) and position <= self.size:
            return True
        return False


    # Function to swap two nodes of the heap
    '''
    Input: Position of the nodes
    Output: None
    '''
    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]


    # Function to heapify the node at position
    '''
    Input: Postion of the node
    Output: Return new minimum heap
    '''
    def minHeapify(self, position):

        # If the node is non-leaf node and greater than any of its children
        if not self.isLeaf(position):
            if (
                (self.heap[position]["weight"] > self.heap[self.leftChild(position)]["weight"]) or 
                (self.heap[position]["weight"] > self.heap[self.rightChild(position)]["weight"])
                ): 

                # Swap with left child and heapify the left child
                if self.heap[self.leftChild(position)]["weight"] < self.heap[self.rightChild(position)]["weight"]:
                    self.swap(position, self.leftChild(position))
                    self.minHeapify(self.leftChild(position))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(position, self.rightChild(position))
                    self.minHeapify(self.rightChild(position))


    # Function to insert new node in the heap
    '''
    Input: Element to be inserted
    '''
    def insertElement(self, element, weight):

        if self.size > self.maxSize:
            return
        self.size += 1
        self.heap[self.size] = {"element": element, "weight": weight}
        print(self.heap[self.size]["weight"])
        currentPosition = self.size

        while self.heap[currentPosition]["weight"] < self.heap[self.parent(currentPosition)]["weight"]:
            self.swap(currentPosition, self.parent(currentPosition))
            currentPosition = self.parent(currentPosition)


    # Function to print contents of the heap
    def printHeap(self):
        for i in range(1, (self.size//2)+1):
            if (2*i+1) <= self.size:
                print(f"PARENT : {self.heap[i]} LEFT CHILD : {self.heap[2*i]} RIGHT CHILD : {self.heap[2*i + 1]}")
            else:
                print(f"PARENT : {self.heap[i]} LEFT CHILD : {self.heap[2*i]}")



    # Function to build minimum heap using minHeapify function
    def buildMinHeap(self):
        for position in range(self.size//2, 0, -1):
            self.minHeapify(position)

    
    # Function to remove and return the minimum element from the heap
    def removeMinElement(self):
        minElement = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)

        return minElement



# Class containing all the function to implement dijkstra's algorithm
class djikstrasAlgorithm():

    # Function to initialise parameters for heap and graph
    def __init__(self, numVertices):
        self.vertices = numVertices
        self.graph = [0]*(self.vertices + 1)
        self.color = ["red"]*(self.vertices + 1) # green = visited, red = not visited
        self.position = [0]*(self.vertices + 1) # position of node from graph in the heap


    # Function to get data from the filename
    '''
    Input: File containing data
    Output: Populates the graph array
    '''
    def getInput(self, filename):
        with open(filename, 'r') as data:
            for line in data:
                arr = [x for x in line.split("\t") if x != "\n"]
                index = int(arr[0])
                elements = list(map(lambda x: x.split(","), arr[1:]))
                self.graph[index] = [list(map(int,x)) for x in elements]

    # Function to define node for heap
    '''
    Input: Vertex and distance from the edge
    Output: Minimum heap node
    '''
    def minHeapNode(self, vertex, distance):
        return (vertex, self.maxLength)

    # Function to return the position of parent node of node 
    # currently at given position
    '''
    Input: Position of the current node
    Output: Returns parent node position
    '''
    def parent(self, position):
        return position // 2

    # Function to return the position of left child 

    # of the node at given position
    '''
    Input: Position of the current node
    Output: Position of the left child
    '''
    def leftChild(self, position):
        return 2*position


    # Function to return the position of right child 
    # of the node at given position
    '''
    Input: Position of the current node
    Output: Position of the right child
    '''
    def rightChild(self, position):
        return (2*position) + 1   
    

    # Function that return true if passed node 
    # is the leaf node
    '''
    Input: Position of the node
    Output: Whether or not the node is a leaf node
    '''
    def isLeaf(self, position):
        if position > (self.size//2) and position <= self.size:
            return True
        return False


    # Function to swap two nodes of the heap
    '''
    Input: Position of the nodes
    Output: None
    '''
    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]


    # Function to heapify the node at position
    '''
    Input: Postion of the node
    Output: Return new minimum heap
    '''
    def minHeapify(self, position):

        # If the node is non-leaf node and greater than any of its children
        if not self.isLeaf(position):
            if (
                (self.heap[position] > self.heap[self.leftChild(position)]) or 
                (self.heap[position] > self.heap[self.rightChild(position)])
                ): 

                # Swap with left child and heapify the left child
                if self.heap[self.leftChild(position)] < self.heap[self.rightChild(position)]:
                    self.swap(position, self.leftChild(position))
                    self.minHeapify(self.leftChild(position))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(position, self.rightChild(position))
                    self.minHeapify(self.rightChild(position))


    # Function to insert new node in the heap
    '''
    Input: Element to be inserted
    '''
    def insertElement(self, element):

        if self.size > self.maxSize:
            return
        self.size += 1
        self.heap[self.size] = element
        currentPosition = self.size

        while self.heap[currentPosition] < self.heap[self.parent(currentPosition)]:
            self.swap(currentPosition, self.parent(currentPosition))
            currentPosition = self.parent(currentPosition)

    # Function to build minimum heap using minHeapify function
    def buildMinHeap(self):
        for position in range(self.size//2, 0, -1):
            self.minHeapify(position)

    
    # Function to remove and return the minimum element from the heap
    def removeMinElement(self):
        minElement = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)

        return minElement





##--------------------------------------------------------------------------------------


if __name__ == "__main__":


    # Importing the data
    # algo = djikstrasAlgorithm(200)
    # algo.getInput("djikstras.txt")
    # print(algo.graph[6])

    # Adding edges to the heap
    heap = minimumHeap(15)
    heap.insertElement(5,2) 
    heap.insertElement(3,45) 
    heap.insertElement(17,55) 
    heap.insertElement(10,56) 
    heap.insertElement(84,9) 
    heap.insertElement(19,45) 
    heap.insertElement(6,23) 
    heap.insertElement(22,49) 
    heap.insertElement(9,90) 
    heap.buildMinHeap()
    heap.printHeap()

    print(f"\nThe minimum element is {heap.removeMinElement()}.\n")

