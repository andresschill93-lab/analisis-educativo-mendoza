import pandas as pd
from sources.escuela_csv import cargar_desde_csv


def limpiar_coord(valor):
    if pd.isna(valor):
        return pd.NA

    valor = str(valor).strip()

    # Convierte valores tipo "-68.843.619" en "-68.843619"
    partes = valor.split(".")
    if len(partes) > 2:
        valor = partes[0] + "." + "".join(partes[1:])

    return pd.to_numeric(valor, errors="coerce")


def limpiar_datos():
    df = cargar_desde_csv()

    # Eliminar columnas vacías o sin nombre útil
    df = df.loc[:, ~df.columns.str.contains("^Unnamed|^$", regex=True)]

    # Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Quitar espacios sobrantes en columnas de texto
    columnas_texto = df.select_dtypes(include="object").columns

    for col in columnas_texto:
        df[col] = df[col].astype(str).str.strip()

    # Reemplazar textos vacíos por valores nulos reales
    df = df.replace(["", "nan", "None"], pd.NA)

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Limpiar coordenadas
    # En este dataset, lati parece contener longitud (-68)
    # y longitud parece contener latitud (-32)
    df["longitud_limpia"] = df["lati"].apply(limpiar_coord)
    df["latitud_limpia"] = df["longitud"].apply(limpiar_coord)

    # Filtrar coordenadas razonables para Mendoza
    df = df[
        df["latitud_limpia"].between(-37, -30)
        & df["longitud_limpia"].between(-70, -66)
    ]

    return df


def guardar_datos_limpios(df):
    df.to_csv(
        "data/escuelas_mendoza_limpio.csv",
        index=False,
        encoding="utf-8"
    )


if __name__ == "__main__":
    df = limpiar_datos()

    print(df.head())
    print("\nInformación del dataset limpio:")
    print(df.info())

    print("\nValores nulos por columna:")
    print(df.isna().sum())

    guardar_datos_limpios(df)
    print("\nArchivo limpio guardado en: data/escuelas_mendoza_limpio.csv")
