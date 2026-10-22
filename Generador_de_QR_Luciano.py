"""Punto de entrada de la aplicación interactiva para generar códigos QR."""

from ModuloGeneradorQR import generar_codigo_qr


def solicitar_datos_usuario() -> tuple[str, str, str, str]:
    """Solicita el contenido, el nombre de archivo y los colores del QR.

    Returns:
        Una tupla con el texto, el nombre de archivo, el color del QR y el
        color de fondo.
    """
    print("=" * 50)
    print("      GENERADOR DE CÓDIGOS QR (UNIDAD 11)")
    print("=" * 50)

    texto = ""
    while not texto.strip():
        texto = input("Ingrese el texto o URL para el QR: ")
        if not texto.strip():
            print("El texto no puede estar vacío. Intente de nuevo.\n")

    nombre_archivo = ""
    while not nombre_archivo.strip():
        nombre_archivo = input(
            "Ingrese el nombre del archivo de salida (ej: mi_qr.png): "
        )
        if not nombre_archivo.strip():
            print(
                "El nombre de archivo no puede estar vacío. "
                "Intente de nuevo.\n"
            )

    print("\n--- Configuración de colores (Opcional) ---")
    color_relleno = input(
        "Color del QR (presione Enter para 'black'): "
    ).strip()
    if not color_relleno:
        color_relleno = "black"

    color_fondo = input(
        "Color de fondo (presione Enter para 'white'): "
    ).strip()
    if not color_fondo:
        color_fondo = "white"

    return texto, nombre_archivo, color_relleno, color_fondo


def main() -> None:
    """Función principal que coordina la ejecución del programa."""
    try:
        (
            texto,
            nombre_archivo,
            color_relleno,
            color_fondo,
        ) = solicitar_datos_usuario()

        exito = generar_codigo_qr(
            texto=texto,
            nombre_archivo=nombre_archivo,
            color_relleno=color_relleno,
            color_fondo=color_fondo,
        )

        if not exito:
            print("\nNo se pudo completar la generación del código QR.")

    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario. Salida limpia.")
    except EOFError:
        print("\nNo se recibieron más datos. Proceso finalizado.")


if __name__ == "__main__":
    main()