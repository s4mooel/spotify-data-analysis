"""
Spotify Data Analysis - Archivo Principal
Autor: Samuel Ibañez
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Agregar la carpeta src al path
sys.path.append('src')

from data_loader import load_spotify_data, get_basic_info
from visualization import create_popularity_charts, create_duration_analysis, create_artist_analysis
from analysis import calculate_statistics, top_genres_analysis, top_artists_analysis

def main():
    print("🎵 Iniciando Análisis de Datos de Spotify...")
    print("=" * 50)
    
    try:
        # Cargar datos
        print("Cargando datos...")
        df = load_spotify_data('data/spotify_tracks.csv') 
        
        # Información básica
        basic_info = get_basic_info(df)
        
        # Mostrar información básica
        print(f"\nRESUMEN DEL DATASET:")
        print(f"   Total de canciones: {basic_info['total_songs']:,}")
        print(f"   Géneros únicos: {basic_info['total_genres']}")
        print(f"   Artistas únicos: {basic_info['total_artists']}")
        print(f"   Álbumes únicos: {basic_info['total_albums']}")
        print(f"   Canciones explícitas: {basic_info['explicit_songs']} ({basic_info['explicit_songs']/basic_info['total_songs']*100:.1f}%)")
        print(f"   Popularidad promedio: {basic_info['avg_popularity']:.2f}")
        print(f"   ⏱Duración promedio: {basic_info['avg_duration_min']:.2f} minutos")
        
        # Análisis estadístico
        print("\n Calculando estadísticas detalladas...")
        stats = calculate_statistics(df)
        
        # Análisis por género
        print("\n Analizando géneros...")
        top_genres = top_genres_analysis(df)
        print("\n TOP 5 GÉNEROS MÁS POPULARES:")
        for i, (genre, data) in enumerate(top_genres.head().iterrows(), 1):
            print(f"   {i}. {genre}:")
            print(f"      Popularidad: {data['avg_popularity']:.2f}")
            print(f"      Canciones: {data['song_count']}")
            print(f"      Duración promedio: {data['avg_duration_min']:.2f} min")
        
        # Análisis de artistas
        print("\n Analizando artistas...")
        top_artists = top_artists_analysis(df)
        print("\n TOP 5 ARTISTAS MÁS POPULARES:")
        for i, (artist, data) in enumerate(top_artists.head().iterrows(), 1):
            print(f"   {i}. {artist}:")
            print(f"      Popularidad: {data['avg_popularity']:.2f}")
            print(f"      Canciones: {data['song_count']}")
        
        # Visualizaciones
        print("\n Generando visualizaciones...")
        create_popularity_charts(df)
        create_duration_analysis(df)
        create_artist_analysis(df)
        
        print("\n" + "=" * 50)
        print(" ¡Análisis completado exitosamente!")
        print(" Los gráficos se guardaron en la carpeta 'images/'")
        print(" Puedes revisar los archivos PNG generados")
        
    except FileNotFoundError:
        print(" Error: No se encontró el archivo 'spotify_tracks.csv'")
        print("   Asegúrate de que el archivo esté en la carpeta correcta")
    except Exception as e:
        print(f" Error inesperado: {e}")

if __name__ == "__main__":
    main()