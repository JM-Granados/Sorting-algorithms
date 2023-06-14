from logging import raiseExceptions
from random import randint
from time import time 
import matplotlib.pyplot as plt

#medir tiempo, análisis
def medirTiempo(funcion, final, incremento):
    """
    Subrutina que se encarga medir el tiempo de ejecución
    de un algoritmo de ordenamiento. Realiza varias pruebas
    e imprime el promedio de ejecución.
    Entradas y restricciones:
    - funcion: debe ser un objeto función.
    - final: cantidad de elementos final para las pruebas.
    - incremento: aumento en el tamaño de las pruebas
    - cantidad: cantidad de pruebas, entero positivo.
    Salidas:
    Dos listas, una con los tamaños de lista utilizados en las pruebas, y otra con los promedios de ejecución
    por cada tamaño de la lista.
    """
    if type(final) != int and final < 0:
        raise Exception("La cantidad de elementos final para las pruebas debe ser entero positivo.")
    if type(incremento) != int and incremento < 0:
        raise Exception("El incremento de elementos para las pruebas debe ser entero positivo.")
    inicio = 100
    cantidad = 10
    print(f"Algoritmo: {funcion.__name__}:")
    tamaños = []
    promedios = []
    for t in range(inicio, final + 1, incremento):
        print(f"Ordenando {t} elementos.")
        duraciones = []
        for i in range(cantidad):
            Lista = generarLista(t)
            time0 = time()
            funcion(Lista)
            time1 = time()
            duracion = time1 - time0
            duraciones.append(duracion)
            if duracion > 10:
                return tamaños, promedios
        promedio = sum(duraciones) / len(duraciones)
        tamaños.append(t)
        promedios.append(promedio)
        print(f"Duración promedio de {cantidad} pruebas de {t} elementos: {promedio}")
    return tamaños, promedios


#Gráfica
def grafico():
    """
    Función que grafica los datos obtenidos de medirTiempo basados en los algoritmos.
    Entradas y restricciones:
    - L1, L2 : listas con los datos obtenidos en medirTiempo.
    Salida:
    Gráfica con datos.
    """
    bubbleSortN = [100, 600, 1100, 1600, 2100, 2600, 3100, 3600, 4100, 4600, 5100, 5600, 6100, 6600, 7100, 7600]
    bubbleSortT = [0.000712442398071289, 0.035685038566589354, 0.14932260513305665, 0.3600119352340698, 0.5657344341278077, 1.038810920715332, 1.3559424877166748, 1.8546303510665894, 2.348458671569824, 2.9581933498382567, 3.9686230182647706, 4.8704866647720335, 4.5480228662490845, 5.94755322933197, 6.75989408493042, 8.004982590675354]
    insertionSortN = [100, 600, 1100, 1600, 2100, 2600, 3100, 3600, 4100, 4600, 5100, 5600, 6100, 6600, 7100, 7600, 8100, 8600]
    insertionSortT = [0.0005983352661132812, 0.0368973970413208, 0.1409754276275635, 0.2795954465866089, 0.4748647451400757, 0.8068522691726685, 1.2611597299575805, 1.7814953565597533, 2.244008755683899, 3.125412440299988, 3.258039712905884, 3.7487046241760256, 4.593561339378357, 4.85471920967102, 6.168131041526794, 6.710570764541626, 7.818587422370911, 9.028725075721741]
    selectionSortN = [100, 600, 1100, 1600, 2100, 2600, 3100, 3600, 4100, 4600, 5100, 5600, 6100, 6600, 7100, 7600, 8100, 8600, 9100, 9600, 10100]
    selectionSortT = [0.0006958246231079102, 0.020000624656677245, 0.06812078952789306, 0.165253210067749, 0.2785155773162842, 0.3974995851516724, 0.5372956752777099, 0.7281533718109131, 0.9447955131530762, 1.3766152381896972, 1.9164446592330933, 2.320447015762329, 2.6114237785339354, 3.0048901557922365, 2.8640136241912844, 3.668128418922424, 3.985926961898804, 4.849565100669861, 5.08129050731659, 5.556162309646607, 6.602257537841797]
    mergeSortN = [100, 1100, 2100, 3100, 4100, 5100, 6100, 7100, 8100, 9100, 10100, 11100, 12100, 13100, 14100, 15100, 16100, 17100, 18100, 19100, 20100, 21100, 22100]
    mergeSortT = [0.0002958059310913086, 0.005093026161193848, 0.01026928424835205, 0.01650371551513672, 0.02422952651977539, 0.028622889518737794, 0.03765826225280762, 0.05542147159576416, 0.05515244007110596, 0.08144323825836182, 0.07255415916442871, 0.0920494794845581, 0.09843027591705322, 0.09905068874359131, 0.1186997652053833, 0.12931745052337645, 0.14696946144104003, 0.1411673307418823, 0.14943060874938965, 0.16945037841796876, 0.16474432945251466, 0.17444732189178466, 0.22825486660003663]
    quickSortN = [100, 1100, 2100, 3100, 4100, 5100, 6100, 7100, 8100, 9100, 10100, 11100, 12100, 13100, 14100, 15100, 16100, 17100, 18100, 19100, 20100, 21100, 22100]
    quickSortT = [0.0001035451889038086, 0.004188108444213867, 0.005894136428833008, 0.010275721549987793, 0.014898324012756347, 0.017302846908569335, 0.02121114730834961, 0.0484844446182251, 0.02841627597808838, 0.03837199211120605, 0.05039424896240234, 0.043699049949646, 0.06291835308074951, 0.08056116104125977, 0.05893640518188477, 0.055700135231018064, 0.06751608848571777, 0.0768383264541626, 0.08120915889739991, 0.08400278091430664, 0.0898050308227539, 0.0856848955154419, 0.10981917381286621]
    plt.plot(bubbleSortN, bubbleSortT, label = "BubbleSort")
    plt.plot(insertionSortN, insertionSortT, label = "InsertionSort")
    plt.plot(selectionSortN, selectionSortT, label = "SelectionSort")
    plt.plot(mergeSortN, mergeSortT, label = "MergeSort")
    plt.plot(quickSortN, quickSortT, label = "QuickSort")
    plt.xlabel("Cantidad de datos")
    plt.ylabel("Segundos")
    plt.title("Algoritmos de Ordenamientos")
    plt.legend()
    plt.show()



#generar listas al azar
def generarLista(n):
    """
    Función que genera una lista de números enteros aleaorios de tamaño n.
    Entradas y restricciones:
    - n: un entero positivo.
    Salidas:
    Lista de tamaño n con enteros aleatorios.
    """
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return [randint(0, 5000) for x in range(n)]


#Algoritmos de ordenamiento

#Primer algoritmo de ordenamiento
def bubbleSort(L):
    """
    Algoritmo de ordenamiento Bubble sort.
    Entradas y restricciones:
    - L : una lista de elementos a ordenar.
    Salida:
    L ordenada ascendentemente.
    """
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    iteracion = 0
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(L) - 1 - iteracion):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                intercambio = True
        iteracion += 1
    return L

#Segundo algoritmo de ordenamiento
def insertionSort(L):
    """
    Algoritmo de ordenamiento Insertion sort.
    Entradas y restricciones:
    - L : una lista de elementos a ordenar.
    Salida:
    L ordenada ascendentemente.
    """
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j] < L[j - 1]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1
    return L

#Tercer algoritmo de ordenamiento
def selectionSort(L):
    """
    Algoritmo de ordenamiento Insertion sort.
    Entradas y restricciones:
    - L : una lista de elementos a ordenar.
    Salida:
    L ordenada ascendentemente.
    """
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    for iteracion in range(len(L) - 1):
        posMenor = iteracion
        for i in range(iteracion + 1, len(L)):
            if L[i] < L[posMenor]:
                posMenor = i
        L[iteracion], L[posMenor] = L[posMenor], L[iteracion]
    return L

#Cuarto algoritmo de ordenamiento
def mergeSort(L):
    """
    Algoritmo de ordenamiento merge sort.
    Entradas y restricciones:
    - L : lista de elementos.
    Salida:
    Lista L ordenada ascendentemente.
    """
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return mergeSortAux(L)

def mergeSortAux(L):
    """
    Función auxiliar de mergeSort.
    """
    if len(L) == 1:
        return L
    else:
        izq = mergeSortAux(L[: len(L) // 2])
        der = mergeSortAux(L[len(L) // 2:])
        L = merge(izq, der)
        return L

def merge(izq, der):
    """
    Función que recibe dos listas ordenadas y las une en una única lista ordenada.
    Entradas y restricciones:
    - izq, der: Listas ordenadas ascendentemente
    Salidas:
    Una única lista ordenada
    """
    resultado = []
    while izq != [] and der != []:
        if izq[0] <= der[0]:
            resultado.append(izq.pop(0)) #.pop: agrega un elemento y lo borra de la prosecencia
        else:
            resultado.append(der.pop(0))
    resultado.extend(izq + der)
    return resultado

#Quinto algoritmo de ordenamiento 
def quickSort(L):
    """
    Algoritmo de ordenamiento quick sort.
    Entradas y restricciones:
    - L: Listas de elementos.
    Salida:
    Lista L ordenada ascendentemente.
    """
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return quickSortAux(L)

def quickSortAux(L):
    """Función auxiliar de quickSort."""
    if len(L) <= 1:
        return L
    else:
        pivote = L.pop(len(L) // 2)
        menores = [x for x in L if x < pivote]
        mayores = [x for x in L if x >= pivote]
        menores = quickSortAux(menores)
        mayores = quickSortAux(mayores)
        return menores + [pivote] + mayores 