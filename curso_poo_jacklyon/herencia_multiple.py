# HERENCIA MULTIPLE

class Telefono:
    def __init__(self):
        pass

    def llamara(self):
        print('Llamando ...')

    def ocupado(self):
        print('Ocupado...')

class Camara:
    def __init__(self):
        pass

    def fotografiar(self):
        print('tomando Fotografia')

class Reproductor:
    def __init__(self):
        pass

    def reproducir_musica(self):
        print('reproduciendo musica')

    def reproducir_video(self):
        print('reproduciendo video..')

class Smartphone(Telefono,Camara,Reproductor):
    def __del__(self):
        print('Telefono apagado')
    
cilo = Smartphone()
print(cilo.fotografiar())
        