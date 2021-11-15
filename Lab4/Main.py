from UI import UI
from FiniteAutomata import FiniteAutomata

if __name__ == "__main__":
    finiteAutomata = FiniteAutomata()
    finiteAutomata.readFile("fa.in")
    ui = UI(finiteAutomata)

    while True:
        ui.displayMenu()
        choice = int(input("\n>>> "))
        if choice == 0:
            break
        elif choice == 1:
            ui.printStates()
        elif choice == 2:
            ui.printAlphabet()
        elif choice == 3:
            ui.printTransitions()
        elif choice == 4:
            ui.printInitialState()
        elif choice==5:
            ui.printFinalStates()
        elif choice==6:
            ui.checkSequence()
        else:
            print("Invalid choice! Check the menu!")
