# validaciones.py
import re
from config import NOMBRE_MIN_LENGTH, PATRON_CORREO

def validar_nombre(mensaje="Ingrese su nombre: "):
    try:
        nombre = input(mensaje).strip()
        
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío.")
            return validar_nombre(mensaje)
        
        if len(nombre) < NOMBRE_MIN_LENGTH:
            print(f"❌ Error: El nombre debe tener al menos {NOMBRE_MIN_LENGTH} caracteres.")
            return validar_nombre(mensaje)
        
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            print("❌ Error: El nombre solo debe contener letras y espacios.")
            return validar_nombre(mensaje)
        
        return nombre
    except Exception as e:
        print(f"❌ Error: {e}")
        return validar_nombre(mensaje)

def validar_correo(mensaje="Ingrese su correo: "):
    try:
        correo = input(mensaje).strip().lower()
        
        if not correo:
            print("❌ Error: El correo no puede estar vacío.")
            return validar_correo(mensaje)
        
        if not re.match(PATRON_CORREO, correo):
            print("❌ Error: El correo no tiene un formato válido.")
            return validar_correo(mensaje)
        
        return correo
    except Exception as e:
        print(f"❌ Error: {e}")
        return validar_correo(mensaje)

def validar_opcion_numerica(mensaje, min_val, max_val):
    try:
        opcion = int(input(mensaje))
        
        if opcion < min_val or opcion > max_val:
            print(f"❌ Error: Ingrese un número entre {min_val} y {max_val}.")
            return validar_opcion_numerica(mensaje, min_val, max_val)
        
        return opcion
    except ValueError:
        print("❌ Error: Debe ingresar un número válido.")
        return validar_opcion_numerica(mensaje, min_val, max_val)