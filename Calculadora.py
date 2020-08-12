#declaro la funcion calculadora y las subfunciones por cada una de las operaciones básicas
def calculadora(Operacion, num1, num2):
    
    def suma(num1, num2):
        return int(num1)+int(num2)

    def resta(num1, num2):
        return int(num1)-int(num2)

    def multiplicacion(num1, num2):
        return int(num1)*int(num2)

    def division(num1, num2):
        return int(num1)/int(num2)
        
    if Operacion ==1:    
        return (f"El resultado de la suma es: {suma(num1,num2)}")
    elif Operacion ==2:
        return (f"El resultado de la resta es: {resta(num1,num2)}")
    elif Operacion ==3:
        return (f"El resultado de la multiplicación es: {multiplicacion(num1,num2)}")
    elif Operacion ==4:
        try:
            return (f"El resultado de la división es: {division(num1,num2)}")
        except:
            return("No se puede dividir un número por cero.")
         
#creo una lista con las opciones de las operaciones    
listaopciones=["1","2","3","4"]
#pido al usuario que ingrese una opción
operacion = input("Ingrese la operación: \n 1-Suma \n 2-Resta \n 3-Multiplicación \n 4-División \n o cualquier otro caracter para salir. \n")


while operacion  in listaopciones:
    pOperacion = int(operacion)
    numero1 = input("Ingrese el primer número: \n")
    numero2 = input("Ingrese el segundo número: \n")    
    print(calculadora(pOperacion,numero1, numero2))
    continuar=input('Desea continuar? \n 1-SI \n 2-NO \n')
    if continuar=='2':
        operacion=0
    else:
        operacion = input("Ingrese la operación: \n 1-Suma \n 2-Resta \n 3-Multiplicación \n 4-División \n o cualquier otro caracter para salir. \n")
print("Adios!")
    