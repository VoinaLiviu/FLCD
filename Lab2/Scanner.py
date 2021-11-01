import SymbolTable

class Scanner:
    def __init__(self):
        self.symbolTable = SymbolTable()
        self.pif = []
        self.identifiers = []
        self.tokens = ["if", "then", "for", "do", "while", ".", ";", ">", "<", "=", "<=", ">=", "!=", "(", ")", "int",
                       "char", "string", "float", "bool", "+", "-", "/", "*"]
        self.constants = []
