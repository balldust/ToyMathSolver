grammar Calc;

// PARSER

parse : (equation | assignment | comment) * EOF;

equation : arithmetic_expr EQ arithmetic_expr SEMICOLON  # EquationExpression ;

assignment : ID ASSIGN (NUMBER | SUB NUMBER) SEMICOLON;

comment: DOUBLESLASH * (ID+) * DOUBLESLASH;

arithmetic_expr
 : LPAREN arithmetic_expr RPAREN         # ArithmeticExpressionParens
 | arithmetic_expr (POW) arithmetic_expr  # ArithmeticExpressionPow
 | arithmetic_expr (MUL| DIV) arithmetic_expr  # ArithmeticExpressionMultDiv
 | arithmetic_expr (ADD | SUB) arithmetic_expr   # ArithmeticExpressionPlusMinus
 | numeric_entity                        # ArithmeticExpressionNumericEntity
 ;


numeric_entity : (NUMBER | SUB NUMBER)              # NumericConst
               | ID           # NumericVariable
               ;


// LEXER
// operators
POW : '^' ;
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

// logical
NEQ : '!=' ;
GE : '>=' ;
LE : '<=' ;
GT  : '>' ;
LT  : '<' ;
EQ  : '=' ;

// other
LPAREN : '(' ;
RPAREN : ')' ;
DOUBLESLASH : '//';


// literals
ID              : [a-zA-Z]+([0-9]+)?;  // match identifiers
NUMBER          : [0-9]+('.' [0-9]+)?;   // match integers
STRINGLITERAL   : '"' ~ ["\r\n]* '"' ;
DOLLAR          : '$' ;
NEWLINE         :'\r'? '\n' -> skip;  // return newlines to parser (end-statement signal)
WS              : [ \t]+ -> skip ; // toss out whitespace
SEMICOLON : ';';
ASSIGN : ':=';