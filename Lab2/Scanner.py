from SymbolTable import SymbolTable
import re

class Scanner:
    def __init__(self):
        self.__symbolTable = SymbolTable()
        self.__pif = []
        self.__keywords = ["if", "then", "else", "for", "do", "while", "int",
                           "char", "string", "float", "bool"]
        self.__operators = [">", "<", "=", "<=", ">=", "!=", "+", "-", "/", "*"]
        self.__separators = ["(", ")", ";", " "]

    def printST(self):
        self.__symbolTable.print()

    def isIdentifier(self, token):
        return re.match(r'[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def isConstant(self, token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def isInOperator(self, char):
        for operator in self.__operators:
            if char in operator:
                return True
        return False

    def buildOperatorToken(self, line, index):
        token = ''

        while index < len(line) and self.isInOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def buildStringToken(self, line, index):
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\"':
                quotes += 1
                index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        tokens = []
        index = 0

        while index < len(line):
            if self.isInOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.buildOperatorToken(line, index)
                tokens.append(token)
                token = ''
            elif line[index] == '\"':
                if token:
                    tokens.append(token)
                token, index = self.buildStringToken(line, index)
                tokens.append(token)
                token = ''
            elif line[index] in self.__separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def clasifyTokens(self, tokens):
        for token in tokens:
            if self.isConstant(token):
                self.__symbolTable.add(token)
                self.__pif.append(("id",self.__symbolTable.searchPosition(token)))
            elif self.isInOperator(token):
                self.__symbolTable.add(token)
                self.__pif.append(("id", self.__symbolTable.searchPosition(token)))
            elif token not in self.__separators:
                self.__pif.append((token,0))

        '''
        
print (max + "is the maximum")
        '''

    def readFile(self, fileName):
        file = open(fileName, "r")
        tokens=[]
        lineIndex= 0
        for line in file:
            lineTokens = self.tokenize(line)
            tokens.append((lineTokens, lineIndex))
            self.clasifyTokens(lineTokens)
            lineIndex+=1

        return tokens

    def populatePifFile(self):
        file = open("pif.out", "w")
        file.close()
        file = open("pif.out", "a")
        for pair in self.__pif:
            file.write(str(pair[0])+" "+str(pair[1])+"\n")

        file.close()


