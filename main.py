from pathlib import Path
from Syntax import parser

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

script_dir = Path(__file__).parent

input_file_name = "ejemplo.c"
input_file_dir = script_dir / input_file_name

#ruta_archivo = 'C:/Users/juanm/Documents/Escuela/7mo semestre/Compiladores/Syntax_Semantica_Analyzer_Team_5/Syntax-Semantic-Analyzer-Team-05-/ejemplo.c'
codigo = leer_archivo(input_file_dir)

# Ejecutar el analizador
parser.parse(codigo)
