# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#prog.
    def visitProg(self, ctx:CalculadoraParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Numero.
    def visitNumero(self, ctx:CalculadoraParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Suma.
    def visitSuma(self, ctx:CalculadoraParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Division.
    def visitDivision(self, ctx:CalculadoraParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Multiplicacion.
    def visitMultiplicacion(self, ctx:CalculadoraParser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Resta.
    def visitResta(self, ctx:CalculadoraParser.RestaContext):
        return self.visitChildren(ctx)



del CalculadoraParser