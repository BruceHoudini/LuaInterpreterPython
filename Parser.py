from BooleanExpression import BooleanExpression
from BinaryExpression import BinaryExpression
from LexicalAnalyzer import LexicalAnalyzer
from ParserException import ParserException
from Assignment import Assignment
from Constant import Constant
from Id import Id

class Parser:
    def __init__(self, fileName):
        self.lex = LexicalAnalyzer(fileName)

    def parse(self):
        tok = self.lex.getNextToken()
        if tok.getTokType() == "FUNCTION_TOK":
            tok = self.lex.getNextToken().getTokType()
            if tok == "ID_TOK":
                tok = self.lex.getNextToken().getTokType()
                if tok == "OPENP_TOK":
                    tok = self.lex.getNextToken().getTokType()
                    if tok == "CLOSEP_TOK":
                        self.getBlock()
                        tok = self.lex.getNextToken().getTokType()
                        if tok != "END_TOK":
                            raise ParserException("END expected")


                    else:
                            raise ParserException(") expected")
                else:
                        raise ParserException("( expected")
            else:
                    raise ParserException("ID expected")
        else:
                raise ParserException("FUNCTION expected")

    def getBlock(self):
        tok = self.lex.getLookaheadToken()
        if(tok.getTokType() != "EOS_TOK") and (tok.getTokType() != "END_TOK") and (tok.getTokType() != "UNTIL_TOK"):
            self.getStatement()
            self.getBlock()

    def getStatement(self):
        tok = self.lex.getLookaheadToken()
        if tok.getTokType() == "IF_TOK":
            self.resolveIf()
        elif tok.getTokType() == "WHILE_TOK":
            self.resolveWhile()
        elif tok.getTokType() == "REPEAT_TOK":
            self.resolveRepeat()
        elif tok.getTokType() == "PRINT_TOK":
            self.printState()
        elif tok.getTokType() == "ID_TOK":
            self.Assign()
        elif tok.getTokType() == "ELSE_TOK":
            return
        elif tok.getTokType() == "UNTIL_TOK":
            return
        else:
            raise ParserException("Statement expected")

    def resolveIf(self):
        tok = self.lex.getLookaheadToken()
        if self.getBooleanExpression().evaluate() == True:
            tok = self.lex.getNextToken()
            if tok.getTokType() == "THEN_TOK":
                self.getBlock()
                tok = self.lex.getNextToken()
                if tok.getTokType() == "ELSE_TOK":
                    while tok.getTokType() != "END_TOK":
                        tok = self.lex.getNextToken()
                    if tok.getTokType() == "END_TOK":
                        return

                else:
                    raise ParserException("ELSE expected")
            else:
                    raise ParserException("THEN expected")

        else:
            while tok.getTokType() != "ELSE_TOK":
                    tok = self.lex.getNextToken()
            self.getBlock()
            tok = self.lex.getNextToken()
            if tok.getTokType() == "END_TOK":
                return
            else:
                raise ParserException("END expected")

    def resolveWhile(self):
        whileCondition = self.getBooleanExpression()
        tok = self.lex.getNextToken()
        if tok.getTokType() == "DO_TOK":
            while whileCondition.evaluate() == True:
                save1 = self.lex.tokenList[:]
                self.getBlock()
                save2 = self.lex.tokenList[:]
                self.lex.tokenList = save1[:]

            self.lex.tokenList = save2[:]
            tok = self.lex.getNextToken().getTokType()

            if tok == "END_TOK":
                return
            else:
                raise ParserException("END expected")
        else:
            raise ParserException("DO expected")


    def resolveRepeat(self):
        save1 = self.lex.tokenList[:]
        self.lex.getNextToken()
        self.getBlock()
        repeatCondition = self.getBooleanExpression()
        if repeatCondition.evaluate() != True:
            self.lex.tokenList = save1[:]
            self.resolveRepeat()

    def printState(self):
        tok = self.lex.getNextToken()
        if tok.getTokType() != "PRINT_TOK":
            raise ParserException("PRINT expected")

        tok = self.lex.getNextToken()
        if tok.getTokType() == "OPENP_TOK":
            print (self.getExpression().evaluate())
            tok = self.lex.getNextToken()
            if tok.getTokType() != "CLOSEP_TOK":
                raise ParserException(") expected ")
        else:
            raise ParserException("( expected ")

    def Assign(self):
        var = self.getId()
        tok = self.lex.getNextToken()
        self.match(tok, "ASSIGN_TOK")
        expr = self.getExpression()
        Assignment(var, expr).execute()

    def getExpression(self):
        tok = self.lex.getLookaheadToken()
        if tok.getTokType() == "ADD_TOK" or tok.getTokType() == "MUL_TOK" or tok.getTokType() == "SUB_TOK" or tok.getTokType() == "DIV_TOK":
            expr = self.getBinaryExpression()
        elif tok.getTokType() == "ID_TOK":
            expr = self.getId()
        else:
            expr = self.getConstant()
        return expr

    def getBinaryExpression(self):
        tok = self.lex.getNextToken()
        if tok.getTokType() == "ADD_TOK":
            self.match(tok, "ADD_TOK")
            op = "ADD_OP"
        elif tok.getTokType() == "MUL_TOK":
            self.match(tok, "MUL_TOK")
            op = "MUL_OP"
        elif tok.getTokType() == "SUB_TOK":
            self.match(tok, "SUB_TOK")
            op = "SUB_OP"
        elif tok.getTokType() == "DIV_TOK":
            self.match(tok, "DIV_TOK")
            op = "DIV_OP"
        else:
            raise ParserException ("Operator expected.")
        expr1 = self.getExpression()
        expr2 = self.getExpression()
        return BinaryExpression(op, expr1, expr2)

    def getBooleanExpression(self):
        self.lex.getNextToken()
        tok = self.lex.getNextToken()
        if tok.getTokType() == "LE_TOK":
            self.match(tok, "LE_TOK")
            op = "LE_OP"
        elif tok.getTokType() == "LT_TOK":
            self.match(tok, "LT_TOK")
            op = "LT_OP"
        elif tok.getTokType() == "GE_TOK":
            self.match(tok, "GE_TOK")
            op = "GE_OP"
        elif tok.getTokType() == "GT_TOK":
            self.match(tok, "GT_TOK")
            op = "GT_OP"
        elif tok.getTokType() == "EQ_TOK":
            self.match(tok, "EQ_TOK")
            op = "EQ_OP"
        elif tok.getTokType() == "NE_TOK":
            self.match(tok, "NE_TOK")
            op = "NE_OP"
        else:
            raise ParserException ("Operator expected.")

        expr1 = self.getExpression()
        expr2 = self.getExpression()

        return BooleanExpression(op, expr1, expr2)

    def getId(self):
        tok = self.lex.getNextToken()
        self.match(tok, "ID_TOK")
        return Id(tok.getLexeme())

    def getConstant(self):
        tok = self.lex.getNextToken()
        self.match(tok, "CONST_TOK")
        value = int(tok.getLexeme())
        return Constant(value)

    def match(self, tok, tokType):
        if tok.getTokType() != tokType:
            raise ParserException ("Token of type " + tokType + "expected.")