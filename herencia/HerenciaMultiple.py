class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, Mundo mi nombre es {self.nombre}")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def decir_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")


class EmpleadoArtista(Artista, Persona):
    def __init__(self, nombre, edad,habilidad,salario,empresa):
        Persona.__init__(self, nombre, edad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    def hablar(self):
        print(f"Mi empresa es {self.empresa}")

employee = EmpleadoArtista("Julian del mar", 22,"RappiChambear", "Recoleccion de moneda","Transmilenio SA")
employee.saludar()
employee.hablar()
employee.decir_habilidad()