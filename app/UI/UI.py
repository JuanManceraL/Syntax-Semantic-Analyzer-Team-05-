import sys
import os

# Obtener la ruta del directorio padre
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agregar el directorio padre al sys.path
sys.path.append(parent_dir)

from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
#from ...app import main
#from app.Analyzer import AnalizeArchive
#from .. import Analyzer
import Analyzer

UI_dir = Path(__file__).parent
app_dir = UI_dir.parent.parent
Examples_dir = app_dir / "Examples"

prevName = "a"

def AnalizeCode():
    archivoTexto = Box_code.get(1.0, END)
    Analyzer.AnalizeCode(archivoTexto)

def NewArchive():
    prevName = "a"
    Box_code.delete("1.0", "end")

def AnalizeScript(ExampleNum = None):
    if ExampleNum == None:
        archivo = filedialog.askopenfilename()
    else:
        if ExampleNum == 1:
            archivo = Examples_dir / "ejemplo1.c"
        elif ExampleNum == 2:
            archivo = filedialog.askopenfilename()
        else:
            archivo = filedialog.askopenfilename()
    if not archivo:
        return
    Analyzer.AnalizeArchive(archivo)
    prevName = archivo
    Box_code.delete("1.0", "end")
    with open(archivo, 'r') as file:
        Box_code.insert("1.0", file.read())

def AnalizeExample(ExampleNum):
    archivo = ExampleNum
    if not archivo:
        return
    Analyzer.AnalizeArchive(archivo)
    prevName = archivo
    Box_code.delete("1.0", "end")
    with open(archivo, 'r') as file:
        Box_code.insert("1.0", file.read())


def LoadCode():
    global prevName
    archivo = filedialog.askopenfilename()
    if not archivo:
        return
    prevName = archivo
    Box_code.delete("1.0", "end")
    with open(archivo, 'r') as file:
        Box_code.insert("1.0", file.read())

def SaveCodeAs():
    global prevName
    archivo = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[ ('Archivo de texto','.txt'), ('Archivo C','.c'), ('Todos los archivos','.*') ])
    if archivo is None:
        return
    prevName = archivo.name
    archivoTexto = Box_code.get(1.0, END)
    archivo.write(archivoTexto)
    archivo.close()

def SaveCode():
    if len(prevName) <= 1:
       SaveCodeAs()
       return
    with open(prevName, "w") as file:
        archivoTexto = Box_code.get(1.0, END)
        file.write(archivoTexto)

def Copy():
    Box_code.event_generate("<<Copy>>")

def Cut():
    Box_code.event_generate("<<Cut>>")  

def Paste():
    Box_code.event_generate("<<Paste>>")  

#code_show=StringVar()
def generarUI():
    raiz = Tk()
    raiz.title("Lexel / Sintactic / Semantic - Analyzer - Team 05")
    raiz.resizable(True, True)
    raiz.iconbitmap(UI_dir / "Image_icon.ico")
    #raiz.geometry("650x350")
    raiz.config(bg="grey")

    Frame1 = Frame(raiz, width=800, height=400)
    Frame1.pack(side="left")

    CodeLabel=Label(Frame1, text="Code: ")
    CodeLabel.grid(row=0, column=0, padx=10, pady=0, sticky="w")

    #Box_code = Text(Frame1, width=100, height=40)
    global Box_code 
    Box_code = ScrolledText(Frame1, width=100, height=40)
    Box_code.grid(row=1, column=0, padx=10, pady=10)
    Box_code.insert("1.0", "Escribe tu codigo aqui")

    CodeLabel=Label(Frame1)
    CodeLabel.grid(row=2, column=0, padx=30)

    #Botones
    botonAnalyzeCode = Button(raiz, text="Analizar archivo", width=15, command=AnalizeScript)
    botonAnalyzeCode.pack(padx=1, pady=1)

    botonAnalyze = Button(raiz, text="Analiza Códigor", width=15, command=AnalizeCode)
    botonAnalyze.pack(padx=1, pady=1)

    PasteButton=Button(raiz, text="Pegar texto copiado", width=15, command=Paste)
    PasteButton.pack(padx=1, pady=1)

    LoadButton=Button(raiz, text="Cargar Archivo", width=15, command=LoadCode)
    LoadButton.pack(padx=1, pady=1)

    SaveButton=Button(raiz, text="Save", width=15, command=SaveCode)
    SaveButton.pack(padx=1, pady=1)

    #Menu
    barraMenu = Menu(raiz)
    raiz.config(menu=barraMenu)

    archivoMenu = Menu(barraMenu, tearoff=0)
    archivoMenu.add_command(label="Nuevo", command=NewArchive)
    archivoMenu.add_command(label="Guardar", command=SaveCode)
    archivoMenu.add_command(label="Guardar como", command=SaveCodeAs)
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Cerrar")
    archivoMenu.add_command(label="Salir")

    ejemplosMenu = Menu(barraMenu, tearoff=0)
    ejemplosMenu.add_command(label="Ejemplo 1", command=lambda: AnalizeScript(1))
    ejemplosMenu.add_command(label="Ejemplo 2", command=lambda: AnalizeScript(2))
    ejemplosMenu.add_command(label="Ejemplo 3", command=lambda: AnalizeScript(3))

    herramientasMenu = Menu(barraMenu, tearoff=0)
    herramientasMenu.add_command(label="Cortar", command=Cut)
    herramientasMenu.add_command(label="Copiar", command=Copy)
    herramientasMenu.add_command(label="Pegar", command=Paste)

    ayudaMenu = Menu(barraMenu,  tearoff=0)
    ayudaMenu.add_command(label="Comandos disponibles")

    barraMenu.add_cascade(label="Archivo", menu = archivoMenu)
    barraMenu.add_cascade(label="Ejemplos", menu = ejemplosMenu)
    barraMenu.add_cascade(label="Herramientas", menu = herramientasMenu)
    barraMenu.add_cascade(label="Ayuda", menu = ayudaMenu)
    raiz.mainloop()

#generarUI()