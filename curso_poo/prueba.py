# comentario agregado desde git hub
class Auto:
    def __init__(self,marca='default',modelo='default',placa='000000'):
        print(f'Propiedades de coche')
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
mi_coche = Auto('Renauld','xSD5s','g5xxd')
print(mi_coche.placa)
