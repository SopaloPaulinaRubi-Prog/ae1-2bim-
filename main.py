import gestion_charlas as gc
import manejo_archivos as ma

def main():
    while True:
        print("\n" + "⏕"*39)
        print("  🧑‍💻 SISTEMA DE INSCRIPCIONES 👩‍💻")
        print("⏕"*39)
        print("1. 📝  Inscribirse en una charla")
        print("2. 📊  Consultar inscripciones")
        print("3. 🚪  Salir")
        
        opcion = input("\nSeleccione una opción🍃: ")

        if opcion == "1":
            # Uso de recursividad para validar datos vacíos
            nombre = gc.validar_entrada_recursiva("🍀Ingrese su nombre: ")
            correo = gc.validar_entrada_recursiva("🍀Ingrese su correo: ")
            
            # Proceso de inscripción
            charla_confirmada = gc.realizar_inscripcion(nombre, correo)
            
            if charla_confirmada:
                ma.guardar_inscripcion(nombre, correo, charla_confirmada)
                print(f"\n✅ ¡Éxito! Inscrito en: {charla_confirmada}")
            else:
                print("\n❌ No se pudo completar la inscripción.")

        if opcion == "2":
            datos = ma.leer_inscripciones()
            if not datos:
                print("\nNo hay registros guardados.")
            else:
                print("\n" + f"{'⁜No.':<5} {'⁜Nombre':<20} {'⁜Correo':<25} {'⁜Charla':<20}")
                print("=" * 70)
                for i, linea in enumerate(datos, 1):
                    # Limpiamos y formateamos la línea del archivo
                    p = linea.strip().split(" | ")
                    if len(p) == 3:
                        print(f"{i:<5} {p[0][0:18]:<20} {p[1][0:23]:<25} {p[2]:<20}")

        if opcion == "3":
            print("👋 Saliendo del sistema. ¡Tenga un excelente día!😉")
            break
        else:
            print("⚠ Opción no válida, intente de nuevo.")

# Bloque de diagnóstico solicitado
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO: {e}")
        import traceback
        traceback.print_exc()
    finally:
        input("\n🏷️Presione Enter para cerrar esta ventana...")
        