import LexicalAnalyzer

mem = []

def memCreate():
    for i in range(0, 57):
        mem.append(0)
def fetch(ch):
    return mem[getIndex(ch)]
def store(ch, value):
    mem[getIndex(ch)] = value
def getIndex(ch):
    if LexicalAnalyzer.isValidIdentifier(ch):
        return (ord(ch) - 65)
    else:
        raise ValueError(str(ch) + ' is not a valid identifier')