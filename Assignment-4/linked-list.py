############------------------------------------- Linked list in python ------------------------------#############

# Class to define node of a linked list
class node:

    # Function to initialise the node
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialise next pointer with null

# Class to define a linked list
class linkedList:

    # Function to initialise head
    def __init__(self):
        self.head = None

    # Function to print contents of linked list
    def printList(self):
        element = self.head
        while (element):
            print(element.data)
            element = element.next

##--------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Initialsing list
    lList = linkedList()

    lList.head = node(1)
    second = node(2)
    third = node(3)

    lList.head.next = second # Link first element to the second
    second.next = third # Link second element to the third

    lList.printList()

