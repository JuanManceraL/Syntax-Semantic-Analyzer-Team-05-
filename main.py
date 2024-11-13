from Syntax import parser
def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

ruta_archivo = 'C:/Users/juanm/Documents/Escuela/7mo semestre/Compiladores/Syntax_Semantica_Analyzer_Team_5/Syntax-Semantic-Analyzer-Team-05-/ejemplo.c'
codigo = leer_archivo(ruta_archivo)

# Ejecutar el analizador
parser.parse(codigo)
