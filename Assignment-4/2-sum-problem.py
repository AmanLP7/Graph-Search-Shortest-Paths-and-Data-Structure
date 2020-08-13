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
    Output: array of sorted input data
    '''
    def importData(self, filename):
        with open(filename,"r") as file:
            for line in file:
                self.data.append(int(line.strip('\n')))
                self.data.sort()


    # Function to implement binary search
    '''
    Input: Key to look for
    Output: Index or False if element is not found in the array
    '''
    def binaryIntervalSearch(self, key, bound = "upper"):
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

        # Returning intervals if key not found
        if bound == "upper":
            return max(low,0)
        elif bound == "lower":
            return max(high,0)
        


    # Function to check if there is a pair of integers which when summed together are equal 
    # to the given number
    '''
    Input: Expected sum of the pair of number
    Output: Pair of numbers
    '''
    def checkSum(self):
        
        for x in self.data:
            upper = self.binaryIntervalSearch(-10000-x, "upper")
            lower = self.binaryIntervalSearch(10000-x, "lower")
            print(f"upper bound for {-10000-x} = {upper}, lower bound for {10000-x} = {lower}\n")
            break





if __name__ == "__main__":

    algorithm = twoSum()
    algorithm.importData("test.txt")
    start = datetime.now()
    print("\n",algorithm.data,"\n")
    algorithm.checkSum()
