import tkinter as tk



def click_numero(numero):
    entrada_texto.insert(tk.END, numero)

def click_operador(operador):
    entrada_texto.insert(tk.END, operador)



def calcular():
    try:
        ecuacion = entrada_texto.get()
        resultado = eval(ecuacion)
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, str(resultado))
    except Exception as e:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Error")



ventana = tk.Tk()
ventana.title("             Calculadora")


entrada_texto = tk.Entry(ventana, width=50, highlightcolor='white')
entrada_texto.grid(row=0, column=0, columnspan=4)
ventana.configure(background='#4B4B4B')
texto = '\x1b[94mtexto a color\x1b[0m'

botones = [
  
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', 'Borrar', '=', '+'
]
ventana.configure(background='#4B4B4B')
texto = '\x1b[94mtexto a color\x1b[0m'
fila = 1
columna = 0


for boton in botones:

    tk.Button(ventana, text=boton, width=10, height=5, background="#4B4B4B", fg="white",  font=("Roboto Cn",12), command=lambda b=boton: click_numero(b) if b.isdigit() or b == "." else click_operador(b) if b in "+-*/" else calcular() if b == "=" else entrada_texto.delete(0, tk.END)).grid(row=fila, column=columna)
 
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
ventana.configure(background='#4B4B4B')

ventana.mainloop()