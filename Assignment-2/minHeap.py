##########---------------- Minimum heap in python ----------------##########

import sys

# Class to create a heap data structure
class minimumHeap():


    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.heap = [0]*(self.maxSize + 1)
        self.heap[0] = -1*sys.maxsize
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
        if position >= (self.size//2) and position <= self.size:
            return True
        return False


    # Function to swap two nodes of the heap
    '''
    Input: Position of the nodes
    Output: None
    '''
    def swap(self, first, second):
        self.heap[first], self.heap


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


    # Function to print contents of the heap
    def printHeap(self):
        for i in range(1, (self.size//2)+1):
            print(f"PARENT : {self.heap[i]} LEFT CHILD : {self.heap[2*i]} RIGHT CHILD : {self.heap[2*i + 1]}")


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


##-------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    print("\nThe minimum heap is .....\n")
    heap1 = minimumHeap(15)
    heap1.insertElement(5) 
    heap1.insertElement(3) 
    heap1.insertElement(17) 
    heap1.insertElement(10) 
    heap1.insertElement(84) 
    heap1.insertElement(19) 
    heap1.insertElement(6) 
    heap1.insertElement(22) 
    heap1.insertElement(9) 
    heap1.buildMinHeap()
    heap1.printHeap()



    

    

