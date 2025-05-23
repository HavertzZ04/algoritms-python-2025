class Curso:
    def __init__(self, nombre, codigo, creditos):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(codigo, str):
            raise TypeError("El código debe ser una cadena de texto.")
        if not isinstance(creditos, int):
            raise TypeError("Los créditos deben ser números enteros.")
        
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.estudiantes = []
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - {self.creditos} créditos"
        
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print(f"El curso {self.nombre} aún no tiene estudiantes.")
        else:
            print(f"Esta es la lista de estudiantes del curso {self.nombre}:")
            for i, estudiante in enumerate(self.estudiantes, start=1):
                print(f"{i}. {estudiante}")

                
class Estudiante:
    def __init__(self, nombre, edad):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        
        self.nombre = nombre
        self.edad = edad
        self.cursos = []
        
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
        
    def inscribirse(self, curso):
        if curso in self.cursos:
            print(f"{self.nombre} ya está inscrito en el curso {curso.nombre}.")
            return
        
        self.cursos.append(curso)
        curso.agregar_estudiante(self)
        
    def mostrar_cursos(self):
        if not self.cursos:
            print(f"{self.nombre} no está inscrito en ningún curso.")
        else:
            print(f"Los cursos de {self.nombre} son:")
            for i, curso in enumerate(self.cursos, start=1):
                print(f"{i}. {curso}")
                

# Prueba del código
curso1 = Curso("Matemáticas", "DK-22", 7)
curso2 = Curso("Lenguas", "AM-55", 5)

estudiante1 = Estudiante("Jahir", 26)
estudiante2 = Estudiante("Johan", 26)

curso1.mostrar_estudiantes()
estudiante1.mostrar_cursos()

estudiante1.inscribirse(curso1)
estudiante1.mostrar_cursos()
curso1.mostrar_estudiantes()

estudiante2.inscribirse(curso1)
estudiante2.inscribirse(curso2)
estudiante2.inscribirse(curso1)

curso1.mostrar_estudiantes()
