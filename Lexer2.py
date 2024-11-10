import ply.lex as lex

# Definición de palabras clave
keywords = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double',
    'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'long', 'register',
    'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
    'union', 'unsigned', 'void', 'volatile', 'while', 'printf', 'scanf'
}

# Lista de tokens
tokens = [
    'IDENTIFIER', 'CONSTANT', 'OPERATOR', 'PUNCTUATION', 'LITERAL', 'DIRECTIVE', 'KEYWORD','INT', 'SEM'
]# + [kw.upper() for kw in keywords]

# Reglas de expresión regular para tokens simples
t_OPERATOR = r'\+|-|=|\*|/'
t_PUNCTUATION = r'[\(\)\[\]\{\},;:.]'
t_DIRECTIVE = r'\#include|\#define'
t_LITERAL = r'\"(\\.|[^\"])*\"'  # Literales de cadena
t_KEYWORD = r'\b(?:' + '|'.join(keywords) + r')\b'
t_INT: r'int'
t_SEM: r';'

# Definición de identificadores y constantes
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in keywords:
        t.type = t.value.upper()  # Detecta si es palabra clave
        return t

def t_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico: Caracter no válido '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
