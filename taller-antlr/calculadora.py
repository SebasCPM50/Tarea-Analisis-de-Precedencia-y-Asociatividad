import sys
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor

# Clase que dice cómo resolver las operaciones matemáticas
class MiVisitor(CalculadoraVisitor):
    
    # resultado de la expresión principal
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitNumero(self, ctx):
        return int(ctx.INT().getText()) # Convierte el texto del token a un número real

    def visitSuma(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitResta(self, ctx):
        return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))

    def visitMultiplicacion(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitDivision(self, ctx):
        return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))

def main():
    # PRUEBA
    texto = "2 + 3 * 4"
    print(f"Expresión: {texto}")

    # LEXER: Lee el texto y saca los tokens
    lexer = CalculadoraLexer(InputStream(texto))
    stream = CommonTokenStream(lexer)

    # PARSER: Usa los tokens para armar el árbol sintáctico
    parser = CalculadoraParser(stream)
    arbol = parser.prog()

    # Semántica: Recorre el árbol y calcula el resultado
    visitor = MiVisitor()
    resultado = visitor.visit(arbol)

    print(f"Resultado: {resultado}")

if __name__ == '__main__':
    main()
