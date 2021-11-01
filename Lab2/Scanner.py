import SymbolTable
import re

#0.5p
class Scanner:
    def __init__(self):
        self.symbolTable = SymbolTable
        self.pif = []
        self.identifiers = []
        self.tokens = ["if", "then", "for", "do", "while", ".", ";", ">", "<", "=", "<=", ">=", "!=", "(", ")", "int",
                       "char", "string", "float", "bool", "+", "-", "/", "*"]
        self.constants = []

    def isIdentifier(self, token):
        return re.match(r'[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def isConstant(self, token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def readProgram(self, fileName):
        file = open(fileName, "r")

        for line in file:
            splittedLine = line.split(" ")
            for element in splittedLine:
                if element not in self.tokens:
                    if self.isConstant(element):
                        self.constants.append(element)
                    if self.isIdentifier(element):
                        self.identifiers.append(element)

