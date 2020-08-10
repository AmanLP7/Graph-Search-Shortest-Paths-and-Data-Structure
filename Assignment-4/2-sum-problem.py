##########--------------------------------------------- 2 sum problem ----------------------------------------------##########

# Class to implement algorithm for 2 sum problem
class twoSum:

    # Initialising class variable
    def __init__(self):
        self.data = []
        self.sumDict = dict()

    # Function to import data from text file
    '''
    Input: Text file containing data
    Output: array of input data
    '''
    def importData(self, filename):
        with open(filename,"r") as file:
            for line in file:
                self.data.append(int(line.strip('\n')))

    # Function to check if there is a pair of integers which when summed together are equal 
    # to the given number
    '''
    Input: Expected sum of the pair of number
    Output: Pair of numbers
    '''
    def checkSum(self, number):
        for index, x in enumerate(self.data):
            self.sumDict[x] = index




if __name__ == "__main__":

    algorithm = twoSum()
    algorithm.importData("test.txt")
    algorithm.checkSum(5)
    print(algorithm.sumDict)
