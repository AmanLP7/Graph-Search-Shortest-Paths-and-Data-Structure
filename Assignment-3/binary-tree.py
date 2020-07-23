## ----------------------------------------------- Python implementation of binary tree ----------------------------------------------- ##

# Utility class to represent individual node in binary tree
class node:

    # Initialising node
    '''
    Input: Takes key as arguement and set it equals to the value of node
    '''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    # Function to implement insert operation from binary tree
    '''
    Input: Root node and the node to be inserted
    '''
    def insertNode(self, root, node):
        if root is None:
            root = node
        else:
            # Inserts on the right
            if root.value < node.value:
                if root.right is None:
                    root.right = node
                else:
                    self.insertNode(root.right, node)
            # Inserts on the left
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insertNode(root.left, node)

    # Function to perform tree traversal in ordered fashion
    '''
    Input: Root
    '''
    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.value)
            self.printTree(root.right)


##---------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    root = node(50)
    root.insertNode(root, node(30))
    root.insertNode(root, node(20))
    root.insertNode(root, node(40))
    root.insertNode(root, node(70))
    root.insertNode(root, node(60))
    root.insertNode(root, node(80))

    root.printTree(root)
