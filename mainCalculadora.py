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
    except ZeroDivisionError:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Error: División por cero")
    except Exception as e:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Error")

def calcular_porcentaje():
    try:
        ecuacion = entrada_texto.get()
        resultado = eval(ecuacion) / 100.0
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Error: División por cero")
    except Exception as e:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Error")

ventana = tk.Tk()
ventana.title("Calculadora")

entrada_texto = tk.Entry(ventana, width=20, font=("Arial", 20))
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)
ventana.configure(background='#4B4B4B')

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '=', '+', '%',
    'Borrar'
]

fila = 1
columna = 0

for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, width=10, height=3, bg="#009688", fg="white", font=("Arial", 20),
                  command=calcular_porcentaje if entrada_texto.get().endswith('%') else calcular).grid(row=fila, column=columna, padx=5, pady=5)
    elif boton == 'C':
        tk.Button(ventana, text=boton, width=10, height=3, bg="#E57373", fg="white", font=("Arial", 20),
                  command=lambda b=boton: entrada_texto.delete(0, tk.END)).grid(row=fila, column=columna, padx=5, pady=5)
    else:
        tk.Button(ventana, text=boton, width=10, height=3, bg="#E0E0E0", fg="black", font=("Arial", 20),
                  command=lambda b=boton: click_numero(b) if b.isdigit() or b == "." else click_operador(b) if b in "+-*/%" else entrada_texto.delete(0, tk.END)).grid(row=fila, column=columna, padx=5, pady=5)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

ventana.mainloop()