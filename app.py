import pandas as pd
# Lista de las edades de los alumnos
edades = [18,19,20,21,22,23,25,28,29,30,34]

def analisis_estadistico(edades):
    # Verificamos si no es una lista o si está vacía
    if not isinstance(edades, list) or len(edades) == 0:
        print("La lista de edades está vacía o el parámetro no es una lista")
        return None
    # Lista de las veces que se repiten esas edades
    fi = [1,9,4,3,4,1,1,2,2,1,2]

    # Verificar si todas las edades son numéricas
    if not all(isinstance(x, (int, float)) for x in edades):
        print("La lista de edades contiene elementos que no son numéricos.")
        return None

    # Crear DataFrame con las columnas edades y fi
    df = pd.DataFrame({"edades": edades, "fi": fi})

    # Calculamos la tabla de frecuencias
    # Frecuencia absoluta acumulada
    df["Fi"] = df["fi"].cumsum()
    # Frecuencia relativa simple
    df["ri"] = (df["fi"] / df["fi"].sum()).round(3)
    # Frecuencia relativa acumulada
    df["Ri"] = df["ri"].cumsum()
    # Frecuencia porcentual simple
    df["pi%"] = df["ri"] * 100
    # Frecuencia porcentual acumulada
    df["Pi%"] = df["pi%"].cumsum()

    # Retornamos el dataframe
    return df
# Mostramos la tabla de frecuencias
print(analisis_estadistico(edades))
