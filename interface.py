import tkinter as tk
import lex_analyzer as lex
import syntax_analyzer as syn
import os
from tkinter import filedialog



def syntax_analyzer():
    textContent = TextField.get("1.0", tk.END)
    errores = syn.analizeSyntax(textContent)

    if len(errores) > 0:
        mensaje = "\n".join(errores)
    else:
        mensaje = "Análisis sintáctico exitoso"

    botRightTextField.delete("1.0", tk.END)
    botRightTextField.insert(tk.END, mensaje)

def lex_analyzer():
    textContent = TextField.get("1.0", tk.END)
    resultErrors, resultLex = lex.analizeLex(textContent)

    topRightTextField.delete("1.0", tk.END)
    if len(resultErrors)==0:
        linea = "\n".join(resultErrors)
        topRightTextField.insert(tk.END, linea + "\n")
    else:
        linea = "Análisis léxico exitoso"
        topRightTextField.insert(tk.END, linea + "\n")
    # for token in resultLex:
    #     linea = str(token.lineno) + ": " + str(token.value) + " - " + str(token.type)
    #     print(linea)
    #     topRightTextField.insert(tk.END, linea + "\n")


def cargar_contenido():

    global fileContent

    file = filedialog.askopenfilename(initialdir=os.path.dirname(__file__), title="Seleccionar archivo",
                                         filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if file:
        with open(file, "r") as f:
            fileContent = f.read()

        # syn.resetear_linea()  # Reinicia el conteo de línea
        TextField.delete("1.0", tk.END)
        TextField.insert(tk.END, fileContent)
        # print(fileContent)

def analizeCode():
    lex_analyzer()
    syntax_analyzer()

def limpiar_contenido():
    TextField.delete("1.0", tk.END)
    topRightTextField.delete("1.0", tk.END)
    botRightTextField.delete("1.0", tk.END)

#ventana principal
ventana = tk.Tk()
ventana.geometry("1080x720")
ventana.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
ventana.grid_rowconfigure(0, weight=1)

ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()

leftContainer = tk.Frame(ventana)
leftContainer.grid(row=0, column=0, columnspan=2, sticky="nsew")

ancho_espacio = ancho_ventana // 2
alto_espacio = alto_ventana

textContainer = tk.Frame(leftContainer, padx=20, pady=20)
textContainer.pack(fill="both", expand=True)

TextField = tk.Text(textContainer, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
TextField.pack(fill="both", expand=True)

rigthContainer = tk.Frame(ventana, bg="blue")
rigthContainer.grid(row=0, column=2, columnspan=3, sticky="nsew")

topRigthContainer = tk.Frame(rigthContainer)
topRigthContainer.pack(side="top", fill="both", expand=True)

botRigthContainer = tk.Frame(rigthContainer)
botRigthContainer.pack(side="bottom", fill="both", expand=True)

topRigthTextContainer = tk.Frame(topRigthContainer, padx=20, pady=20)
topRigthTextContainer.pack(fill="both", expand=True)

botRigthTextContainer = tk.Frame(botRigthContainer, padx=20, pady=20)
botRigthTextContainer.pack(fill="both", expand=True)

topRightTextField = tk.Text(topRigthTextContainer, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
topRightTextField.pack(fill="both", expand=True)

botRightTextField = tk.Text(botRigthTextContainer, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
botRightTextField.pack(fill="both", expand=True)

button = tk.Button(topRigthContainer, text="Run", command=analizeCode)
button.pack(side="bottom")

ventana.mainloop()