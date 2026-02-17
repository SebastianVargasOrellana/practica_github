import tkinter as tk
from tkinter import messagebox
def dividir_dos():
    try:
        numero=float(entry_numero.get())
        resultado=numero/2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error, introduzca un número válido")
ventana=tk.Tk()
ventana.title("Dividir entre 2")
label_instruccion=tk.Label(ventana, text="Introduce un número:")
label_instruccion.pack(pady=5)
entry_numero = tk.Entry(ventana)
entry_numero.pack(pady=5)
boton_calcular = tk.Button(ventana, text="Dividir entre 2", command=dividir_dos)
boton_calcular.pack(pady=5)
label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack(pady=5)
ventana.mainloop()