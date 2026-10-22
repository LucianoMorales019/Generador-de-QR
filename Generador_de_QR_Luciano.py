# 📚 Ejercicio Avanzado 2: "Generador de Códigos QR"
#
# 🎯 Objetivo:
# Construir un pequeño proyecto que genere imágenes de códigos QR a partir de
# un texto o enlace, aplicando entorno virtual, librerías de terceros, manejo
# de errores y buenas prácticas de código.
#
# 📄 Enunciado:
# Desarrollá un programa de consola que:
#   1. Le pida al usuario un texto o una URL.
#   2. Le pida el nombre del archivo de salida (ej: "mi_qr.png").
#   3. Genere el código QR correspondiente.
#   4. Guarde la imagen en disco y avise al usuario la ruta donde quedó.
#   5. (Opcional) Permita elegir el color del QR.
#
# 🧩 Librerías de terceros a usar (mínimo 2, instalar con pip):
#   - qrcode       → para generar el código QR.
#   - pillow (PIL) → para manejar y guardar la imagen resultante.
#
# 🛠️ Pasos obligatorios del proyecto:
#   1. Crear una carpeta para el proyecto (ej: "generador_qr/").
#   2. Crear el entorno virtual:        python -m venv .venv
#   3. Activarlo:
#         Linux/Mac:   source .venv/bin/activate
#         Windows:     .venv\Scripts\activate
#   4. Instalar las librerías:          pip install qrcode pillow
#   5. Congelar las dependencias:       pip freeze > requirements.txt
#   6. Escribir un README.md que explique qué hace el proyecto, cómo crear
#      el entorno virtual, cómo instalar las dependencias y cómo ejecutarlo.
#
# ✅ Requerimientos técnicos:
#   - Manejar TODOS los errores posibles con try / except
#     (texto vacío, nombre de archivo inválido, error al guardar la imagen,
#     etc.).
#   - Cada función debe tener su docstring explicando qué hace.
#   - Usar anotación de tipos en parámetros y valores de retorno.
#   - Respetar PEP8 (nombres, espacios, longitud de línea, sangría).
#   - Entregar la carpeta del proyecto con: el .py, requirements.txt y
#     README.md.


"""
Módulo main.py
Punto de entrada principal para la aplicación interactiva de generación de QR.
"""

from ModuloGeneradorQR import generar_codigo_qr


def solicitar_datos_usuario() -> tuple[str, str, str, str]:
    """
    Solicita e ingresa los datos por consola validando entradas vacías.

    Retorna:
        tuple[str, str, str, str]: Contiene (texto, nombre_archivo, color_relleno, color_fondo)
    """
    print("=" * 50)
    print("      GENERADOR DE CÓDIGOS QR (UNIDAD 11)")
    print("=" * 50)

    # Validación de texto
    texto = ""
    while not texto.strip():
        texto = input("Ingrese el texto o URL para el QR: ")
        if not texto.strip():
            print("El texto no puede estar vacío. Intente de nuevo.\n")

    # Validación de nombre de archivo
    nombre_archivo = ""
    while not nombre_archivo.strip():
        nombre_archivo = input("Ingrese el nombre del archivo salida (ej: mi_qr.png): ")
        if not nombre_archivo.strip():
            print("El nombre de archivo no puede estar vacío. Intente de nuevo.\n")

    # Opción de colores (opcional)
    print("\n--- Configuración de colores (Opcional) ---")
    color_relleno = input("Color del QR (presione Enter para 'black'): ").strip()
    if not color_relleno:
        color_relleno = "black"

    color_fondo = input("Color de fondo (presione Enter para 'white'): ").strip()
    if not color_fondo:
        color_fondo = "white"

    return texto, nombre_archivo, color_relleno, color_fondo


def main() -> None:
    """Función principal que coordina la ejecución del programa."""
    try:
        texto, nombre_archivo, color_relleno, color_fondo = solicitar_datos_usuario()
        
        exito = generar_codigo_qr(
            texto=texto,
            nombre_archivo=nombre_archivo,
            color_relleno=color_relleno,
            color_fondo=color_fondo
        )

        if not exito:
            print("\nNo se pudo completar la generación del código QR.")

    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario. Salida limpia.")
    except Exception as error:
        print(f"\nOcurrió un error inesperado durante la ejecución: {error}")


if __name__ == "__main__":
    main()