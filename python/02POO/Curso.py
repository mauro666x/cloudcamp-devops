from Estudiante import Estudiante
from Profesor import Profesor

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.estudiantes = []
        self.profesor = profesor
    
    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def imprimirCurso(self):
        print("Curso: " + self.nombre + " con el profesor: "+self.profesor.nombre)
        if len(self.estudiantes) == 0:
            print("Sin estudiantes")
        else:
            for estudiante in self.estudiantes:
                estudiante.imprimirEstudiante()

"""
x = Curso("DevOps 2024-2", Profesor("Jhonny", "Pong", "DevOps"))
x.imprimirCurso()
x.agregarEstudiante(Estudiante("Juan", "Perez", "Grupo 2"))
x.imprimirCurso()
"""