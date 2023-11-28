# PRACTICA 2: FUENTES DE TEXTO: Diseñar una nueva fuente de texto, construir un pequeño
# conjunto de caracteres usando la nueva fuente creada y usarla en una aplicación de prueba
import tkinter as tk
from PIL import Image, ImageFont, ImageDraw

# Función para cargar la fuente TTF
def cargar_fuente(ruta_fuente, tamaño):
    return ImageFont.truetype(ruta_fuente, tamaño)

# Función para crear una imagen con texto usando la fuente
def crear_imagen_con_texto(texto, fuente):
    imagen = Image.new("RGB", (500, 400), color="white")
    draw = ImageDraw.Draw(imagen)
    draw.text((10, 50), texto, font=fuente, fill="black")
    return imagen

# Función para actualizar la imagen en el Label
def actualizar_imagen():
    texto = entry_texto.get()
    try:
        imagen = crear_imagen_con_texto(texto, fuente)
        imagen.thumbnail((500, 400))
        imagen_tk = ImageTk.PhotoImage(imagen)
        label_imagen.configure(image=imagen_tk)
        label_imagen.image = imagen_tk  # Guardar una referencia para evitar que la imagen se elimine
    except Exception as e:
        print(f"No se pudo actualizar la imagen: {e}")

# Crear una ventana
root = tk.Tk()
root.title("Texto con tipografía personalizada")

# Ruta de la fuente TTF
ruta_fuente = "Carito-Regular.ttf"  # Reemplaza con la ruta de tu archivo TTF
tamaño_fuente = 24

# Cargar la fuente TTF
fuente = cargar_fuente(ruta_fuente, tamaño_fuente)

# Crear una imagen inicial con texto predefinido
texto_inicial = "¡Hola mundo!"
imagen_inicial = crear_imagen_con_texto(texto_inicial, fuente)
imagen_inicial.thumbnail((500, 400))

# Convertir la imagen PIL a formato Tkinter PhotoImage
from PIL import ImageTk
imagen_tk_inicial = ImageTk.PhotoImage(imagen_inicial)

# Mostrar la imagen inicial en un Label
label_imagen = tk.Label(root, image=imagen_tk_inicial)
label_imagen.pack(side=tk.LEFT, padx=20, pady=40)

# Entrada de texto para que el usuario ingrese texto
entry_texto = tk.Entry(root, width=30)
entry_texto.pack(side=tk.RIGHT, padx=20, pady=40)

# Botón para actualizar la imagen
btn_actualizar = tk.Button(root, text="Actualizar", command=actualizar_imagen)
btn_actualizar.pack(side=tk.RIGHT, padx=10)

# Ejecutar la aplicación
root.mainloop()
