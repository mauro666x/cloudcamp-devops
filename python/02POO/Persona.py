class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def imprimirNombreCompleto(self):
        print("Nombre: " + self.apellido + ", " + self.nombre )


"""
x = Persona("Juan", "Perez")
x.imprimirNombreCompleto()
"""