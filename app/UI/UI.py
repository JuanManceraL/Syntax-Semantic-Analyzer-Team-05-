import sys
import os

# Obtener la ruta del directorio padre
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agregar el directorio padre al sys.path
sys.path.append(parent_dir)

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import time
from pathlib import Path
import Analyzer

UI_dir = Path(__file__).parent
app_dir = UI_dir.parent.parent
Examples_dir = app_dir / "Examples"

prevName = "a"
pad_x_buttons = 7
pad_y_buttons = 24

colour1 = "#020f12"
colour2 = "#05d7ff"
colour3 = "#65e7ff"
colour4 = "BLACK"

colour5 = "#05242B"
colour6 = "#26364B"


def NewArchive():
    prevName = "a"
    Box_code.delete("1.0", "end")

def AnalyzeCode():
    archivoTexto = Box_code.get(1.0, END)
    Analyzer.AnalyzeCode(archivoTexto)
    UpdateOutput()

def AnalyzeScript(ExampleNum = None):
    if ExampleNum == None:
        archivo = filedialog.askopenfilename()
    else:
        if ExampleNum == 0:
            archivo = Examples_dir / "ejemplo0.c"
        elif ExampleNum == 1:
            archivo = Examples_dir / "ejemplo1.c"
        elif ExampleNum == 2:
            archivo = Examples_dir / "ejemplo2.c"
        elif ExampleNum == 3:
            archivo = Examples_dir / "ejemplo3.c"
        elif ExampleNum == 4:
            archivo = Examples_dir / "ejemploE0.c"
        elif ExampleNum == 5:
            archivo = Examples_dir / "ejemploE1.c"
        elif ExampleNum == 6:
            archivo = Examples_dir / "ejemploE2.c"
        elif ExampleNum == 7:
            archivo = Examples_dir / "ejemploE3.c"
    if not archivo:
        return
    #Analyzer.AnalyzeArchive(archivo)
    #prevName = archivo
    Box_code.delete("1.0", "end")
    with open(archivo, 'r') as file:
        Box_code.insert("1.0", file.read())
    UpdateOutput()

def AnalizeExample(ExampleNum):
    archivo = ExampleNum
    if not archivo:
        return
    Analyzer.AnalizeArchive(archivo)
    prevName = archivo
    Box_code.delete("1.0", "end")
    with open(archivo, 'r') as file:
        Box_code.insert("1.0", file.read())
    UpdateOutput()

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

def ExitApp():
    value = messagebox.askokcancel("Salir", "Estás seguro que deseas salir?")
    if value:
        raiz.destroy()

def UpdateOutput():
    time.sleep(0.2)
    textOutput = Analyzer.output
    LabB7.config(text=textOutput)

def ShowCommands():
    messagebox.showinfo("Comandos disponibles", "print()  if(){}  if(){}else{} \ndeclaracion int a = 10;")

def ShowRequeriments():
    messagebox.showinfo("Requeriments", "Libraries: \ntkinter\ntime\npathlib\nmath\nply")

def ShowInfoTeam():
    messagebox.showinfo("Team Info", "Lexel / Syntatic / Semantic - Analyzer - Team 05") #\nJuan M\nDaniela M\nAngel R\n

def showReductions():
    textRed =  Analyzer.path_Reduction
    if textRed == "":
        return

    root = Tk()
    root.title("Reductions")
    root.resizable(True, True)
    root.geometry('300x600')

    FrameR = Frame(root)
    FrameR.grid(row=0,column=0)
    
    #RedLabel=Label(Frame1, text=textRed)
    #RedLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Red_text = ScrolledText(FrameR, width=70, height=30)
    with open(textRed, 'r') as file:
        Red_text.insert("1.0", file.read())



#raiz
raiz = Tk()
raiz.title("Lexel / Syntatic / Semantic - Analyzer - Team 05")
raiz.resizable(True, True)
raiz.iconbitmap(UI_dir / "Image_icon.ico")
raiz.geometry('800x400')
raiz.geometry("850x550")
raiz.config(bg=colour1)

Frame1 = Frame(raiz, background="#05242B")
Frame1.grid(row=0,column=0)

Frame2 = Frame(raiz)
Frame2.grid(row=0,column=1)
Frame2.config(bg=colour1, width=20, height=20, pady=40, padx=25)

CodeLabel=Label(Frame1, text="Code: ", background="#05242B", foreground='WHITE', font=('Arial', 10, 'bold'))
CodeLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")

Box_code = ScrolledText(Frame1, width=70, height=30)
Box_code.config(background=colour6, foreground='WHITE')
Box_code.grid(row=2, column=0, padx=10, pady=10)
Box_code.insert("1.0", "Escribe tu codigo aqui")

width_buttons = 18


botonAnalyzeCode = Button(Frame2, text="Analizar archivo", width=width_buttons, command=AnalyzeScript, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
botonAnalyzeCode.grid(row=0, column=0, padx=pad_y_buttons)

LabB1=Label(Frame2)
LabB1.config(background=colour1)
LabB1.grid(row=1, column=0, padx=2, pady=2)

botonAnalyze = Button(Frame2, text="Analizar Códigor", width=width_buttons, command=AnalyzeCode, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
botonAnalyze.grid(row=2, column=0, padx=pad_y_buttons)

LabB2=Label(Frame2)
LabB2.config(background=colour1)
LabB2.grid(row=3, column=0, padx=2, pady=2)

PasteButton=Button(Frame2, text="Pegar texto copiado", width=width_buttons, command=Paste, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
PasteButton.grid(row=4, column=0, padx=pad_y_buttons)

LabB3=Label(Frame2)
LabB3.config(background=colour1)
LabB3.grid(row=5, column=0, padx=2, pady=2)

LoadButton=Button(Frame2, text="Cargar Archivo", width=width_buttons, command=LoadCode, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
LoadButton.grid(row=6, column=0, padx=pad_y_buttons)

LabB4=Label(Frame2)
LabB4.config(background=colour1)
LabB4.grid(row=7, column=0, padx=2, pady=2)

SaveButton=Button(Frame2, command=SaveCode, text="Guardar", font=('Arial', 10, 'bold'), width=width_buttons, height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
SaveButton.grid(row=8, column=0, padx=pad_y_buttons)

LabB5=Label(Frame2)
LabB5.config(background=colour1)
LabB5.grid(row=9, column=0, padx=10, pady=2)

LabB6=Label(Frame2)
LabB6.config(background=colour1, text="Salida:", foreground=colour2, font=('Arial', 10, 'bold'))
LabB6.grid(row=10, column=0, padx=10, pady=2)

txt_Output=''
LabB7=Label(Frame2)
LabB7.config(background=colour1, text="", foreground=colour2, font=('Arial', 10, 'bold'))
LabB7.grid(row=11, column=0, padx=10, pady=2)

    #Menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo", command=NewArchive)
archivoMenu.add_command(label="Guardar", command=SaveCode)
archivoMenu.add_command(label="Guardar como", command=SaveCodeAs)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ExitApp)

ejemplosMenu = Menu(barraMenu, tearoff=0)
ejemplosMenu.add_command(label="Ejemplo 0", command=lambda: AnalyzeScript(0))
ejemplosMenu.add_command(label="Ejemplo 1", command=lambda: AnalyzeScript(1))
ejemplosMenu.add_command(label="Ejemplo 2", command=lambda: AnalyzeScript(2))
ejemplosMenu.add_command(label="Ejemplo 3", command=lambda: AnalyzeScript(3))
ejemplosMenu.add_separator()
ejemplosMenu.add_command(label="Ejemplo error 0", command=lambda: AnalyzeScript(4))
ejemplosMenu.add_command(label="Ejemplo error 1", command=lambda: AnalyzeScript(5))
ejemplosMenu.add_command(label="Ejemplo error 2", command=lambda: AnalyzeScript(6))
ejemplosMenu.add_command(label="Ejemplo error 3", command=lambda: AnalyzeScript(7))

herramientasMenu = Menu(barraMenu, tearoff=0)
herramientasMenu.add_command(label="Cortar", command=Cut)
herramientasMenu.add_command(label="Copiar", command=Copy)
herramientasMenu.add_command(label="Pegar", command=Paste)

ayudaMenu = Menu(barraMenu,  tearoff=0)
ayudaMenu.add_command(label="Comandos disponibles", command=ShowCommands)
ayudaMenu.add_command(label="Requerimientos", command=ShowRequeriments)
ayudaMenu.add_command(label="Información fabricante", command=ShowInfoTeam)

#ReductionMenu = Menu(barraMenu, tearoff=0)
#ReductionMenu.add_command(label="Last Reduction", command=showReductions)

barraMenu.add_cascade(label="Archivo", menu = archivoMenu)
barraMenu.add_cascade(label="Ejemplos", menu = ejemplosMenu)
barraMenu.add_cascade(label="Herramientas", menu = herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu = ayudaMenu)
#barraMenu.add_cascade(label="Last Reduction", menu = ReductionMenu)
raiz.mainloop()
