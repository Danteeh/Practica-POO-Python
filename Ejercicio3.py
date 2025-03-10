#PreRequisito recordar MRO
"""
Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal", "Mamifero" y
"Ave". La clase "Animal" debe tener un método llamado "comer". La clase "Mamifero" debe tener
un método llamado "amamantar" y la clase "Ave" un método llamado "volar".
hora, crea una clase "Murcielago" que herede de "Mamjfero' y "Ave", en ese orden, y por 10 tanto
debe ser capaz de "amamantar" y "volar", además de "comer".
Finalmente, juega con el orden de herencia de la clase "Murcielagp" y observa cómo cambia el
MRO y el comportamiento de los métodos al usar super().
"""

class Animal:
    def __init__(self):
      pass
    def comer(self):
        print("comer")

class Mamifero(Animal):
    def __init__(self):
        pass
    def amamantar(self):
        print("amamantar")

class  Ave(Animal):
    def __init__(self):
        pass
    def volar(self):
        print("volar")



class Murcilago(Mamifero,Ave):
     pass


murcielago = Murcilago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()