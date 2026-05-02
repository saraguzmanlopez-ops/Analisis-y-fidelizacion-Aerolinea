import pandas as pd

def calcular_frecuencia(df, lista_items, columna):
    """
    Calcula el porcentaje de aparición de elementos de una lista 
    en una columna específica de un DataFrame.
    """
    resultados = {}
    total_filas = len(df)
    
    for item in lista_items:
        conteo = (df[columna] == item).sum()
        porcentaje = round((conteo / total_filas) * 100, 2)
        resultados[item] = porcentaje
        print(f"{item}: {porcentaje}%")
    
    return resultados