"""
Módulo para la gestión de archivos de inscripciones.
Incluye funciones para leer, escribir y sincronizar datos.
"""

import os
from config import ARCHIVO_INSCRIPCIONES, SEPARADOR

def inicializar_archivo():
    """Crea el archivo si no existe."""
    if not os.path.exists(ARCHIVO_INSCRIPCIONES):
        try:
            with open(ARCHIVO_INSCRIPCIONES, 'w', encoding='utf-8') as archivo:
                pass  # Crea el archivo vacío
            print(f"✓ Archivo '{ARCHIVO_INSCRIPCIONES}' creado exitosamente.")
        except IOError as e:
            print(f"❌ Error al crear el archivo: {e}")

def guardar_inscripcion(nombre, correo, charla):
    """
    Guarda una nueva inscripción en el archivo.
    
    Args:
        nombre (str): Nombre del inscrito
        correo (str): Correo del inscrito
        charla (str): Nombre de la charla
    
    Returns:
        bool: True si se guardó exitosamente, False en caso contrario
    """
    try:
        with open(ARCHIVO_INSCRIPCIONES, 'a', encoding='utf-8') as archivo:
            linea = f"{nombre}{SEPARADOR}{correo}{SEPARADOR}{charla}\n"
            archivo.write(linea)
        return True
    except IOError as e:
        print(f"❌ Error al guardar la inscripción: {e}")
        return False

def cargar_inscripciones():
    """
    Carga todas las inscripciones del archivo.
    
    Returns:
        list: Lista de diccionarios con las inscripciones
    """
    inscripciones = []
    
    try:
        if not os.path.exists(ARCHIVO_INSCRIPCIONES):
            return inscripciones
        
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                linea = linea.strip()
                if not linea:  # Ignorar líneas vacías
                    continue
                
                partes = linea.split(SEPARADOR)
                
                if len(partes) != 3:
                    print(f"⚠ Advertencia: Línea {numero_linea} con formato incorrecto.")
                    continue
                
                nombre, correo, charla = partes
                inscripciones.append({
                    'nombre': nombre.strip(),
                    'correo': correo.strip(),
                    'charla': charla.strip()
                })
    
    except IOError as e:
        print(f"❌ Error al leer inscripciones: {e}")
    
    return inscripciones

def obtener_estadisticas():
    """
    Genera estadísticas sobre las inscripciones.
    
    Returns:
        dict: Diccionario con estadísticas por charla
    """
    inscripciones = cargar_inscripciones()
    estadisticas = {}
    
    for inscripcion in inscripciones:
        charla = inscripcion['charla']
        estadisticas[charla] = estadisticas.get(charla, 0) + 1
    
    return estadisticas

def exportar_inscripciones_por_charla(charla):
    """
    Obtiene todos los inscritos en una charla específica.
    
    Args:
        charla (str): Nombre de la charla
    
    Returns:
        list: Lista de inscritos en esa charla
    """
    inscripciones = cargar_inscripciones()
    return [ins for ins in inscripciones if ins['charla'].lower() == charla.lower()]