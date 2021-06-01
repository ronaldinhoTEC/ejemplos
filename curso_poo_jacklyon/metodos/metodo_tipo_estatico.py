import math

class Pastel:
    def __init__(self,ingredientes,tamano):
        self.ingredientes = ingredientes
        self.tamano = tamano

    def __repr__(self):
        return (f'Pastel({self.ingredientes}, 'f'{self.tamano})')

    def area(self):
        return self.tamano_area(self.tamano)

    @staticmethod
    def tamano_area(A):
        return A ** 2 * math.pi

pastel_nuevo = Pastel(['harina','Azucar','leche','crema'],4)
print(pastel_nuevo.tamano)
