##########--------------------------------------------- 2 sum problem ----------------------------------------------##########

from datetime import datetime

# Class to implement algorithm for 2 sum problem
class twoSum:

    # Initialising class variable
    def __init__(self):
        self.data = []
        self.sumDict = dict()
        self.pairs = 0


    # Function to import data from text file
    '''
    Input: Text file containing data
    Output: array of input data
    '''
    def importData(self, filename):
        with open(filename,"r") as file:
            for line in file:
                self.data.append(int(line.strip('\n')))


    # Function to implement binary search
    '''
    Input: Key to look for
    Output: Index or False if element is not found in the array
    '''
    def binarySearch(self, key):
        low = 0
        high = len(self.data)-1
        middle = 0

        while low <= high:
            middle = (low + high) // 2
            # Check if the key is less than the middle element
            # or greater than middle element or equal to it.
            if self.data[middle] > key:
                high = middle - 1
            elif self.data[middle] < key:
                low = middle + 1
            else:
                return middle

        return False
        


    # Function to check if there is a pair of integers which when summed together are equal 
    # to the given number
    '''
    Input: Expected sum of the pair of number
    Output: Pair of numbers
    '''
    def checkSum(self):

        # Populating the hash table where key is the number in the array and 
        # index is the corresponding value
        for index, x in enumerate(self.data):
            self.sumDict[x] = index
        
        for x in self.data:
            for number in range(-10000,10001):
                if (number-x) in self.sumDict:
                    self.pairs += 1
        
        return (self.pairs // 2)




if __name__ == "__main__":

    algorithm = twoSum()
    algorithm.importData("test.txt")
    start = datetime.now()
    print(algorithm.checkSum())
    print(f"Total time taken = {datetime.now()-start}.")
