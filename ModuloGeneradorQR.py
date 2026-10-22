"""
Módulo qr_generator.py
Proporciona la lógica para generar y guardar imágenes de códigos QR
utilizando la librería de terceros 'qrcode'.
"""

import os
import qrcode
from PIL import Image


def generar_codigo_qr(
    texto: str,
    nombre_archivo: str,
    color_relleno: str = "black",
    color_fondo: str = "white"
) -> bool:
    """
    Genera un código QR a partir de un texto o URL y lo guarda en disco.

    Parámetros:
        texto (str): El contenido o enlace que se codificará en el QR.
        nombre_archivo (str): El nombre del archivo de salida (ej: 'mi_qr.png').
        color_relleno (str): Color de los cuadros del QR. Por defecto 'black'.
        color_fondo (str): Color de fondo del QR. Por defecto 'white'.

    Retorna:
        bool: True si el archivo se guardó correctamente, False si hubo error.
    """
    # Validación defensiva de parámetros
    if not texto or not texto.strip():
        print("Error: El texto o URL no puede estar vacío.")
        return False

    if not nombre_archivo or not nombre_archivo.strip():
        print("Error: El nombre del archivo de salida no puede estar vacío.")
        return False

    # Asegurar extensión .png si el usuario no la escribió
    if not nombre_archivo.lower().endswith(".png"):
        nombre_archivo += ".png"

    try:
        # Configuración del objeto QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto.strip())
        qr.make(fit=True)

        # Creación de la imagen
        imagen: Image.Image = qr.make_image(
            fill_color=color_relleno,
            back_color=color_fondo
        )

        # Guardado en disco
        imagen.save(nombre_archivo)
        
        # Obtener ruta absoluta para notificar al usuario
        ruta_absoluta = os.path.abspath(nombre_archivo)
        print(f"\n¡Éxito! El código QR ha sido guardado en:")
        print(f"-> {ruta_absoluta}")
        return True

    except Exception as error:
        print(f"Error al generar o guardar la imagen del QR: {error}")
        return False

