# Diccionario para controlar los cupos iniciales
charlas_disponibles = {
    "Marketing": 10,
    "Finanzas": 5,
    "Liderazgo": 8,
    "Superación": 12,
    "Redes Sociales": 15
}

def validar_entrada_recursiva(mensaje):
    """Pide un dato y si está vacío, se llama a sí misma (recursividad)"""
    valor = input(mensaje).strip()
    if not valor:
        print("  ⚠ El campo no puede estar vacío. Intente de nuevo porfavor.")
        return validar_entrada_recursiva(mensaje)
    return valor

def mostrar_disponibilidad():
    """Muestra las charlas y sus cupos actuales"""
    print("\n--- 📋 Charlas y Cupos Disponibles📋  ---")
    lista = list(charlas_disponibles.keys())
    for i, nombre in enumerate(lista, 1):
        cupo = charlas_disponibles[nombre]
        print(f"{i}. {nombre} ({cupo} cupos📚)")
    return lista

def realizar_inscripcion(nombre, correo):
    """Lógica para validar cupos y descontar"""
    lista_nombres = mostrar_disponibilidad()
    try:
        opcion = int(input("\n😺Seleccione el número de la charla a la que desea inscribirse: "))
        if 1 <= opcion <= len(lista_nombres):
            charla_sel = lista_nombres[opcion - 1]
            
            # Validar disponibilidad de cupos
            if charlas_disponibles[charla_sel] > 0:
                charlas_disponibles[charla_sel] -= 1
                return charla_sel
            else:
                print(f"❌ No quedan cupos para {charla_sel}.")
                return None
        else:
            print("⚠ Opción inválida.")
            return None
    except ValueError:
        print("⚠ Error: Debe ingresar un número.")
        return None