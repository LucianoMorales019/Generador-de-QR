"""Funciones para generar y guardar imágenes de códigos QR."""

import os
from pathlib import Path

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

    ruta_archivo = Path(nombre_archivo.strip())
    if ruta_archivo.name in ("", ".", ".."):
        print("Error: La ruta debe incluir un nombre de archivo válido.")
        return False

    if ruta_archivo.suffix and ruta_archivo.suffix.lower() != ".png":
        print("Error: El formato de salida debe ser PNG (.png).")
        return False

    if not ruta_archivo.suffix:
        ruta_archivo = ruta_archivo.with_suffix(".png")

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto.strip())
        qr.make(fit=True)
    except qrcode.exceptions.DataOverflowError as error:
        print(f"Error: El texto excede la capacidad del código QR: {error}")
        return False
    except ValueError as error:
        print(
            "Error: El texto es demasiado extenso para generar un QR: "
            f"{error}"
        )
        return False

    try:
        imagen: Image.Image = qr.make_image(
            fill_color=color_relleno,
            back_color=color_fondo,
        ).get_image()
    except (TypeError, ValueError) as error:
        print(f"Error: El color indicado no es válido: {error}")
        return False

    try:
        imagen.save(ruta_archivo)
    except OSError as error:
        print(f"Error al guardar el código QR: {error}")
        return False

    ruta_absoluta = os.path.abspath(ruta_archivo)
    print("\n¡Éxito! El código QR ha sido guardado en:")
    print(f"-> {ruta_absoluta}")
    return True
