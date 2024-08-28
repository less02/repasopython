import math

'''resultado = math.sqr(168)
print("La raiz cuadrada es: ", resultado)'''

'''x1 = float(input("Ingrese las coordenadas X del primer punto: "))
y1 = float(input("Ingrese la coordenada Y del primero punto :"))

x2 = float(input("Ingrese las coordenadas X del segundo punto: "))
y2 = float(input("Ingrese las coordenadas Y del segundo punto: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print("La distancia entre los dos puntos es: ", distancia)'''


#Crear un programa que calcule el monto total depues de aplicar interés compuesto
#El usuario debe ingresar el capital inicial, la tasa de interés anual y el número de años
#La formula de interés compuesto es:
#M = P(1 + r / 100) t
#M es el monto final
#P es el capital inicial
#r es la tasa de interés anual
#t es el número de años

'''print("==============================================================")
print("Esta calculadora está diseñada para calcular interés compuesto")
capital = float(input("Ingrese cual es el capital inicial: "))
tasaI = float(input("Ingrese cual es la tasa de interés anual (%): "))
anios = int(input("Ingrese la cantidad de años: "))

montoFinal = capital * (1 + tasaI / 100) * anios

print(f"El monto total despues de {anios} años es {montoFinal}")'''


'''print("==============================================================")
texto = input("Ingrese el mensaje")

mayuscula = texto.upper() #en mayuscula
minuscula = texto.lower() #en minuscula
titulo = texto.title() #inicial en mayuscula

print("El texto en mayuscula es: ")
print("El texto en minuscula es: ")
print("El texto en titulo es: ")'''

#Crear un programa en Python que muestre la fecha y hora actual en un
#formato legible utilizando el módulo detetime

'''print("==============================================================")
import datetime
fechaHoraActual = datetime.datetime.now()

print(fechaHoraActual)
#formato fecha y hora
fechaFormato = fechaHoraActual.strftime("%d/%m/%Y %H:%M:%S")'''


#Escribe un programa en Python que genere un número aleatorio entre 1 y 100 utilizando el módulo random
'''import random
numeroAleatorio = random.randint(1,100)
print("El número aleatorio generado es: ", numeroAleatorio)'''