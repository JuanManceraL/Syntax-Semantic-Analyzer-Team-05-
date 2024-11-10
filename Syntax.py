import ply.yacc as yacc
import math
from Lexer_ayuda import tokens

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

symbol_table = {}

def p_program(p):
    """statements   : statements statement
                    | statement"""
    print(f"P <- S")
    #print(p[1])

#def p_declaration(p):
#    """declaration"""

def p_statement(p):
    """statement    : declaration
                    | statement assignment
                    | statement prt"""
    print(f"S <- S")
    #p[0] = p[1]

def p_declaration(p):
    """declaration  : TYPE IDENTIFIER SEMIC
                    | TYPE IDENTIFIER EQUALS expression SEMIC"""
    var_name = p[2]
    if var_name in symbol_table:
        print(f"Error: La variable '{var_name}' ya fue declarada.")
    else:
        symbol_table[var_name] = None
        if p[3] == '=':
            print(f"Declaración y asignación: {var_name}")
            print(f"D(S) <- {p[1]} {p[2]}{p[3]}{p[4]}{p[5]}")
        else:
            print(f"Declaración: {var_name}")
            print(f"D(S) <- {p[1]} {p[2]}{p[3]}")

def p_assignment(p):
    """assignment   : IDENTIFIER EQUALS expression SEMIC"""
    print(f"A(S) <- {p[1]}{p[2]}{p[3]}{p[4]}")
    var_name = p[1]
    if var_name not in symbol_table:
        print(f"Error: La variable '{var_name}' no está declarada.")
    else:
        symbol_table[var_name] = p[3]
        print(f"Asignación: {var_name} = {p[3]}")

def p_print(p):
    """prt  : PRINT LPAREN expression RPAREN SEMIC"""
    print(f"P(S) <- Imprimiendo... Printf({p[3]})")
    p[0] = p[1]

#Syntax for summ
def p_expression_plus(p):
    """expression   : expression PLUS term"""
    p[0] = p[1] + p[3]
    print(f"E <- {p[1]}{p[2]}{p[3]}")

def p_expression_minus(p):
    """expression   : expression MINUS term"""
    p[0] = p[1] - p[3]
    print(f"E <- {p[1]}{p[2]}{p[3]}")

def p_term_times(p):
    """term : term TIMES factor"""
    p[0] = p[1] * p[3]
    print(f"T <- {p[1]} * {p[3]}")

def p_term_div(p):
    """term : term DIVIDE factor"""
    p[0] = p[1] / p[3]
    print(f"T <- {p[1]} / {p[3]}")

def p_factor_exp(p):
    """factor : EXP LPAREN factor value RPAREN"""
    print(f"Exponiendo {p[3]} a la {p[4]} = {p[3]**p[4]}")
    p[0] = p[3]**p[4]

def p_factor_sqr(p):
    """factor : SQR LPAREN factor RPAREN"""
    print(f"Raizcuadreando a {p[3]} = {math.sqrt(p[3])}")
    p[0] = math.sqrt(p[3])

def p_values_num(p):
    """value   : NUMBER"""
    p[0] = p[1]
    print(f"V <- N {p[1]}")

def p_expression_term(p):
    """expression   : term""" #expression
    p[0] = p[1]
    print(f"E <- T {p[1]}")

def p_term_factor(p):
    "term : factor"
    p[0] = p[1]
    print(f"T <- F {p[1]}")

def p_factor_value(p):
    "factor : value"
    p[0] = p[1]
    print(f"F <- V {p[1]}")

#def p_expression_term(p):
#    """expression : term"""
#    p[0] = p[1]

#def p_term_factor(p):
#    """term : factor"""
#    p[0] = p[1]

#Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

#Build the parser
parser = yacc.yacc()

"""
while True:
    try:
        s = input('calc > ')
    except EOFError: 
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
"""
#ruta_archivo = 'C:/Users/juanm/Documents/Escuela/7mo semestre/Compiladores/Syntax_Semantica_Analyzer_Team_5/ejemplo.c'
#if not os.path.isfile(ruta_archivo):
#    print("El archivo especificado no existe.")
#else:
"""

codigo = leer_archivo(ruta_archivo)
result = parser.parse(codigo)
print(result)
parser = yacc.yacc()
"""