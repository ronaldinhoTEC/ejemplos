#esta es la rama pruebas 

from datetime import datetime
fecha = datetime.now().time()
class Perro:
    def __init__(self , nombre , color , raza , tamano):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.tamano = tamano
        print(f'Informacion sobre este animal \n'
              f'Nombre: {nombre}\n'
              f'Color: {color}\n'
              f'Raza: {raza}\n'
              f'Tamaño: {tamano}\n')

    def ladrar(self,fuerza):
        self.fuerza = fuerza
        if fuerza == 'fuerte':
            print('Waaaaaaaaaaaaaaww fuerte')
        elif fuerza == 'medio':
            print('waaaaw medio')
        elif fuerza == 'bajo':
            print('waw xd ')

    def comer(self, tipo ='favoritos'):
        #self.comida = comida
        self.tipo = tipo
        favoritos = ['arroz','lechuga','platano','pera','espinaca','carne']
        moderado = ['sandia','piña','brololi','papa','manzana','pan','fresa']
        no_recomendado = ['porcorn','maiz','apion','rocoto']
        rechazados = ['palta','cerveza','chocolate','ajos','uvas','dulces']
        tipo_comida= input('Introduce el tipo de comida: ')
        if tipo_comida == 'favoritos':
            print(f'ALIMENTOS FAVORITOS: \n')
            for i in favoritos:
                print(f'          {i.title()}')

        elif tipo_comida == 'moderado':
            print(f'COMIDA MODERADA')
            for i in moderado:
                print(f'          {i.title()}')
        elif tipo_comida == 'no recomendado':
            print(f'COMIDA NO RECOMENDADA')
            for i in no_recomendado:
                print(f'          {i.title()}')
        elif tipo_comida == 'rechazados':
            print(f'COMIDA RECHAZADA')
            for i in rechazados:
                print(f'          {i.title()}')

    def dormir(self):
        print(f'zzz')

    def correr(self):
        pass

doby = Perro('doby','negro','Doberman','Grande')
doby.dormir()
