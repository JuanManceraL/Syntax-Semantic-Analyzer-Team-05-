import ply.lex as lex

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

keywords = {
    'char', 'else', 'float', 'if', 'int', 'union', 'unsigned', 'void', 'volatile', 'while', 'printf', 'scanf', 'exp', 'sqr'
}

types = {
    'int', 'bool', 'float'
}

libraries = {
    'stdio.h', 'math.h'
}

directives = {
    'include'
}

val_bool = {
    'True', 'False'
}

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'OCURLB',
    'CCURLB',
    'SEMIC', 
    'TYPE',
    'EQUALS',
    'IDENTIFIER',
    'PRINT',
    'EXP',
    'SQR',
    'NS',
    'LIBRARIES',
    'DIRECTIVES',
    'IF',
    'ELSE',
    'VAL_BOOL',
    'OP_BOOL'
)

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_OCURLB    = r'\{'
t_CCURLB    = r'\}'
t_SEMIC     = r';'
t_EQUALS    = r'='
t_NS        = r'\#'
t_PRINT     = r'printf'
t_EXP       = r'exp'
t_SQR       = r'sqr'
t_IF        = r'if'
t_ELSE      = r'else'

t_TYPE      = r'\b(?:' + '|'.join(types) + r')\b'

#Aquí agregar todas las listas de palabras reservadas posibles
resserverWords = keywords | libraries | directives | types | val_bool

t_IDENTIFIER = r'(?!\b(?:' + '|'.join(resserverWords) + r')\b)[a-zA-Z_][a-zA-Z0-9_]*'
t_LIBRARIES = r'\b(?:' + '|'.join(libraries) + r')\b'
t_DIRECTIVES = r'\b(?:' + '|'.join(directives) + r')\b'
t_VAL_BOOL = r'\b(?:' + '|'.join(val_bool) + r')\b'
t_OP_BOOL = r'(<=|>=|==|<|>)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()



#ruta_archivo = 'C:/Users/juanm/Documents/Escuela/7mo semestre/Compiladores/Syntax_Semantica_Analyzer_Team_5/ejemplo.c'
#codigo = leer_archivo(ruta_archivo)

#lexer.input(codigo)
