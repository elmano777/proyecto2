from sklearn import datasets
import cv2
from math import sqrt

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
for total in range(10):
    for i in range(8):
        for j in range(8):
            distacia += (rescalar[i][j]-datos["data"][total][i*8+j])**2
    distacia_eu = sqrt(distacia)
    cercanos.append(distacia_eu)
    distacia = 0

ubicacion = cercanos.index(min(cercanos))
valorfinal = datos["target"][ubicacion]
print("Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al "
          "número", valorfinal, ",donde", valorfinal, "es un número entre 0 y 9.")