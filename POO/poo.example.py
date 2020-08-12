class Persona:
    'Crea una nueva instancia de la clase persona'

    
    def __init__(self, nombre, edad, genero, estatura, peso):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.estatura = estatura
        self.peso = peso
        
    def hablar(self):
        print("Hola soy {}".format(self.estatura))
        
    
persona1 = Persona("Marcelo",15,'M',1.70,72)

Persona.hablar(persona1)

print(persona1.hablar())
class Cine:
    'Esta clase contiene las caracteristicas de cine'
    
    def __init__(self, nombreCine, direccion, precioEntrada):
        self.nombreCine = nombreCine
        self.direccion = direccion
        self.precioEntrada = precioEntrada
        
    def mostrarCine(self):
        return self.nombreCine
    
Cinemacenter=Cine('Cinemacenter Av. Ávalos', 'Duvivier 1815', '20')

print(Cine.mostrarCine(Cinemacenter))