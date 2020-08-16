##########------------------------------- 2 sum problem naive solution -----------------------------#############

# Function to import data from file
'''
Input: Data from text file
Output: Sorted list of numbers
'''
def importData(filename):
    data = []
    with open(filename,"r") as file:
        for line in file:
            data.append(int(line.strip('\n')))
            data.sort()

    return data

def checkSumNaive(data):

    uniqueSum = set()
    for number in [-648]:
        for x in data:
            y = number - x
            if y in data:
                print(x,y,number)
                uniqueSum.add(number)

    print(f"Length of set = {len(uniqueSum)}")
    print(uniqueSum)



if __name__ == "__main__":

    data = importData("test.txt")
    # print(data)
    checkSumNaive(data)


