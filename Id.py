import Memory
import LexicalAnalyzer

class Id:
    def __init__(self, ch):
        if LexicalAnalyzer.isValidIdentifier(ch):
            self.ch = ch
        else:
            raise ValueError("character is not a valid identifier")
    def evaluate(self):
        return Memory.fetch(self.ch)
    def getChar(self):
        return self.ch