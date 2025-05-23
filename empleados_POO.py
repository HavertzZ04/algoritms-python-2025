class Empleado:
    def __init__(self, nombre, id_empleado, cargo):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(id_empleado, int):
            raise TypeError("El ID del empleado debe ser un número entero.")
        if not isinstance(cargo, str):
            raise TypeError("El cargo debe ser una cadena de texto.")
            
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.cargo = cargo
        self.proyectos = []
        
    def __str__(self):
        return f"Trabajador: {self.nombre} - ID: {self.id_empleado} - Cargo: {self.cargo}"
        
    def asignar_proyecto(self, proyecto):
        if proyecto in self.proyectos:
            print(f"{self.nombre} ya está asignad@ al proyecto \"{proyecto.nombre}\".\n")
        else:
            self.proyectos.append(proyecto)
            proyecto.agregar_empleado(self)
            print(f"{self.nombre} ha sido asignad@ al proyecto:\n- {proyecto}.\n")
        
    def mostrar_proyectos(self):
        if not self.proyectos:
            print(f"{self.nombre} no tiene proyectos asignad@s aún.\n")
        else:
            print(f"Los proyectos de {self.nombre} son:")
            for i, proyecto in enumerate(self.proyectos, start=1):
                print(f"\t{i}. {proyecto}")
            print()
            
    def numero_proyectos(self):
        cantidad = len(self.proyectos)
        if cantidad == 0:
            print(f"{self.nombre} no tiene proyectos asignados aún.\n")
        else:
            print(f"{self.nombre} ha sido asignad@ a {cantidad} proyecto(s).\n")
    

class Proyecto:
    def __init__(self, nombre, codigo, duracion_meses):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(codigo, str):
            raise TypeError("El código debe ser una cadena de texto.")
        if not isinstance(duracion_meses, int) or duracion_meses <= 0:
            raise TypeError("La duración debe ser un número entero mayor a 0.")
            
        self.nombre = nombre
        self.codigo = codigo
        self.duracion_meses = duracion_meses
        self.empleados_asignados = []
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Código: {self.codigo} - Duración: {self.duracion_meses} mes(es)"
    
    def agregar_empleado(self, empleado):
        if empleado in self.empleados_asignados:
            print(f"{empleado.nombre} ya está asignad@ al proyecto \"{self.nombre}\".\n")
        else:
            self.empleados_asignados.append(empleado)
    
    def mostrar_empleados(self):
        if not self.empleados_asignados:
            print(f"{self.nombre} no tiene emplead@s asignad@s aún.\n")
        else:
            print(f"Los emplead@s del proyecto \"{self.nombre}\" son:")
            for i, empleado in enumerate(self.empleados_asignados, start=1):
                print(f"\t{i}. {empleado}")
            print()
            
    def numero_empleados(self):
        cantidad = len(self.empleados_asignados)
        if cantidad == 0:
            print(f"El proyecto {self.nombre} no tiene emplead@s asignad@s aún.\n")
        else:
            print(f"El proyecto {self.nombre} tiene asignad@(s) a {cantidad} emplead@(s).\n")


# Prueba del código
emp1 = Empleado("Laura", 101, "Desarrolladora")
emp2 = Empleado("Carlos", 102, "Diseñador UX")

proy1 = Proyecto("Sistema de Inventario", "PR-001", 6)
proy2 = Proyecto("App Móvil", "PR-002", 4)

# Asignar proyectos
emp1.asignar_proyecto(proy1)
emp1.asignar_proyecto(proy2)
emp2.asignar_proyecto(proy1)

# Mostrar proyectos por empleado
emp1.mostrar_proyectos()
emp1.numero_proyectos()

# Mostrar empleados por proyecto
proy1.mostrar_empleados()
proy1.numero_empleados()
