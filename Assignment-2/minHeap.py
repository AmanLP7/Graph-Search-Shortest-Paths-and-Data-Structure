##########---------------- Minimum heap in python ----------------##########

import sys

# Class to create a heap data structure

class minHeap():


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
    

    

