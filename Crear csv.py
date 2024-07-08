from sklearn import datasets
import pandas as pd

#Cargo los datos de los números:
datos = datasets.load_digits()

#Imprimo las listas:
img1 = pd.DataFrame(datos["images"][0])
for i in range(1,len(datos["images"])):
    a = pd.DataFrame(data=datos["images"][i])
    separador = pd.DataFrame(data=[[0]*8])
    img2 = pd.concat([img1 , separador],ignore_index=True)
    img1 = pd.concat([img2 , a],ignore_index=True)
separador = pd.DataFrame(data=[[0]*8])
img1 = pd.concat([img1 , separador],ignore_index=True)

#Imprimir los tarjets:
lista = []
for i in range(len(datos["target"])):
    for j in range(9):
        lista.append(datos["target"][i])

#Imprimir el CSV:
img1["target"] = lista
"""img1.to_csv("Final.csv")"""