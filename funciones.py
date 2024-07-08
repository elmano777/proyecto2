from sklearn import datasets
datos = datasets.load_digits()
def hallarvalores(parecidos:list,cercanos:list):

    # Posiciones de los minimos:
    posiciones = []
    for i in parecidos:
        posicion = cercanos.index(i)
        posiciones.append(posicion)

    # Buscar los tarjets de los números:
    correctos = []
    for i in posiciones:
        correctos.append(int(datos["target"][i]))

    # Detectar el número más parecido:
    diccionario = {}
    for i in correctos:
        if i not in diccionario:
            diccionario[i] = 1
        else:
            diccionario[i] += 1

    numeros = list(diccionario.keys())
    valores = list(diccionario.values())

    return numeros,valores,diccionario
