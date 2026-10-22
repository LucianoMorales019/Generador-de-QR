"""Funciones para generar y guardar imágenes de códigos QR."""

import os

import qrcode
from PIL import Image


def generar_codigo_qr(
    texto: str,
    nombre_archivo: str,
    color_relleno: str = "black",
    color_fondo: str = "white",
) -> bool:
    """Genera un código QR a partir de un texto o URL y lo guarda en disco.

    Args:
        texto: El contenido o enlace que se codificará en el QR.
        nombre_archivo: El nombre o la ruta del archivo de salida.
        color_relleno: Color de los cuadros del QR.
        color_fondo: Color de fondo del QR.

    Returns:
        True si el archivo se guardó correctamente; False ante errores
        esperables de generación, colores o escritura.
    """
    if not texto or not texto.strip():
        print("Error: El texto o URL no puede estar vacío.")
        return False

    if not nombre_archivo or not nombre_archivo.strip():
        print("Error: El nombre del archivo de salida no puede estar vacío.")
        return False

    if not nombre_archivo.lower().endswith(".png"):
        nombre_archivo += ".png"

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto.strip())
        qr.make(fit=True)

        imagen: Image.Image = qr.make_image(
            fill_color=color_relleno,
            back_color=color_fondo,
        )

        imagen.save(nombre_archivo)

        ruta_absoluta = os.path.abspath(nombre_archivo)
        print("\n¡Éxito! El código QR ha sido guardado en:")
        print(f"-> {ruta_absoluta}")
        return True

    except (OSError, ValueError, qrcode.exceptions.DataOverflowError) as error:
        print(f"Error al generar o guardar la imagen del QR: {error}")
        return False
