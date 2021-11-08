from BST import BST


class SymbolTable:
    def __init__(self):
        self.bst = BST()
        self.position = 0

    def add(self, identifier):
        if not self.alreadyIn(identifier):
            info = [self.position, str(identifier)]
            self.bst.insert(info)
            self.position = self.position + 1

    def alreadyIn(self, identifier):
        return self.search(identifier) != None

    def search(self, identifier):
        return self.bst.search(str(identifier))

    def searchPosition(self, identifier):
        pair = self.bst.search(identifier)
        return pair[0]

    def print(self):
        self.bst.print()

if __name__ == "__main__":
    symbolTable = SymbolTable()

    symbolTable.add("r")
    symbolTable.add("r")
    symbolTable.add("n")
    symbolTable.add("b")
    symbolTable.add("f")
    symbolTable.add("a")
    symbolTable.add("h")
    symbolTable.add("g")

    symbolTable.print()
    print(symbolTable.search("a"))
