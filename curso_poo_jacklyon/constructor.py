# metodo constructor

class Persona:
    pass
    def __init__(self,nombre,fecha):
        self.nombre = nombre
        self.fecha = fecha

    def description(self):
        print(f'{self.nombre} tiene {self.fecha} años')

usr1 = Persona('Ronal',20)
usr1.description()