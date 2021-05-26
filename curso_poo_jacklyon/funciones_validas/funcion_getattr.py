class Persona:
    edad = 32
    nombre = 'raul'
    
doctor = Persona()
print(f'La edad es: {doctor.edad}')
print('la edad es: ', getattr(doctor,'edad'))

""" Esta funcion getting lo que hacemos es obtener el atributo de manera directa 
sin ingresar directamente al atributo"""
