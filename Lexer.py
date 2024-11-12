import ply.lex as lex
import os

# Lista de palabras clave (keywords) de C
keywords = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double',
    'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register',
    'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
    'union', 'unsigned', 'void', 'volatile', 'while', 'printf', 'scanf'
}

# Lista de tokens
tokens = [
    'KEYWORD', 'IDENTIFIER', 'PUNCTUATION', 'OPERATOR', 'CONSTANT', 'LITERAL', 'DIRECTIVE'
]


# Definición de literales (prioridad alta para capturar cualquier cosa entre comillas)
def t_LITERAL(t):
    r'\"(?:[^\\"]|\\.)*\"'
    return t


# Definición de las palabras reservadas
t_KEYWORD = r'\b(?:' + '|'.join(keywords) + r')\b'

# Definición para identificadores
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Definición de operadores
t_OPERATOR = r'[+\-*/%=<>!&|]+'

# Definición de puntuaciones
t_PUNCTUATION = r'[\(\)\[\]\{\},;:.]'

# Definición para números constantes (enteros y decimales)
t_CONSTANT = r'\b\d+(\\d+)?\b'


# Definición para directivas de preprocesador (e.g., #include, #define)
def t_DIRECTIVE(t):
    r'\#\s*(include|define|ifdef|ifndef|endif|undef|pragma)'
    return t


# Ignorar espacios y tabs
t_ignore = ' \t'


# Ignorar comentarios
def t_COMMENT(t):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
    pass


# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico: {t.value[0]}")
    t.lexer.skip(1)


# Construcción del lexer
lexer = lex.lex()


# Función para analizar el código y devolver las categorías solicitadas
def analizar_codigo(data):
    lexer.input(data)

    cont = 0
    keywords_set = set()
    identifiers = set()
    punctuation = set()
    operators = set()
    constants = set()
    literals = set()
    directives = set()

    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'KEYWORD':
            keywords_set.add(tok.value)
        elif tok.type == 'IDENTIFIER' and tok.value not in keywords_set:
            identifiers.add(tok.value)
        elif tok.type == 'PUNCTUATION':
            punctuation.add(tok.value)
        elif tok.type == 'OPERATOR':
            operators.add(tok.value)
        elif tok.type == 'CONSTANT':
            constants.add(tok.value)
        elif tok.type == 'LITERAL':
            literals.add(tok.value)
        elif tok.type == 'DIRECTIVE':
            directives.add(tok.value)
        cont += 1

    # Mostrar resultados
    print(f"Keyword: {' '.join(sorted(keywords_set))}")
    print(f"Identifier: {' '.join(sorted(identifiers))}")
    print(f"Punctuation: {' '.join(sorted(punctuation))}")
    print(f"Operator: {' '.join(sorted(operators))}")
    print(f"Constant: {' '.join(sorted(constants))}")
    print(f"Literal: {' '.join(sorted(literals))}")
    print(f"Directive: {' '.join(sorted(directives))}")
    print("Conteo de tokens: ", cont)


# Función para leer el código desde un archivo
def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()


# Función principal para seleccionar la entrada del usuario
def main():
    print("Selecciona el modo de entrada:")
    print("1. Introducir código manualmente")
    print("2. Leer desde un archivo")

#    
#    opcion = input("Ingresa el número de la opción (1 o 2): ")
#    if opcion == '1':
 #       print("Introduce el código a analizar (presiona Enter dos veces para finalizar):")
#        codigo = []
#        while True:
#            linea = input()
#            if linea == "":
#                break
#            codigo.append(linea)
#        codigo = "\n".join(codigo)  # Unir las líneas en un solo bloque de código
#    elif opcion == '2':
#        ruta_archivo = input("Ingresa la ruta del archivo (ej. archivo.c o archivo.txt): ")
#        if not os.path.isfile(ruta_archivo):
#            print("El archivo especificado no existe.")
#            return
#        codigo = leer_archivo(ruta_archivo)
#    else:
#        print("Opción no válida.")
##        return
    ruta_archivo = 'C:/Users/juanm/Documents/Escuela/7mo semestre/Compiladores/Syntax_Semantica_Analyzer_Team_5/Syntax-Semantic-Analyzer-Team-05-/ejemplo.c'
    if not os.path.isfile(ruta_archivo):
        print("El archivo especificado no existe.")
        return
    codigo = leer_archivo(ruta_archivo)
    
  #  codigo = "5+3"

    analizar_codigo(codigo)


if __name__ == "__main__":
    main()
