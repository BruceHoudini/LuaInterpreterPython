from LexemeDictionary import lexDict
from Token import Token

class LexicalAnalyzer:
    def __init__(self, fileName):
        f = open(fileName)
        self.lexList = f.readline().strip("\n").strip("\t").split(" ")
        while self.lexList[-1] != '':
            self.lexList += f.readline().strip("\n").strip("\t").split(" ")
        f.close()
        #debug
        #print(self.lexList)
        #print(self.lexList[0])
        #debug
        self.tokenList = self.buildTokenList()

    def buildTokenList(self):
        newTokenList = []
        for i in range(0, len(self.lexList)):
            newTokenList.append(Token(self.lexList[i], lexDict(self.lexList[i])))
        return newTokenList

    def getNextToken(self):
        return self.tokenList.pop(0)

    def getLookaheadToken(self):
        return self.tokenList[0]

def isValidIdentifier(ch):
    checkAscii = ord(ch)
    return ((checkAscii >= 65 and checkAscii <= 90) or (checkAscii >= 97 and checkAscii <= 122))