import Memory
from Parser import Parser
from LexicalAnalyzer import LexicalAnalyzer

def main():
    fileName = "C:\\Users\Bruce Houdini\PycharmProjects\PyLuaInterpreter\\test1.lua"
    p = Parser(fileName)
    p.parse()
    #test = LexicalAnalyzer(fileName)



if __name__ == "__main__":
    main()