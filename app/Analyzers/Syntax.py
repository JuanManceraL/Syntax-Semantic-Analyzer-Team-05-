
import ply.yacc as yacc
import math
from .Lexer import tokens

symbol_table = {}
Reduces = ""
Upd_ST = ""
Adv = ""

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

def p_program(p):
    """program  : code
                | """
    saveMessages("Reduce", "P <- C")

def p_code(p):
    """code : code statement 
            | statement"""
    if(len(p) >= 3):
        saveMessages("Reduce", "C <- C S")
    else:
        saveMessages("Reduce", "C <- S")

def p_statement(p):
    """statement    : declaration
                    | assignment
                    | prt
                    | directives
                    | ifst""" 
    saveMessages("Reduce", "S <- S(esp)")

def p_directives(p):
    """directives  : NS DIRECTIVES LIBRARIES"""
    saveMessages("Advertisements",f"Incluyendo {p[1]}{p[2]} {p[3]}")
    saveMessages("Reduce", f"Dir(S) <- {p[1]}{p[2]} {p[3]}")

def p_declaration(p):
    """declaration  : TYPE IDENTIFIER SEMIC
                    | TYPE IDENTIFIER EQUALS expression SEMIC"""
    var_type = p[1]
    var_name = p[2]
    if var_name in symbol_table:
        print(f"Error: La variable '{var_name}' ya fue declarada.")
        raise SystemExit
    
    if len(p) > 4 and p[3] == '=':
        if p[4] == None:
            print(f"Error: No se puede asignar un valor nulo a una variable")
            raise SystemExit
        elif (p[1] == 'int'):
            valueNum = abs(p[4])
            if (valueNum - int(valueNum) != 0):
                print(f"Error: No se puede asignar un flotante en una variable entera")
                raise SystemExit
            else:
                symbol_table[var_name] = {'Identifier': var_name, 'Type': var_type, 'Value': int(p[4])}
                saveMessages("Advertisements",f"Declaración y asignación: {var_name} = {int(p[4])}")
                saveMessages("Reduce", f"D(S) <- {p[1]} {p[2]}{p[3]}{p[4]}{p[5]}")
                print_symbol_table()
        else:   
            symbol_table[var_name] = {'Identifier': var_name, 'Type': var_type, 'Value': p[4]}
            saveMessages("Advertisements", f"Declaración y asignación: {var_name} = {p[4]}")
            saveMessages("Reduce", f"D(S) <- {p[1]} {p[2]}{p[3]}{p[4]}{p[5]}")
            print_symbol_table() 
    else:
        symbol_table[var_name] = {'Identifier': var_name, 'Type': var_type, 'Value': None}
        saveMessages("Advertisements", f"Declaración: {var_name}")
        saveMessages("Reduce", f"D(S) <- {p[1]} {p[2]}{p[3]}")
        print_symbol_table()  

def p_assignment(p):
    """assignment   : IDENTIFIER EQUALS expression SEMIC"""
    saveMessages("Reduce", f"A(S) <- {p[1]}{p[2]}{p[3]}{p[4]}")
    var_name = p[1]
    if var_name not in symbol_table:
        print(f"Error: La variable '{var_name}' no está declarada.")
        raise SystemExit
    else:
        valueNum = abs(p[3])
        if (symbol_table[var_name]['Type'] == 'int'):
            if (valueNum - int(valueNum) != 0):
                print(f"Error: No se puede asignar un flotante en una variable entera")
                raise SystemExit
            else:
                symbol_table[var_name]['Value'] = int(p[3])
                saveMessages("Advertisements", f"Asignación: {var_name} = {int(p[3])}")
                print_symbol_table()
        else:
            symbol_table[var_name]['Value'] = p[3]
            saveMessages("Advertisements", f"Asignación: {var_name} = {p[3]}")
            print_symbol_table()
            

def p_print(p):
    """prt  : PRINT LPAREN expression RPAREN SEMIC"""
    saveMessages("Reduce", f"P(S) <- Imprimiendo... Printf({p[3]})")
    saveMessages("Advertisements", f"Imprimiendo... Printf({p[3]})")
    p[0] = p[1]

def p_if(p):
    """ifst : IF LPAREN valbool RPAREN OCURLB program CCURLB
            | IF LPAREN valbool RPAREN OCURLB program CCURLB ELSE OCURLB program CCURLB"""
    saveMessages("Advertisements", "Cierre de un if")
    saveMessages("Reduce", f"ifst(S) <- {p[1]}{p[2]}{p[3]}{p[4]}")

#Syntax for summ
def p_expression_plus(p):
    """expression   : expression PLUS term"""
    if((p[1] != None) and ((p[3] != None))):
        p[0] = p[1] + p[3]
        saveMessages("Reduce", f"E <- {p[1]}{p[2]}{p[3]}")
    else:
        print(f"Error: No se pueden sumar variables nulas")
        raise SystemExit

def p_expression_minus(p):
    """expression   : expression MINUS term"""
    if((p[1] != None) and ((p[3] != None))):
        p[0] = p[1] - p[3]
        saveMessages("Reduce", f"E <- {p[1]}{p[2]}{p[3]}")
    else:
        print(f"Error: No se pueden restar variables nulas")
        raise SystemExit
    

def p_term_times(p):
    """term : term TIMES factor"""
    if((p[1] != None) and ((p[3] != None))):
        p[0] = p[1] * p[3]
        saveMessages("Reduce", f"T <- {p[1]} * {p[3]}")
    else:
        print(f"Error: No se pueden multiplicar variables nulas")
        raise SystemExit
    

def p_term_div(p):
    """term : term DIVIDE factor"""
    if((p[1] != None) and ((p[3] != None))):
        p[0] = p[1] / p[3]
        saveMessages("Reduce", f"T <- {p[1]} / {p[3]}")
    else:
        print(f"Error: No se pueden dividir variables nulas")
        raise SystemExit
    
def p_factor_exp(p):
    """factor : EXP LPAREN factor value RPAREN"""
    if((p[3] != None) and ((p[4] != None))):
        saveMessages("Advertisements", f"Elevando {p[3]} a la {p[4]} = {p[3]**p[4]}")
        saveMessages("Reduce", f"F <- {p[1]}{p[2]}{p[3]} {p[4]}{p[5]}")
        p[0] = p[3]**p[4]
    else:
        print(f"Error: No se pueden elevar a la potencia variables nulas")
        raise SystemExit
    

def p_factor_sqr(p):
    """factor : SQR LPAREN factor RPAREN"""
    if(p[3] != None):
        saveMessages("Advertisements", f"Raiz cuadrada de {p[3]} = {math.sqrt(p[3])}")
        saveMessages("Reduce", f"F <- {p[1]}{p[2]}{p[3]}{p[4]}")
        p[0] = math.sqrt(p[3])
    else:
        print(f"Error: No se pueden elevar a la potencia variables nulas")
        raise SystemExit
    

def p_values_num(p):
    """value   : NUMBER"""
    p[0] = p[1]
    saveMessages("Reduce", f"V <- N {p[1]}")

def p_value_bool(p):
    """ valbool     : VAL_BOOL
                    | LPAREN valbool RPAREN
                    | expression OP_BOOL expression"""
    if (p[1] == 'True' or p[1] == 'False'):
        Val = p[1]
    elif p[2] == '<':
        Val = p[1] < p[3]
    elif p[2] == '>':
        Val = p[1] > p[3] 
    elif (p[2] == '<='):
        Val = p[1] <= p[3] 
    elif (p[2] == '>='):
        Val = p[1] >= p[3] 
    elif (p[2] == '=='):
        Val = p[1] == p[3] 
    else:
        Val = p[2]
    p[0] = Val
    saveMessages("Reduce", f"V <- B {Val}")

def p_expression_term(p):
    """expression   : term""" 
    p[0] = p[1]
    saveMessages("Reduce", f"E <- T {p[1]}")

def p_term_factor(p):
    "term : factor"
    p[0] = p[1]
    saveMessages("Reduce", f"T <- F {p[1]}")

def p_factor_value(p):
    """factor   : value
                | IDENTIFIER
                | LPAREN expression RPAREN
                | MINUS factor"""
    if p[1] == '-':
        p[0] = (-1)*p[2]
        saveMessages("Reduce", f"F <- V {p[2]}")
    elif p[1] == '(':
        p[0] = p[2]
        saveMessages("Reduce", f"F <- V {p[2]}")
    elif not str(p[1])[0].isnumeric():
        var_name = p[1]
        if not var_name in symbol_table:
            print(f"Error: La variable '{var_name}' no existe declarada.")
            raise SystemExit
        else:
            ref_val = symbol_table[var_name]['Value']
            p[0] = ref_val
            saveMessages("Reduce", f"F <- Var_val {ref_val}")
    else:
        p[0] = p[1]
        saveMessages("Reduce", f"F <- V {p[1]}")

#Error rule for syntax errors
def p_error(p):
    saveMessages("Advertisements", "Syntax error in input!")
    print("Syntax error in input!")
    if p:
        print(f"Error de sintaxis en '{p.value}'")
        raise SystemExit
    else:
        print("Error de sintaxis al final de la entrada")
        raise SystemExit

def print_symbol_table():
    saveMessages("Symbol Table", "\n\nTabla de Símbolos:")
    saveMessages("Symbol Table", "{:<15} {:<10} {:<10}".format("Identificador", "Tipo", "Valor"))
    saveMessages("Symbol Table", "-" * 35)    
    for var_name, attributes in symbol_table.items():

        if isinstance(attributes, dict):
            var_type = attributes.get("Type", "N/A")
            var_value = attributes.get("Value", "N/A")
        else:
            
            var_type = "N/A"
            var_value = str(attributes)  
        
        if var_value is None:
            var_value = "N/A"

        saveMessages("Symbol Table", "{:<15} {:<10} {:<10}".format(var_name, var_type, var_value))
    saveMessages("Symbol Table", "-" * 35)

def saveMessages(Type, Message):
    global Upd_ST, Adv, Reduces
    match Type: 
        case "Advertisements":
            Adv += Message + "\n"
        case "Reduce":
            Reduces += Message + "\n"
        case "Symbol Table":
            Upd_ST += Message + "\n"

#Build the parser
parser = yacc.yacc()
