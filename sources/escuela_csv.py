import pandas as pd
from pathlib import Path


def cargar_desde_csv():
    base_dir = Path(__file__).resolve().parent.parent
    archivo = base_dir / "data" / "escuelas-coordenadas-agosto-2018 (1).csv"

    df = pd.read_csv(
        archivo,
        sep=";",
        encoding="latin1"
    )

    return df


if __name__ == "__main__":
    df = cargar_desde_csv()
    print(df.head())
    print(f"\nFilas: {len(df)}")
    print(f"Columnas: {list(df.columns)}")