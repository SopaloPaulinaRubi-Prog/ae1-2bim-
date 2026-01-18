"""
Módulo de validaciones para entrada de datos.
Implementa recursividad para re-solicitar datos inválidos.
"""

import re
from config import NOMBRE_MIN_LENGTH, PATRON_CORREO

def validar_nombre(mensaje="Ingrese su nombre: ", intentos=1):
    """
    Valida que el nombre no esté vacío y tenga longitud mínima.
    Usa recursividad si el input es inválido.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        intentos (int): Número de intento actual (para recursividad)
    
    Returns:
        str: Nombre validado
    """
    try:
        nombre = input(mensaje).strip()
        
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío.")
            return validar_nombre(mensaje, intentos + 1)
        
        if len(nombre) < NOMBRE_MIN_LENGTH:
            print(f"❌ Error: El nombre debe tener al menos {NOMBRE_MIN_LENGTH} caracteres.")
            return validar_nombre(mensaje, intentos + 1)
        
        # Validar que solo contenga letras y espacios
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            print("❌ Error: El nombre solo debe contener letras y espacios.")
            return validar_nombre(mensaje, intentos + 1)
        
        return nombre
    
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return validar_nombre(mensaje, intentos + 1)

def validar_correo(mensaje="Ingrese su correo: ", intentos=1):
    """
    Valida que el correo tenga un formato válido.
    Usa recursividad si el input es inválido.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        intentos (int): Número de intento actual
    
    Returns:
        str: Correo validado
    """
    try:
        correo = input(mensaje).strip().lower()
        
        if not correo:
            print("❌ Error: El correo no puede estar vacío.")
            return validar_correo(mensaje, intentos + 1)
        
        if not re.match(PATRON_CORREO, correo):
            print("❌ Error: El correo no tiene un formato válido.")
            return validar_correo(mensaje, intentos + 1)
        
        return correo
    
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return validar_correo(mensaje, intentos + 1)

def validar_opcion_numerica(mensaje, min_val, max_val, intentos=1):
    """
    Valida que la opción ingresada sea un número dentro del rango.
    
    Args:
        mensaje (str): Mensaje a mostrar
        min_val (int): Valor mínimo permitido
        max_val (int): Valor máximo permitido
        intentos (int): Número de intento
    
    Returns:
        int: Opción validada
    """
    try:
        opcion = int(input(mensaje))
        
        if not (min_val <= opcion <= max_val):
            print(f"❌ Error: Ingrese un número entre {min_val} y {max_val}.")
            return validar_opcion_numerica(mensaje, min_val, max_val, intentos + 1)
        
        return opcion
    
    except ValueError:
        print("❌ Error: Debe ingresar un número válido.")
        return validar_opcion_numerica(mensaje, min_val, max_val, intentos + 1)
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return validar_opcion_numerica(mensaje, min_val, max_val, intentos + 1)