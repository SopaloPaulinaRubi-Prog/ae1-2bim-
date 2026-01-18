"""
Módulo de configuración del sistema de inscripciones.
Contiene los datos de las charlas y constantes globales.
"""

# Diccionario con las charlas y sus cupos iniciales
CHARLAS = {
    "Marketing": 5,
    "Finanzas": 3,
    "Liderazgo": 10,
    "Superación": 2,
    "Redes Sociales": 8
}

# Ruta del archivo de inscripciones
ARCHIVO_INSCRIPCIONES = "inscripciones_charlas.txt"

# Separador de campos en el archivo
SEPARADOR = "|"

# Longitud mínima de nombre
NOMBRE_MIN_LENGTH = 2

# Patrones de validación
PATRON_CORREO = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'