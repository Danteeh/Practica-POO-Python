class Carro:
    def claxon(self):
        return " sonido claxon carro"

class Moto:
    def claxon(self):
        return " sonido claxon moto"



def PresionarClaxon(vehiculo):
    print(vehiculo.claxon())

moto = Moto()
carro = Carro()


PresionarClaxon(carro)