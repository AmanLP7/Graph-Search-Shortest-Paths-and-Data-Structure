##--------------------- Program to implement median management using heap --------------------##

from datetime import datetime

# Class implementing heap data structure which supports extracting minimum element
# in O(logn) time
class minimumHeap():

    # Function to initialise heap data structure
    def __init__(self, numVertices):
        self.maxSize = numVertices 
        self.heap = [0]*(self.maxSize + 1)
        self.heap[0] = -1*float("inf")
        self.size = 0
        self.FRONT = 1

    # Function to swap nodes
    '''
    Input: Position for which element are to be swapped
    '''
    def swapNodes(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]


    # Function to define new node in a minimum heap
    '''
    Input: Vertex
    Output: New node as a list containing vertex
    '''
    def insertNode(self, element):

        if self.size > self.maxSize:
            return
        self.size += 1
        self.heap[self.size] = element
        currentPosition = self.size
        parent = currentPosition // 2

        while self.heap[currentPosition] < self.heap[parent]:
            self.swapNodes(currentPosition, parent)
            currentPosition = parent
            parent = currentPosition // 2

    

    # Function to maintain minmum heap invariant in the heap for given position
    '''
    Input: Position to be heapified
    '''
    def minHeapify(self, position):

        parent = position
        leftChild = 2*parent
        rightChild = 2*parent + 1

        # Swap with the left child if less than parent and exists
        if (leftChild <= self.size) and (self.heap[leftChild] < self.heap[parent]):
            parent = leftChild
        
        # Swap with right child if less than parent and exists
        if (rightChild <= self.size) and (self.heap[rightChild] < self.heap[parent]):
            parent = rightChild

        # If original positions were changed
        if parent != position:
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
        root = self.heap[self.FRONT]

        # Replace root node with the last node
        lastNode = self.heap[self.size]
        self.heap[self.FRONT] = lastNode

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(self.FRONT)

        return root



##------------------------------------------------------------------------------------------------------------------------

# Class to implement median management using heaps
class medianManagement:

    # Function to intialise variables for the class
    def __init__(self, length):
        self.length = length
        self.highHeap = minimumHeap(length)
        self.lowHeap = minimumHeap(length)
        self.data = []

    # Function read input file as a stream of numbers
    '''
    Input: Filename
    Output: Data as list
    '''
    def inputData(self, filename = "median.txt"):
        with open(filename, "r") as file:
            for line in file:
                self.data.append(int(line.strip("\n")))
        return self.data

    # Function to find median of set of numbers after each iteration
    '''
    Input: Data
    Output: sum of median at each step modulo 10000
    '''
    def findMedian(self, filename = "test.txt"):

        numbers = self.inputData(filename)
        medians = 0
        FRONT = 1

        for number in numbers:

            # If both the heaps are balanced
            if abs(self.highHeap.size - self.lowHeap.size) <= 2:
                if (number > -(self.lowHeap.heap[FRONT])) and (number > self.highHeap.heap[FRONT]):
                    self.highHeap.insertNode(number)
                elif (number > -self.lowHeap.heap[FRONT]) and (number < self.highHeap.heap[FRONT]):
                    self.lowHeap.insertNode(-number)
                else:
                    self.lowHeap.insertNode(-number)
            
                while abs(self.highHeap.size - self.lowHeap.size) > 1:
                    if self.lowHeap.size < self.highHeap.size:
                        element = self.highHeap.extractMinimum()
                        self.lowHeap.insertNode((-1)*element)
                    elif self.lowHeap.size > self.highHeap.size:
                        element = self.lowHeap.extractMinimum()
                        self.highHeap.insertNode((-1)*element)

                if self.highHeap.size > self.lowHeap.size:
                    medians += self.highHeap.heap[FRONT]
                else:
                    medians += (-1)*self.lowHeap.heap[FRONT]

        
        return(f"median -> {medians % 10000}")






##------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    median = medianManagement(10000)
    frames = median.findMedian(filename="median.txt")
    start = datetime.now()
    print("\n",frames)
    print(f"\nTotal time taken = {datetime.now()-start}\n")

   
   