class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print("Hola, Mundo")

class employee(Persona):
    def __init__(self,nombre,edad, salario, trabajo):
        super().__init__(nombre, edad)
        self.salario = salario
        self.trabajo = trabajo
    def decirTrabajo(self):
        print(f"Mi trabajo es {self.trabajo}")

empleado = employee("julian",21,1,"Rappi")
empleado.saludar()
empleado.decirTrabajo()
