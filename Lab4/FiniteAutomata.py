class FiniteAutomata:
    def __init__(self):
        self.__states = []
        self.__alphabet = []
        self.__transitions = []
        self.__initialState = ""
        self.__finalStates = []

    def readFile(self, fileName):
        file = open(fileName, "r")
        lines = file.readlines()

        self.__states = lines[0].split()
        self.__alphabet = lines[1].split()
        self.__transitions = lines[2].split(';')
        self.__initialState = lines[3]
        self.__finalStates = lines[4].split()

    def getStates(self):
        return self.__states

    def getAlphabet(self):
        return self.__alphabet

    def getTransitions(self):
        return self.__transitions

    def getInitialState(self):
        return self.__initialState

    def getFinalStates(self):
        return self.__finalStates
