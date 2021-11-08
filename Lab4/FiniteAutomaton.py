class FiniteAutomaton:
    def __init__(self):
        self.__states = []
        self.__alphabet=[]
        self.__transitions=""
        self.__initialState=""
        self.__finalStates=[]

    def readFile(self, fileName):
        file = open(fileName, "r")
        lines = file.readlines()

        self.__states=lines[0].split()
        self.__alphabet=lines[1].split()
        self.__transitions=lines[2]
        self.__initialState=lines[3]
        self.__finalStates=lines[4].split()

    def printStates(self):
        print(self.__states)

if __name__=="__main__":
    fa = FiniteAutomaton()
    fa.readFile("fa.in")
    fa.printStates()

    while True:
        print("\tMenu:")
        print("1.Print states")

