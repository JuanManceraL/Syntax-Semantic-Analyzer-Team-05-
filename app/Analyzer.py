from pathlib import Path
from Analyzers.Syntax import parser
import Analyzers.Syntax as Syntax

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()
    
def guardar_resultados(nombre_archivo, data):
    AppDir = script_dir.parent
    output_dir = AppDir / "Outputs"
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / nombre_archivo
    with open(file_path, "w") as file:
        file.write(data)

script_dir = Path(__file__).parent

#input_file_name = "ejemplo.c"
#input_file_dir = script_dir / input_file_name


def AnalizeArchive(input_file_dir):
    codigo = leer_archivo(input_file_dir)

    # Ejecutar el analizador
    parser.parse(codigo)

    guardar_resultados("SymbolTable_Updates.txt", Syntax.Upd_ST)
    guardar_resultados("Reductions_List.txt", Syntax.Reduces)
    guardar_resultados("Advertisements.txt", Syntax.Adv)

def AnalizeCode(txt):

    # Ejecutar el analizador
    parser.parse(txt)

    guardar_resultados("SymbolTable_Updates.txt", Syntax.Upd_ST)
    guardar_resultados("Reductions_List.txt", Syntax.Reduces)
    guardar_resultados("Advertisements.txt", Syntax.Adv)

def AnalizarELCodigo(txt):
    print(f"ola  {txt}")

def AnalizarArchivo(path):
    print(f"Adios   {path}")