class Cuenta():
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    def menu(self):
        print('---MENU---')
        print('1- Mostrar datos de la cuenta')
        print('2- Ingresar cantidad')
        print('3- Retirar cantidad')
        print('4- Salir')
        opcion = int(input('Seleccione una opción: '))

        while True:
            if opcion == 1:
                self.mostrar()
            elif opcion == 2:
                self.ingresar()
            elif opcion == 3:
                self.retirar()
            elif opcion == 4:
                print('Ha cerrado sesión')
                exit()
            else:
                print('ERROR - Opción no válida')
            
            self.menu()
            break

    def mostrar(self):
        print(f'Titular de la cuenta:{self.titular}\nCantidad en cuenta:{self.__cantidad}')
    
    def ingresar(self):
        monto = float(input('Ingrese el monto: '))
        if monto > 0:
            self.__cantidad += monto
        else:
            print('No válido')
    
    def retirar(self):
        monto = float(input('Ingrese el monto: '))
        if monto > 0:
             self.__cantidad -= monto
       

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        Cuenta.__init__(self, titular, cantidad=0)
        self.bonificacion = bonificacion

    def esTitularValido(self):
        edad = int(input('Ingrese edad: '))
        if edad > 18 and edad < 25:
            es_titular = True
        else:
            es_titular = False
        return es_titular
    
    def menu(self):

        if esTitularValido():

            print('---MENU---')
            print('1- Mostrar datos de la cuenta')
            print('2- Ingresar cantidad')
            print('3- Retirar cantidad')
            print('4- Salir')
            opcion = int(input('Seleccione una opción: '))

            while True:
                if opcion == 1:
                    self.mostrar()
                elif opcion == 2:
                    self.ingresar()
                elif opcion == 3:
                    self.retirar()
                elif opcion == 4:
                    print('Ha cerrado sesión')
                    exit()
                else:
                    print('ERROR - Opción no válida')
                
                self.menu()
                break
    
    def mostrar(self):
        print('CUENTA JOVEN')
        print(f'Titular de la cuenta:{self.titular}\nCantidad en cuenta:{self.__cantidad}\nBonificación:{self.bonificacion}')

    def ingresar(self):
        monto = float(input('Ingrese el monto: '))
        if monto > 0:
            self.__cantidad += monto
        else:
            print('No válido')
    
    def retirar(self):
        monto = float(input('Ingrese el monto: '))
        if monto > 0:
             self.__cantidad -= monto


            

cuenta1 = Cuenta('Juan Perez', 1000)
cuenta_joven1 = CuentaJoven('Juan Perez', 1000, '50%')

cuenta_joven1.menu()