class Estudiante:
    def __init__(self,nombre,apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def  __str__(self):
        return f'Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años.'

new_student = Estudiante('Ronaldinho','Farfan',19)
print(f'{new_student}')

#El metodo __str__es parecido al metodo __repr__