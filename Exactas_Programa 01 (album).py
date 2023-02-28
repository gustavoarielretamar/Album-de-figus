#variables globales
import random
figus = 6
repeticiones = 1000
resultados=[]
figusMaximas =0
muchos_resultados_album_de_6 = resultados
probabilidadesDeseadas= 0.9 #numero entre 0 y 1

#LLENAR un album
def cuantas_figus(figus_total): #aca definimos la función
    album = [0]*figus_total
    contador = 0
    while sum (album) < figus_total:
        figu = random.randint(0, figus_total - 1)
        contador = contador+1
        album[figu]= 1
    return contador

#promediar una lista
def promedio (lista):
    promedio = sum(lista)/len(lista)
    #print (promedio)
    return promedio

#LOOP para llenar varios álbumes
def simular_muchas_repeticiones(n_rep, figus_total):
    contador = 0
    while contador < n_rep:
        nuevo_resultado = cuantas_figus(figus_total)
        muchos_resultados_album_de_6.append(nuevo_resultado)
        contador = contador+1
    promedio (muchos_resultados_album_de_6)
    return muchos_resultados_album_de_6
simular_muchas_repeticiones(repeticiones, figus)


#calcular probabilidad
def dame_chance(resultados, cantidad_maxima):
    iterator = 0
    meSirve = 0
    while iterator<len(resultados):
        if resultados[iterator] <= cantidad_maxima:
            meSirve = meSirve + 1
        iterator = iterator + 1
    chances= meSirve/len(resultados)
    print (chances)
    return chances
        
#dame_chance(muchos_resultados_album_de_6, figusMaximas)


def dale_comprame (resultados, figus_total, prob):
    if figus_total > 0:
        dame_chance(muchos_resultados_album_de_6, figusMaximas)
    else:
        probabilidad = 0
        cantidadMaxima = figus
        while probabilidad < prob:
            iterator = 0
            meSirve = 0
            while iterator<len(resultados):
                if resultados[iterator] <= cantidadMaxima:
                    meSirve = meSirve + 1
                iterator = iterator + 1
            chances= meSirve/len(resultados)
            probabilidad = chances
            cantidadMaxima = cantidadMaxima + 1
        print (cantidadMaxima)
        return cantidadMaxima


dale_comprame (muchos_resultados_album_de_6, figusMaximas, probabilidadesDeseadas)
