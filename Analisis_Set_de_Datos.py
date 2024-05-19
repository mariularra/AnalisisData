from io import open
import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np
import statistics as stats
import scipy.optimize as optimization
from scipy.optimize import curve_fit

def uno(datos):
    datos = np.sort(datos)

    if np.size(datos) % 2 == 0:
      mediana = (datos[int(np.size(datos)/2)], datos[int((np.size(datos)+2)/2)])
    else:
      mediana = (datos[int(np.size(datos)/2)])
    
    bin = int(input("Ingrese la cantidad de bins desesados:"))
    rango = np.max(datos)-np.min(datos)
    ancho = rango/bin
    c = np.min(datos)
    m = []
    e = []
    for i in range(1, bin+1):
        a = c
        c += ancho
        e.append([a, c])
        g = 0
        for dato in datos:
            if a <= float(dato) < c:
                g += 1
            elif a <= float(dato) <= c and c==np.max(datos):
                g += 1
        m.append(g)
    moda = e[m.index(np.max(m))] 
    print (f"Cantidad de bins: {bin} \n Media: {np.mean(datos)} \n Mediana: {mediana} \n Moda: {moda}")

def desviacion(datos):
    std = np.std((datos), ddof=1)
    std_prom = std/np.sqrt(np.size(datos))
    print (f"Desviación estándar: {round(std,4)} \n Desviación estándar del promedio: {round(std_prom,4)}")

def nro_optimo(datos):
    n = np.size(datos)
    nop = (np.std((datos), ddof=1)/0.01)**2
    if nop <= n:
        print (f"El número óptimo de medidas es {round(nop, 4)} y las medidas efectuadas {n}, no es necesario seguir midiendo.")
    elif nop > n:
        print (f"El número óptimo de medidas es {round(nop, 4)} y las medidas efectuadas {n}, por lo que se debe seguir midiendo.")

def histograma(datos):
    fig,ax=plt.subplots()
    ax.hist(datos, bins=int(input("Ingrese la cantidad de bins desesados:")), range=(np.min(datos),np.max(datos)), color="red", edgecolor='black')
    x = input("¿Qué magnitud corresponde al eje x?")
    plt.title(f"Histograma para {x}")
    plt.xlabel(x)
    plt.ylabel("Frecuencia")
    plt.show()

def gaussiana(datos):
    def distrib(x):
        distrib= np.exp(-0.5*(1/np.std(datos, ddof=1)*(x-np.mean(datos)))**2)
        return distrib
    fig,ax=plt.subplots()
    valoresdex = np.linspace(np.min(datos), np.max(datos), 50)
    ax.plot(valoresdex,distrib(valoresdex))
    x = input("¿Qué magnitud corresponde al eje x?")
    plt.title(f"Gaussiana para {x}")
    plt.xlabel(x)
    plt.ylabel("Frecuencia")
    plt.show()

def gausshisto(datos):
    def distrib(x):
        distrib= np.exp(-0.5*(1/np.std(datos, ddof=1)*(x-np.mean(datos)))**2)
        return distrib
    datos = np.sort (np.array(datos))
    bin=int(input("Ingrese la cantidad de bins desesados:"))
    hist, bins = np.histogram(datos, bins=bin)
    fig,ax=plt.subplots()
    valoresdex = np.linspace(np.min(datos), np.max(datos), 50)
    ax.hist(datos, bins=bin, range=(np.min(datos),np.max(datos)), color="orange", edgecolor='orange',label="Histograma")
    ax.plot(valoresdex,distrib(valoresdex)*hist[np.argmax(hist)],color="blue", label="Gaussiana")
    x = input("¿Qué magnitud corresponde al eje x?")
    plt.legend(edgecolor="w")
    plt.title("Histograma y Gaussiana")
    plt.xlabel(x)
    plt.ylabel("Frecuencia")
    plt.show()

#def ajuste_lineal(x, y):
#    x = np.array(x)
#    y = np.array(y)
#    n = len(x)
#    a = (n*sum(x*y)-sum(x)*sum(y))/(n*sum(x**2)-sum(x)**2)
#    b = (-sum(x*y)*sum(x)+sum(x**2)*sum(y))/(n*sum(x**2)-sum(x)**2)
#    yfit = a*x + b
#    plt.errorbar(x, y, marker='o', capsize=4, fmt=' ')
#    plt.plot(x, yfit, '-r')

def main(datos):
    while True:
        print("Selecciona una opción: \n 1. Media, mediana y moda. \n 2. Desviación estándar \n 3. Número óptimo. Si hay que seguir midiendo. \n 4. Histograma. \n 5. Gaussiana. \n 6. Histograma y Gaussiana en el mismo gráfico. \n 7. Salir")

        opcion = input("Ingrese un número: ")

        if opcion == "1":
            uno(datos)
            continue
        elif opcion == "2":
            desviacion(datos)
            continue
        elif opcion == "3":
            nro_optimo(datos)
            continue
        elif opcion == "4":
            histograma(datos)
            continue
        elif opcion == "5":
            gaussiana(datos)
            continue
        elif opcion == "6":
            gausshisto(datos)
            continue
        elif opcion == "7":
            print("Adios!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.")
            continue

while True:
    try:
        pregunta = int(input("Seleccione un número: \n 1 - quiere ingresar los datos a mano \n 2 - quiere ingresar un archivo"))
        if pregunta == 1:
            datos = [input("Ingrese elemento {} de la lista: ".format(i+1)) for i in range(int(input("Ingrese la cantidad de elementos en la lista: ")))]
            break  
        elif pregunta == 2:
            while True:
                archivo = input("Ingrese el nombre del archivo (sin olvidarse de escribir la extensión del mismo):")
                try:
                    with open (archivo, "r") as f:
                        data = f
                        datos = np.loadtxt (archivo)
                        data.close()
                        lect = np.array(datos)
                        break
                except FileNotFoundError:
                    print("El archivo", archivo, "no existe.")
                    continue  
            print("Gracias! Se ha leido el archivo {} correctamente".format(archivo))
            break
        else:
            print ("Ha ingresado un número fuera de rango ¿Puede volver a ingresar 1 o 2?")
            continue
    except ValueError:
        print("Ha ingresado algo que no es un número. ¿Puede volver a ingresar 1 o 2?")

if __name__ == "__main__":
    main(datos)