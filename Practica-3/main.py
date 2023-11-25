# PRÁCTICA 3: Transformación de Objetos Bidimensionales. Desarrolle una aplicación en la que se dibujen objetos bidimencionaes
# a los que se les puedan aplicar operaciones de traslación, rotación y escalamiento. Además utilice la representación matricial
# para realizar transformaciones que sean combinaciones de las anteriores, en una sola operación.
from tkinter import *

window = Tk()
window.title("Práctica 3")
window.config(padx=100, pady=50, bg="#f7f5dd", width=700, height=500)
canvas = Canvas(window, width=700, height=500,
                background="#f7f5dd", highlightthickness=0)
canvas.pack()
a = canvas.create_rectangle(50, 0, 100, 50, fill='red')
# Rote el objeto en torno al origen con incrementos de 10 grados, hasta completar una revolución completa.

# Escale el objeto al doble o triple de su tamaño original y redúzcalo a la mitad y a la tercera parte del tamaño original.

# Rote el objeto en incrementos de 10 grados pero ahora en torno a un punto arbitrario

# Traslade el objeto de una posición a otra

# Refleje el objeto respecto a los ejes cartesianos

window.mainloop()
