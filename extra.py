import ply.yacc as yacc
from Lexer2 import tokens  # Importa los tokens del archivo lexer.py

# Tabla de símbolos
symbol_table = {}

# Reglas de producción
def p_program(p):
    '''program : statements'''
    print("Análisis completado.")
    print("1")

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    print("2")

def p_statement(p):
    '''statement : declaration'''
#    '''statement : declaration
#                 | assignment
#                 | expression SEM '''
    print("3")

def p_declaration(p):
    '''declaration : INT IDENTIFIER SEM'''
    var_name = p[2]
    if var_name in symbol_table:
        print(f"Error: La variable '{var_name}' ya fue declarada.")
    else:
        symbol_table[var_name] = None
        print(f"Declaración: {var_name}")
    print("4")

#def p_assignment(p):
#    '''assignment : IDENTIFIER OPERATOR CONSTANT ';' '''
#    var_name = p[1]
#    if var_name not in symbol_table:
#        print(f"Error: La variable '{var_name}' no está declarada.")
#    else:
#        symbol_table[var_name] = p[3]
#        print(f"Asignación: {var_name} = {p[3]}")

#def p_expression(p):
#    '''expression : IDENTIFIER
#                  | CONSTANT
#                  | IDENTIFIER OPERATOR IDENTIFIER
#                  | IDENTIFIER OPERATOR CONSTANT'''
#    # Esta producción permite expresiones aritméticas simples
#    print("Expresión reconocida.")

# Manejo de errores de sintaxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

# Construir el parser

#parser = yacc.yacc(start='program')
parser = yacc.yacc()
