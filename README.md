# Generador de Códigos QR

Aplicación interactiva de consola escrita en Python para generar imágenes de
códigos QR a partir de texto o enlaces. Permite elegir el color del código y
el color de fondo.

## Integrantes

- Luciano Morales / LucianoMorales019
- Lucas Ariel Holës
- Kevin Alejandro Medina
-Gabriel Alfredo Regali

## Requisitos

- Python 3.9 o superior.
- `pip`, incluido normalmente con Python.

## Instalación

Cloná el repositorio y entrá en la carpeta del proyecto:

```bash
git clone https://github.com/LucianoMorales019/Generador-de-QR.git
cd Generador-de-QR
```

Creá y activá un entorno virtual. En Windows, desde PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En Windows, desde Símbolo del sistema (CMD):

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalá las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Uso

Con el entorno virtual activado, ejecutá:

```bash
python Generador_de_QR_Luciano.py
```

Ingresá el texto o enlace, el nombre del archivo de salida y, si querés,
los colores. Si omitís la extensión, el programa agrega `.png`; se admite
únicamente ese formato. Al terminar, mostrará la ruta absoluta donde guardó
la imagen.

## Estructura del proyecto

```text
Generador-de-QR/
├── .gitignore
├── Generador_de_QR_Luciano.py
├── modulo_generador_qr.py
├── requirements.txt
└── README.md
```

El entorno virtual (`.venv/`) y los archivos generados no se incluyen en el
repositorio.
