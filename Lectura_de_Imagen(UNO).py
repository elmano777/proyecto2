from sklearn import datasets
import cv2
from math import sqrt
from funciones import hallarvalores

#Cargo los datos de los números:
datos = datasets.load_digits()

#Leer imagen en escala de grises:
primeraimg = cv2.imread("imgs/yeimi.png", cv2.IMREAD_GRAYSCALE)

#Rescalo la dimensión de la imagen:
rescalar = cv2.resize(primeraimg,(8,8))

#Rescalo el valor de los colores:
for i in range(8):
    for j in range(8):
        rescalar[i][j] = 255 - rescalar[i][j]
        rescalar[i][j] = rescalar[i][j] / 255 * 16

#Hallo su distancia euclidiana:
distacia = 0
cercanos = []
for total in range(len(datos["data"])):
    for i in range(8):
        for j in range(8):
            distacia += (rescalar[i][j]-datos["data"][total][i*8+j])**2
    distacia_eu = sqrt(distacia)
    cercanos.append(distacia_eu)
    distacia = 0

#Indentificar los 3 numeros con menor distancia:
parecidos = [float('inf'), float('inf'), float('inf')]
for numero in cercanos:
    if numero < parecidos[0]:
        parecidos = [numero, parecidos[0], parecidos[1]]
    elif numero < parecidos[1]:
        parecidos = [parecidos[0], numero, parecidos[2]]
    elif numero < parecidos[2]:
        parecidos = [parecidos[0], parecidos[1], numero]

#Llamo a la funcion para identificar los numeros parecidos:
numeros, valores, diccionario = hallarvalores(parecidos, cercanos)
maximo = max(valores)

#Identificar que halle un valor parecido:
if valores.count(maximo) > 1:
    parecidos = [float('inf'), float('inf'), float('inf'), float('inf')]
    for numero in cercanos:
        if numero < parecidos[0]:
            parecidos = [numero, parecidos[0], parecidos[1], parecidos[2]]
        elif numero < parecidos[1]:
            parecidos = [parecidos[0], numero, parecidos[2], parecidos[3]]
        elif numero < parecidos[2]:
            parecidos = [parecidos[0], parecidos[1], numero, parecidos[3]]
        elif numero < parecidos[3]:
            parecidos = [parecidos[0], parecidos[1], parecidos[2], numero]

    #Llamo a la funcion para identificar los numeros parecidos:
    numeros, valores, diccionario = hallarvalores(parecidos, cercanos)
    maximo = max(valores)

#Mostrar el resultado:
if valores.count(maximo) > 1:
    #Mensaje al usuario(ERROR):
    print("No se puede identificar el número del dibujo, ingrese otra imagen porfavor.")
else:
    maximo = max(valores)
    index = valores.index(maximo)
    valorfinal = numeros[index]

    #Mensaje al usuario:
    print("Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al "
          "número", valorfinal, ",donde", valorfinal, "es un número entre 0 y 9.")

print(diccionario)
print(rescalar)







