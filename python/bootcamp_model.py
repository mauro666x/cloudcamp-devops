class Persona:
    # nombre
    # apellido
    # edad

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def imprimirNombreCompleto(self):
        print("Nombre completo: "+ self.nombre + " " + self.apellido)

    def imprimirEdad(self):
        print("Edad: " + str(self.edad))


class Estudiante(Persona):
    # nombre
    # apellido
    # edad
    # codigo
    # grupo

    def __init__(self, nombre, apellido, edad, codigo, grupo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.codigo = codigo
        self.grupo = grupo

    def imprimirEstudiante(self):
        print("Estudiante: " + self.nombre + ", codigo: " + str(self.codigo) + " del grupo: " + self.grupo)

class Profesor(Persona):
    # nombre
    # apellido
    # edad
    # especialidad

    def __init__(self, nombre, apellido, edad, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.especialidad = especialidad

    def imprimirProfesor(self):
        print("Profesor: " + self.nombre +  ", Especialidad: " + self.especialidad)

class Curso:

    def __init__(self, profesor, horario, intensidad, id, nombre):
        self.estudiantes = []
        self.profesor = profesor

    def agregarEstudiante(self, estudiante):
        self.estudantes.append(estudiante)
    
    def imprimirCurso(self):
        print()
        self.profesor.imprimirProfesor()
        for estudiante in self.estudiantes:
                estudiante.imprimirEstudiante()









persona = Persona("Mauricio", "Benavides", 20)
persona.imprimirNombreCompleto()
persona.imprimirEdad()

naruto = Estudiante("Naruto", "Uzumaki", 21, 111, "Devops Group")
naruto.imprimirNombreCompleto()
naruto.imprimirEstudiante()

pr = Profesor("Jiraya", "Sensei", 50, "Jutsus")
pr.imprimirNombreCompleto()
pr.imprimirProfesor()