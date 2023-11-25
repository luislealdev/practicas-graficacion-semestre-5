# PRÁCTICA 3: Transformación de Objetos Bidimensionales. Desarrolle una aplicación en la que se dibujen objetos bidimencionaes
# a los que se les puedan aplicar operaciones de traslación, rotación y escalamiento. Además utilice la representación matricial
# para realizar transformaciones que sean combinaciones de las anteriores, en una sola operación.
from tkinter import *
import math

angulo_inicial = 0

window = Tk()
window.title("Práctica 3")
window.config(padx=100, pady=50, bg="#f7f5dd", width=700, height=500)
canvas = Canvas(window, width=700, height=500,
                background="#f7f5dd", highlightthickness=0)
canvas.pack()

# Dimensiones del rectángulo
ancho_rect = 100
alto_rect = 100

# Coordenadas del centro del canvas
centro = (canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2)

# Coordenadas del rectángulo
x0 = centro[0] - ancho_rect / 2
y0 = centro[1] - alto_rect / 2
x1 = centro[0] + ancho_rect / 2
y1 = centro[1] + alto_rect / 2

# Dibujar el rectángulo inicial
rectangulo = canvas.create_rectangle(x0, y0, x1, y1, fill='red')


# Rote el objeto en torno al origen con incrementos de 10 grados, hasta completar una revolución completa.
def transformar():
    global x0, y0, x1, y1
    angulo = math.radians(10)  # Convertir 10 grados a radianes
    # Aplicar la fórmula de rotación a cada punto del rectángulo
    x0_rotado = (x0 - centro[0]) * math.cos(angulo) - \
        (y0 - centro[1]) * math.sin(angulo) + centro[0]
    y0_rotado = (x0 - centro[0]) * math.sin(angulo) + \
        (y0 - centro[1]) * math.cos(angulo) + centro[1]
    x1_rotado = (x1 - centro[0]) * math.cos(angulo) - \
        (y1 - centro[1]) * math.sin(angulo) + centro[0]
    y1_rotado = (x1 - centro[0]) * math.sin(angulo) + \
        (y1 - centro[1]) * math.cos(angulo) + centro[1]

    # Actualizar las coordenadas del rectángulo en el canvas
    canvas.coords(rectangulo, x0_rotado, y0_rotado, x1_rotado, y1_rotado)
    # Actualizar las variables globales
    x0, y0, x1, y1 = x0_rotado, y0_rotado, x1_rotado, y1_rotado


def rotar():
    pass


btn_transformar = Button(window, text="Transformar",
                         command=transformar)
btn_transformar.pack()

btn_rotar = Button(window, text="Rotar",
                   command=rotar)
btn_rotar.pack()
# Escale el objeto al doble o triple de su tamaño original y redúzcalo a la mitad y a la tercera parte del tamaño original.

# Rote el objeto en incrementos de 10 grados pero ahora en torno a un punto arbitrario

# Traslade el objeto de una posición a otra

# Refleje el objeto respecto a los ejes cartesianos


window.mainloop()
