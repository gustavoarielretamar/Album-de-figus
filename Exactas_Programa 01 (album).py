# %% LIBRERIAS:
import random


# %% CUANTAS_FIGUS, cantidad de figuritas para llenar un album:
def cuantas_figus(figus_total, debug=False):
    album = [0] * figus_total
    cont = 0
    while sum(album) < figus_total:
        figu = random.randint(0, figus_total - 1)
        cont += 1
        album[figu] = 1
    if debug:
        print(cont)
    return cont


# %% PROMEDIO, promediar una lista:
def promedio(lista, debug=False):
    prom = sum(lista) / len(lista)
    if debug:
        print(prom)
    return prom


# %% SIMULAR_MUCHAS_REPETICIONES, llena n cantidad de albumes:
def simular_muchas_repeticiones(n_rep, figus_total, debug=False):
    n_resultados = [0] * n_rep
    cont = 0
    while cont < n_rep:
        resultado = cuantas_figus(figus_total)
        n_resultados.append(resultado)
        cont += 1
    # promedio (muchos_resultados_album_de_6)
    if debug:
        print(n_resultados)
    return n_resultados


# %% DAME_ CHANCES, calcular probabilidad:
def dame_chance(resultados, cantidad_maxima, debug=False):
    i = 0
    meSirve = 0
    while i < len(resultados):
        if resultados[i] <= cantidad_maxima:
            meSirve = meSirve + 1
        i += 1
    chances = meSirve*100 / len(resultados)
    if debug:
        print(chances)
    return chances


# %% DALE_COMPRAME, cuantas figuritas hay que comprar con PROB
def dale_comprame(resultados, figus_total, prob, debug=False):
    probabilidad = 0
    cont = figus_total
    while probabilidad < prob:
        probababilidad = dame_chance(resultados, cont)
        cont += 1
    if debug:
        print(cont)
    return cont


# %% PARAMETROS:
figus_total = 6
n_rep = 1000
resultados = simular_muchas_repeticiones(n_rep, figus_total)
cantidad_maxima = 15
prob = 50  # numero entre 0 y 1
# %% LLAMADAS:
# simular_muchas_repeticiones(repeticiones, figus)
# dame_chance(resultados, cantidad_maxima, True)
dale_comprame(resultados, figus_total, prob, True)
