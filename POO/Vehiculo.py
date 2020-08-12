class Vehiculo():
        def __init__(self,color,ruedas):
            self.color=color
            self.ruedas=ruedas
        def mostrarColor(self):
            return "mi color  ", self.color
auto1=Vehiculo("verde",4)
print(auto1.mostrarColor())
class Autos(Vehiculo):
      def __init__(self, color,ruedas, cilindrada, velocidad):
            self.cilindrada= cilindrada
            self.velocidad=velocidad
            super().__init__(color,ruedas)
      def mostrarcilindrada(self):
            return self.cilindrada

class Bicicleta(Vehiculo):
      def __init__(self, color, ruedas, rodado):
            self.rodado=rodado
            super().__init__(color, ruedas)
      def mostarRodado(self):
            
            return self.color, "tengo ", self.ruedas, self.rodado
          
corolla=Autos("Rojo",4,1.6,200)
bici=Bicicleta('verde',2,26)

print(corolla.mostrarcilindrada())
print(bici.mostarRodado())