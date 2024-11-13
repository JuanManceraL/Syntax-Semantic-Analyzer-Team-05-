from pathlib import Path
from Syntax import parser
import Syntax

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()
    
def guardar_resultados(nombre_archivo, data):
    output_dir = script_dir / "Outputs"
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / nombre_archivo
    with open(file_path, "w") as file:
        file.write(data)

script_dir = Path(__file__).parent

input_file_name = "ejemplo.c"
input_file_dir = script_dir / input_file_name

#ruta_archivo = 'C:/Users/juanm/Documents/Escuela/7mo semestre/Compiladores/Syntax_Semantica_Analyzer_Team_5/Syntax-Semantic-Analyzer-Team-05-/ejemplo.c'
codigo = leer_archivo(input_file_dir)

# Ejecutar el analizador
parser.parse(codigo)

guardar_resultados("SymbolTable_Updates.txt", Syntax.Upd_ST)
guardar_resultados("Reductions_List.txt", Syntax.Reduces)
guardar_resultados("Advertisements.txt", Syntax.Adv)