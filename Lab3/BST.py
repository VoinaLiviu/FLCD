class Node:
    def __init__(self, v):
        self.__value = v
        self.__left = None
        self.__right = None

    def getValue(self):
        return self.__value

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self, right):
        self.__right = right

    def setLeft(self, left):
        self.__left = left

    def __str__(self):
        return str(self.__value)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, info):
        if self.root is None:
            self.root = Node(info)
        else:
            temp = None
            leftFlag = False
            node = self.root
            while node is not None:
                temp = node
                if node.getValue()[1] <= info[1]:
                    node = node.getLeft()
                    leftFlag = True
                elif node.getValue()[1] >= info[1]:
                    node = node.getRight()
                    leftFlag = False
            if leftFlag == True:
                temp.setLeft(Node(info))
            else:
                temp.setRight(Node(info))

    def search(self, value):
        if self.root is None:
            return None

        node = self.root
        while node is not None:
            if node.getValue()[1] > value:
                node = node.getLeft()
            elif node.getValue()[1] < value:
                node = node.getRight()
            else:
                return node.getValue()

    def printAlphabetically(self, root):
        if root:
            self.printAlphabetically(root.getRight())
            print(root.getValue())
            self.printAlphabetically(root.getLeft())



    def print(self):
        self.printAlphabetically(self.root)