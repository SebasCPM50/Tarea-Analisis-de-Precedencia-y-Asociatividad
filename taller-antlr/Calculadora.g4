grammar Calculadora;

// PARSER
prog: expr EOF ;

expr: expr '+' expr                   # Suma
    | <assoc=right> expr '-' expr     # Resta
    | expr '*' expr                   # Multiplicacion
    | expr '/' expr                   # Division
    | INT                             # Numero
    ;

// LEXER
INT: [0-9]+ ;
WS: [ \t\r\n]+ -> skip;
