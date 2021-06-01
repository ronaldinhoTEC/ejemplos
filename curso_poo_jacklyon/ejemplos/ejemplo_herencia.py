class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def dato(self):
        self.datos = [int(input('Ingresa datos'+ str(i+1)+'= ')) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def sumar(self):
        a,b, = self.datos
        suma = a + b
        print(f'el resultado de {a} + {b} es: {suma}')

    def restar(self):
        a,b, = self.datos
        resta = a - b
        print(f'    El resultado de {a} - {b} es: {resta}')

    def multiplicar(self):
        a,b, = self.datos
        producto = a * b
        print(f'el resultado de {a} x {b} es: {producto}')

    def dividir(self):
        a,b, = self.datos
        division = a // b
        print(f'el resultado de {a} + {b} es: {division}')

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def cuadrada(self):
        import math
        a, = self.datos
        print(f'El resultado es: {math.sqrt(a)}')

objeto = Op_basicas()

print(issubclass(Raiz,Calculadora))

