"""
Módulo de gestión de charlas e inscripciones.
Controla disponibilidad de cupos y valida inscripciones.
"""

from config import CHARLAS, SEPARADOR
import manejo_archivos as ma
import validaciones as val

class GestorCharlas:
    """Clase para gestionar charlas e inscripciones."""
    
    def __init__(self):
        """Inicializa el gestor cargando datos previos."""
        ma.inicializar_archivo()
        self.charlas = CHARLAS.copy()
        self.inscripciones = ma.cargar_inscripciones()
        self._actualizar_cupos_disponibles()
    
    def _actualizar_cupos_disponibles(self):
        """Actualiza los cupos disponibles basándose en inscripciones previas."""
        for inscripcion in self.inscripciones:
            charla = inscripcion['charla']
            if charla in self.charlas:
                self.charlas[charla] -= 1
    
    def mostrar_charlas_disponibles(self):
        """Muestra el listado de charlas con cupos disponibles."""
        print("\n" + "="*60)
        print("📋 CHARLAS DISPONIBLES".center(60))
        print("="*60)
        
        lista_charlas = list(self.charlas.keys())
        
        for indice, charla in enumerate(lista_charlas, 1):
            cupos = self.charlas[charla]
            
            if cupos > 0:
                estado = f"✓ {cupos} cupo(s)"
                color = "🟢"
            else:
                estado = "AGOTADO"
                color = "🔴"
            
            print(f"{indice:2}. {color} {charla:<25} {estado:>15}")
        
        print("="*60)
        return lista_charlas
    
    def inscribir_usuario(self):
        """
        Proceso completo de inscripción de un usuario.
        
        Returns:
            bool: True si la inscripción fue exitosa, False en caso contrario
        """
        print("\n" + "="*60)
        print("📝 FORMULARIO DE INSCRIPCIÓN".center(60))
        print("="*60 + "\n")
        
        # Validar entrada de datos
        nombre = val.validar_nombre("Ingrese su nombre completo: ")
        correo = val.validar_correo("Ingrese su correo electrónico: ")
        
        # Mostrar charlas disponibles
        charlas_lista = self.mostrar_charlas_disponibles()
        
        # Seleccionar charla
        opcion = val.validar_opcion_numerica(
            f"Seleccione el número de la charla (1-{len(charlas_lista)}): ",
            1,
            len(charlas_lista)
        )
        
        charla_seleccionada = charlas_lista[opcion - 1]
        
        # Validar disponibilidad de cupos
        if self.charlas[charla_seleccionada] <= 0:
            print(f"\n❌ Lo sentimos, no hay cupos disponibles para '{charla_seleccionada}'.")
            return False
        
        # Confirmar inscripción
        print(f"\n📌 Resumen de inscripción:")
        print(f"   Nombre: {nombre}")
        print(f"   Correo: {correo}")
        print(f"   Charla: {charla_seleccionada}")
        
        confirmacion = input("\n¿Desea confirmar su inscripción? (S/N): ").strip().upper()
        
        if confirmacion != 'S':
            print("❌ Inscripción cancelada.")
            return False
        
        # Guardar inscripción
        if ma.guardar_inscripcion(nombre, correo, charla_seleccionada):
            self.charlas[charla_seleccionada] -= 1
            self.inscripciones.append({
                'nombre': nombre,
                'correo': correo,
                'charla': charla_seleccionada
            })
            print(f"\n✅ ¡Inscripción exitosa en '{charla_seleccionada}'!")
            return True
        else:
            print("\n❌ Error al guardar la inscripción. Intente nuevamente.")
            return False
    
    def consultar_inscripciones(self):
        """Muestra todas las inscripciones registradas."""
        print("\n" + "="*80)
        print("📊 LISTADO DE INSCRITOS".center(80))
        print("="*80)
        
        if not self.inscripciones:
            print("\n⚠ No hay inscripciones registradas aún.\n")
            return
        
        print(f"\n{'No.':<5} {'Nombre':<25} {'Correo':<35} {'Charla':<15}")
        print("-"*80)
        
        for indice, inscripcion in enumerate(self.inscripciones, 1):
            nombre = inscripcion['nombre'][:24]
            correo = inscripcion['correo'][:34]
            charla = inscripcion['charla'][:14]
            print(f"{indice:<5} {nombre:<25} {correo:<35} {charla:<15}")
        
        print("-"*80)
        print(f"Total de inscritos: {len(self.inscripciones)}\n")
        
        # Mostrar estadísticas
        self._mostrar_estadisticas()
    
    def _mostrar_estadisticas(self):
        """Muestra estadísticas de inscripciones por charla."""
        print("\n" + "="*80)
        print("📈 ESTADÍSTICAS POR CHARLA".center(80))
        print("="*80)
        
        estadisticas = ma.obtener_estadisticas()
        
        print(f"\n{'Charla':<25} {'Inscritos':<15} {'Cupos Restantes':<20}")
        print("-"*80)
        
        for charla in self.charlas:
            inscritos = estadisticas.get(charla, 0)
            cupos_restantes = self.charlas[charla]
            total_inicial = inscritos + cupos_restantes
            
            print(f"{charla:<25} {inscritos:<15} {cupos_restantes:<20}")
        
        print("-"*80 + "\n")
    
    def obtener_inscritos_por_charla(self, charla):
        """
        Obtiene los inscritos en una charla específica.
        
        Args:
            charla (str): Nombre de la charla
        
        Returns:
            list: Lista de inscritos
        """
        return [ins for ins in self.inscripciones 
                if ins['charla'].lower() == charla.lower()]