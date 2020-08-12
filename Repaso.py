'''usuario = {
    'nombre':'juan perez',
    'domicilio':{
        'calle':'Calle Falsa 123',
        'localidad':'Saenz Peña'
    },
    'nivel':'basico'
}

print(usuario['domicilio'].get('localidad'))
'''
'''
verduras =['papa','cebolla','rucula','batata','lechuga']
#contador=0
for contador, una_verdura in enumerate(verduras):
    print(f'En la posición {contador} esta una {una_verdura}')

'''
'''
def una_funcion_valor(nro):
    """Paso por valor"""
    nro=nro+3
    print(f"Valor dentro de la funcion {nro}")
nro=22
una_funcion_valor(nro)
print(f"Valor fuera de la funcion {nro}")
'''
'''
colores=['azul','rojo','amarillo','negro']
print(colores[-3])
print(colores[3])
'''
'''
animal ='León'

def mostar_animal():
    """ Esta funcion muestra el valor de la variable animal """
    #global animal
    animal='Ballena'
    print(animal)
mostar_animal()
print(animal)

'''
'''
valor=float(input())
if valor<=5:
    print('bajo')
elif valor <=10:
    print('medio')
else:
    print('alto')
    '''
'''
def saludo():
    print("Hola Mundo")

saludo()
'''
'''
edades =(5,25,2,18,22,45,50,1,80,10)
cont=0

for i in edades
    if i>20:
        cont +=1
        
print(f'hay {cont} numeros mayores a 20')
'''
'''
for letra in "Python":
if letra == 'h':
continue
print('erre')
'''
'''
variable='5'
variable= int(variable)
print(type(variable))
'''
'''
animales= ('perro', 'gato', 'gallina',('canario','loro','guacamayo'),['leon','puma','yaguareté'] )
obt_loro = animales[3][1]
obt_puma = animales[4][1]
print(obt_loro)
print(obt_puma)
'''
'''
nombre= input("Ingrese su nombre por favor:")
'''
'''
vocales =('a','e','i','o','u')

mostrar_pos = vocales[2]

print("el la posicion 2 se encuentra la letra: ", mostrar_pos)
'''
'''
try:
    for vocales in "Python":
        if letra =="h":
            pass
        print("Letrar actual :", letra)
except Exception as e:
    print("Ha ocurrido un error no previsto ", type(e).__name__)
    for letra in "Python":
        if letra=="h":
            pass
        print("Letra actual :", letra)
'''
'''
def sumaNumeros(numero1,numero2):
    return numero1 + numero2
#resultado= sumaNumeros(5,10)
sumaNumeros(5,2)
'''
'''
def una_funcion_referencia(lista):
    
    lista.append(3500)
    print(f"Este es el contenido de la lista una vez ejecutada la funcion: {lista}")
    
lista = [50,80,100]
una_funcion_referencia(lista)
print(f"Este es el contenido de la lista al llamarla fuera de la funcion una vez ejecutada: {lista}")
'''
'''
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

 
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumaDigitos(sumatoria))
'''
'''
a=1
while a in range (5):
    print(a)
'''
'''
from random import shuffle

x =['Tener','El','Azul','Bandera','Volar','Alto']

shuffle(x)
print(len(x))
print(x)
'''
'''
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)
'''
'''
materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]

print(materias["domingo"])
'''
'''
d = {'juan':40, 'pedro':45}
print(d)
'''
'''
diccionario={'Pais':'India','Capital':'Delhi','PM':'Modi'}

print(diccionario['Pais'])
'''
