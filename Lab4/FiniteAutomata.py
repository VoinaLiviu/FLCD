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
        fileTransitions = lines[2].split(';')
        for fileTransition in fileTransitions:
            self.__transitions.append(fileTransition.split())
        self.__initialState = lines[3][0:2]
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

    def checkSequence(self, sequence):
        alphabet = self.getAlphabet()
        transitions = self.getTransitions()
        currentState = self.getInitialState()

        for element in sequence:
            if element not in alphabet:
                print("Element not from the alphabet!")
                return False
            nextState = "default"
            for transition in transitions:
                if transition[0] == currentState and transition[1] == element:
                    nextState = transition[2]
                    break
            if nextState != "default":
                currentState = nextState
            else:
                print("Invalid transition!")
                return False

        if currentState in self.getFinalStates():
            return True
        else:
            return False
