class UI:
    def __init__(self, fa):
        self.__finiteAutomata = fa

    def displayMenu(self):
        print("\nMenu:")
        print("1. Print states")
        print("2. Print alphabet")
        print("3. Print transitions")
        print("4. Print initial state")
        print("5. Print final states")
        print("6. Check a sequence")
        print("0. Exit")

    def printStates(self):
        states = self.__finiteAutomata.getStates()
        printedString = "The finite automata's states are:"
        for state in states:
            printedString += "  "
            printedString += state

        print(printedString)

    def printAlphabet(self):
        alphabet = self.__finiteAutomata.getAlphabet()
        printedString = "The finite automata's alphabet is: {"
        for index in range(0, len(alphabet) - 1):
            printedString += alphabet[index]
            printedString += " "
        printedString += alphabet[len(alphabet) - 1]
        printedString += "}"

        print(printedString)

    def printTransitions(self):
        transitions = self.__finiteAutomata.getTransitions()
        print("The finite automata's transitions are:")
        for transition in transitions:
            transitionString = transition[0]
            transitionString += " -"
            transitionString += transition[1]
            transitionString += "-> "
            transitionString += transition[2]
            print("\t", transitionString)


    def printInitialState(self):
        initialState = self.__finiteAutomata.getInitialState()

        print("The finite automata's initial state is:", initialState)

    def printFinalStates(self):
        finalStates = self.__finiteAutomata.getFinalStates()
        printedString = "The finite automata's final states are:"
        for state in finalStates:
            printedString += " "
            printedString += state

        print(printedString)

    def checkSequence(self):
        sequence = input("Enter the sequence: ")
        result = self.__finiteAutomata.checkSequence(sequence)
        if result == True:
            print("The sequence is accepted by the DFA")
        else:
            print("The sequence is not accepted by the DFA")
