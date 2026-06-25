import geopandas as gpd
import folium


def crear_geodataframe(df):
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(
            df["longitud_limpia"],
            df["latitud_limpia"]
        ),
        crs="EPSG:4326"
    )

    return gdf


def guardar_geojson(gdf):
    gdf.to_file(
        "data/escuelas_mendoza.geojson",
        driver="GeoJSON"
    )


def crear_mapa_interactivo(gdf):
    mapa = folium.Map(
        location=[
            gdf["latitud_limpia"].mean(),
            gdf["longitud_limpia"].mean()
        ],
        zoom_start=8
    )

    for _, fila in gdf.iterrows():
        folium.Marker(
            location=[
                fila["latitud_limpia"],
                fila["longitud_limpia"]
            ],
            popup=f"""
            <b>{fila["escuela_nombre"]}</b><br>
            Departamento: {fila["departamento"]}<br>
            Localidad: {fila["localidad"]}<br>
            Nivel: {fila["nivel"]}<br>
            Gestión: {fila["gestion"]}<br>
            Ámbito: {fila["ambito"]}
            """
        ).add_to(mapa)

    mapa.save("data/mapa_escuelas_mendoza.html")