from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, grupo):
        Persona.__init__(self, nombre, apellido)
        #super().__init__(nombre, apellido)
        self.grupo = grupo

    def imprimirEstudiante(self):
        print("Estudiante: " + self.apellido + ", " + self.nombre + "; del grupo : " + self.grupo)

""""
x = Estudiante("Juan", "Perez", "Grupo 2")
x.imprimirNombreCompleto()
x.imprimirEstudiante()
"""