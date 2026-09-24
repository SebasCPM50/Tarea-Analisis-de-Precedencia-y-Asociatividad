# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#prog.
    def enterProg(self, ctx:CalculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#prog.
    def exitProg(self, ctx:CalculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Numero.
    def enterNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Numero.
    def exitNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Suma.
    def enterSuma(self, ctx:CalculadoraParser.SumaContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Suma.
    def exitSuma(self, ctx:CalculadoraParser.SumaContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Division.
    def enterDivision(self, ctx:CalculadoraParser.DivisionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Division.
    def exitDivision(self, ctx:CalculadoraParser.DivisionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Multiplicacion.
    def enterMultiplicacion(self, ctx:CalculadoraParser.MultiplicacionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Multiplicacion.
    def exitMultiplicacion(self, ctx:CalculadoraParser.MultiplicacionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Resta.
    def enterResta(self, ctx:CalculadoraParser.RestaContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Resta.
    def exitResta(self, ctx:CalculadoraParser.RestaContext):
        pass



del CalculadoraParser