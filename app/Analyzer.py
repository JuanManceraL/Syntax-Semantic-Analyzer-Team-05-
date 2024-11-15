from pathlib import Path
from Parser.Syntax import parser
import Parser.Syntax as Syntax

output = ""
path_Reduction = ""

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()
    
def guardar_resultados(nombre_archivo, data):
    AppDir = script_dir.parent
    output_dir = AppDir / "Outputs"
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / nombre_archivo
    global path_Reduction
    path_Reduction = output_dir / "Reductions_List.txt"
    with open(file_path, "w") as file:
        file.write(data)

script_dir = Path(__file__).parent

# Ejecutar el analizador
def AnalyzeArchive(input_file_dir):
    Syntax.rebootVariables()
    codigo = leer_archivo(input_file_dir)

    parser.parse(codigo)

    guardar_resultados("SymbolTable_Updates.txt", Syntax.Upd_ST)
    guardar_resultados("Reductions_List.txt", Syntax.Reduces)
    guardar_resultados("Advertisements.txt", Syntax.Adv)
    global output
    output = Syntax.Output
    SDTOutput = Syntax.Semantic_Errors
    if output == "Parsing Success!\nSDT Verified!" and SDTOutput != "":
        output = "Parsing Success!\nSDT error...\n\n" + SDTOutput

# Ejecutar el analizador
def AnalyzeCode(txt):
    Syntax.rebootVariables()
    parser.parse(txt)

    guardar_resultados("SymbolTable_Updates.txt", Syntax.Upd_ST)
    guardar_resultados("Reductions_List.txt", Syntax.Reduces)
    guardar_resultados("Advertisements.txt", Syntax.Adv)
    global output
    output = Syntax.Output
    SDTOutput = Syntax.Semantic_Errors
    if output == "Parsing Success!\nSDT Verified!" and SDTOutput != "":
        output = "Parsing Success!\nSDT error...\n\n" + SDTOutput
    #print(Syntax.Semantic_Errors)

