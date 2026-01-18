def guardar_inscripcion(nombre, correo, charla):
    """Escribe una nueva línea en el archivo de texto."""
    try:
        # El modo 'a' abre el archivo para añadir texto al final sin borrar lo anterior
        with open("inscripciones_charlas.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre} | {correo} | {charla}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def leer_inscripciones():
    """Lee todas las líneas del archivo y las devuelve como una lista."""
    try:
        with open("inscripciones_charlas.txt", "r", encoding="utf-8") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        # Si el archivo aún no existe (nadie se ha inscrito), devuelve una lista vacía
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []