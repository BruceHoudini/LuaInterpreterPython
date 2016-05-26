class Token:
    def __init__(self, lexeme, tokType):
        if lexeme == None or len(lexeme) < 0:
            raise ValueError("invalid lexeme argument")
        if tokType == None:
            #debug
            #print ("loop")
            #debug
            raise ValueError("invalid TokenType argument")
        self.lexeme = lexeme
        self.tokType = tokType

    def getLexeme(self):
        return self.lexeme
    def getTokType(self):
        return self.tokType