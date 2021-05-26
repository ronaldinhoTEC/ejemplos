class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def description(self):
        print(f'Añadiste un pokemon :\n'
              f'    Nombre: {self.nombre}\n'
              f'    Tipo: {self.tipo}')

class Electrico(Pokemon):
    def ataque(self,nombre_ataque):
        self.nombre_ataque = nombre_ataque
        print(f'Este pokemos tiene el ataque de: {nombre_ataque}')

mi_poke = Electrico('Pika','Electrico')
mi_poke.description()
mi_poke.ataque('impactrueno')
