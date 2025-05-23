import json

class Tarea:
    def __init__(self, descripcion, fecha, completada='NO'):
        self.descripcion = descripcion
        self.fecha = fecha
        self.completada = completada
        
    def completar_tarea(self):
        self.completada = 'SI'
        
    def mostrar_info_tarea(self):
        print(f"Tarea: {self.descripcion}\nFecha: {self.fecha}\nCompletada: {self.completada}\n")
        
    def __str__(self):
        return f"Tarea: {self.descripcion}\nFecha: {self.fecha}\nCompletada: {self.completada}\n"
    
    def to_dict(self):
        return {
            'descripcion': self.descripcion,
            'fecha': self.fecha,
            'completada': self.completada
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['descripcion'], data['fecha'], data['completada'])

class AdministradorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        for t in self.tareas:
            if t.descripcion == tarea.descripcion:
                print(f"La tarea: '{tarea.descripcion}' ya fue asignada.\n")
                return
        self.tareas.append(tarea)
    
    def eliminar_tarea(self, tarea):
        for t in self.tareas:
            if t.descripcion == tarea.descripcion:
                self.tareas.remove(t)
                print(f"La tarea: '{tarea.descripcion}', ha sido eliminada.\n")
                return
        print(f"La tarea: '{tarea.descripcion}', no existe en tu lista de tareas.\n")
    
    def listar_tareas(self, tipo_tarea):
        if not isinstance(tipo_tarea, str):
            raise TypeError("El tipo de tarea debe ser una cadena (todas, pendientes, completadas).")
        
        tipo_tarea = tipo_tarea.lower()
        tareas_filtradas = []

        if tipo_tarea == 'todas':
            print("<--- Todas las tareas --->")
            tareas_filtradas = self.tareas

        elif tipo_tarea == 'pendientes':
            print("<--- Tareas pendientes --->")
            tareas_filtradas = [t for t in self.tareas if t.completada == 'NO']
            if not tareas_filtradas:
                print("No hay tareas pendientes.\n")

        elif tipo_tarea == 'completadas':
            print("<--- Tareas completadas --->")
            tareas_filtradas = [t for t in self.tareas if t.completada == 'SI']
            if not tareas_filtradas:
                print("No hay tareas completadas.\n")

        for i, tarea in enumerate(tareas_filtradas, start=1):
            print(f"{i}. {tarea}")
    
    def completar_tarea(self, tarea):
        for t in self.tareas:
            if t.descripcion == tarea.descripcion:
                t.completada = 'SI'
                print(f"La tarea: '{t.descripcion}' ha sido marcada como completada.\n")
                return
        print(f"La tarea: '{tarea.descripcion}' no existe en tu lista.\n")

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.tareas], f, indent=4)
        print(f"Tareas guardadas en '{nombre_archivo}'.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                tareas_data = json.load(f)
                self.tareas = [Tarea.from_dict(td) for td in tareas_data]
            print(f"Tareas cargadas desde '{nombre_archivo}'.\n")
        except FileNotFoundError:
            print(f"No se encontró el archivo '{nombre_archivo}'. Se empezará con una lista vacía.\n")

def mostrar_menu():
    print("===== GESTOR DE TAREAS =====")
    print("1. Agregar nueva tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Listar todas las tareas")
    print("5. Listar tareas pendientes")
    print("6. Listar tareas completadas")
    print("7. Guardar tareas")
    print("8. Salir")
    print("============================")

def main():
    admin = AdministradorTareas()
    archivo = "tareas.json"
    admin.cargar_desde_archivo(archivo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == '1':
            descripcion = input("Descripción de la tarea: ")
            fecha = input("Fecha de vencimiento (ej. 2025-05-02): ")
            nueva_tarea = Tarea(descripcion, fecha)
            admin.agregar_tarea(nueva_tarea)

        elif opcion == '2':
            descripcion = input("Descripción de la tarea a eliminar: ")
            tarea_a_eliminar = Tarea(descripcion, "fecha-desconocida") 
            admin.eliminar_tarea(tarea_a_eliminar)

        elif opcion == '3':
            descripcion = input("Descripción de la tarea a completar: ")
            tarea_a_completar = Tarea(descripcion, "fecha-desconocida")
            admin.completar_tarea(tarea_a_completar)

        elif opcion == '4':
            admin.listar_tareas('todas')

        elif opcion == '5':
            admin.listar_tareas('pendientes')

        elif opcion == '6':
            admin.listar_tareas('completadas')

        elif opcion == '7':
            admin.guardar_en_archivo(archivo)

        elif opcion == '8':
            admin.guardar_en_archivo(archivo)
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
