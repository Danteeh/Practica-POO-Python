#Crear una clase estudoante la cual contenga como atributos nombre edad y grado y un metodo donde saque un mensaje con el nombre del estudiante y que esta estudiando
class Estudiante:
    def __init__(self, nombre, edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre}  esta estudiando")

nombre = input("Introduce el nombre: ")
edad  =  input("Introduce el edad: ")
grado =  input("Introduce el grado: ")
estudiante1 = Estudiante(nombre, edad, grado)


while True:
    estudiar = input()
    if estudiar == "Estudiar":
        estudiante1.estudiar()
    elif estudiar == "salir":
        break
