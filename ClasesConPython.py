class Curso:
	def get_name(self):
		return  "Tecnologia"
class Carrera:
    def __init__(self, name):
        self.name=name
    def get_name(self):
        return self.name
    def imprime(self):
        print("imprime algo")
def suma (a, b):
        return a+b

curso = Curso()
print(curso.get_name())
print(suma(2,4))
carrera= Carrera("sistemas")
print(carrera.get_name()) #comentario
""" cometario
de varias lineas"""


