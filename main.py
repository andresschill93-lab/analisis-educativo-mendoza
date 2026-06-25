from data_processing import limpiar_datos, guardar_datos_limpios
from geo_analysis import crear_geodataframe, guardar_geojson, crear_mapa_interactivo


def main():
    print("Iniciando proyecto...")

    print("Limpiando datos...")
    df = limpiar_datos()
    guardar_datos_limpios(df)
    print("Datos limpios guardados.")

    print("Creando GeoDataFrame...")
    gdf = crear_geodataframe(df)
    print("GeoDataFrame creado.")

    print("Guardando GeoJSON...")
    guardar_geojson(gdf)
    print("GeoJSON guardado.")

    print("Creando mapa interactivo...")
    crear_mapa_interactivo(gdf)
    print("Mapa interactivo guardado en data/mapa_escuelas_mendoza.html")

    print("Proyecto finalizado correctamente.")


if __name__ == "__main__":
    main()