from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, especialidad):
        #Persona.__init__(self, nombre, apellido)
        super().__init__(nombre, apellido)
        self.especialidad = especialidad

    def imprimirProfesor(self):
        print("Profesor: " + self.apellido + ", " + self.nombre + "; con especialidad : " + self.especialidad)

"""
x = Profesor("Juan", "Perez", "DevOps")
x.imprimirNombreCompleto()
x.imprimirProfesor()
"""