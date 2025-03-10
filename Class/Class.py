#Asi se crea una clase
class Persona(): #Usamos class y el nombre de nuestra clase
    def __init__(self, nombre, edad):#Inicializamos nuestros atributos
        self.nombre = nombre #Les asignamos valor a estos atributos
        self.edad = edad

    def saludar(self):
        print(f"Hola, Mundo mi nombre es {self.nombre}")

#Creacion de persona
persona1 = Persona("Carlos Sierra", 28)
persona1.saludar()