"""  
Módulo principal del sistema de inscripciones a charlas.  
Contiene el menú principal e interacción con el usuario.  
"""  

from gestion_charlas import GestorCharlas  
import os  

def mostrar_banner():  
    """Muestra un banner de bienvenida."""  
    print("\n" + "="*60)  
    print("🎓 SISTEMA DE INSCRIPCIONES A CHARLAS".center(60))  
    print("="*60 + "\n")  

def mostrar_menu():  
    """Muestra el menú principal."""  
    print("\n" + "="*60)  
    print("MENÚ PRINCIPAL".center(60))  
    print("="*60)  
    print("1. 📝 Inscribirse en una charla")  
    print("2. 📊 Consultar inscripciones")  
    print("3. 🔍 Ver inscritos por charla")  
    print("4. 🚪 Salir del sistema")  
    print("="*60)  

def limpiar_pantalla():  
    """Limpia la pantalla de la consola."""  
    os.system('cls' if os.name == 'nt' else 'clear')  

def opcion_inscritos_por_charla(gestor):  
    """Opción para ver inscritos en una charla específica."""  
    print("\n" + "="*60)  
    print("🔍 INSCRITOS POR CHARLA".center(60))  
    print("="*60 + "\n")  
    
    charlas = list(gestor.charlas.keys())  
    
    for indice, charla in enumerate(charlas, 1):  
        print(f"{indice}. {charla}")  
    
    print(f"{len(charlas) + 1}. Volver al menú principal")  
    
    while True:  
        try:  
            opcion = int(input("\nSeleccione una charla: "))  
            
            if 1 <= opcion <= len(charlas):  
                charla_seleccionada = charlas[opcion - 1]  
                inscritos = gestor.obtener_inscritos_por_charla(charla_seleccionada)  
                
                print("\n" + "="*80)  
                print(f"Inscritos en {charla_seleccionada}".center(80))  
                print("="*80)  
                
                if not inscritos:  
                    print("\n⚠ No hay inscritos en esta charla aún.\n")  
                else:  
                    print(f"\n{'No.':<5} {'Nombre':<25} {'Correo':<50}")  
                    print("-"*80)  
                    
                    for indice, inscrito in enumerate(inscritos, 1):  
                        nombre = inscrito['nombre'][:24]  
                        correo = inscrito['correo'][:49]  
                        print(f"{indice:<5} {nombre:<25} {correo:<50}")  
                    
                    print(f"\nTotal: {len(inscritos)} inscritos en {charla_seleccionada}\n")  
                
                input("Presione Enter para continuar...")  
                break  
            
            elif opcion == len(charlas) + 1:  
                break  
            
            else:  
                print(f"❌ Error: Ingrese un número entre 1 y {len(charlas) + 1}.")  
        
        except ValueError:  
            print("❌ Error: Debe ingresar un número válido.")  

def ejecutar_menu_principal(gestor):  
    """  
    Ejecuta el menú principal del sistema.  
    
    Args:  
        gestor (GestorCharlas): Instancia del gestor de charlas  
    """  
    while True:  
        mostrar_menu()  
        
        opcion = input("Seleccione una opción (1-4): ").strip()