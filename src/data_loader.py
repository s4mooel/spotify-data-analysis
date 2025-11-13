import pandas as pd

def load_spotify_data(file_path):
    df = pd.read_csv(file_path)
    
    # Limpieza básica
    df = df.drop_duplicates()
    df = df.dropna()
    
    # Convertir duración a minutos
    df['duration_min'] = df['duration_ms'] / 60000
    
    print(f" Datos cargados: {len(df)} canciones, {df['genre'].nunique()} géneros")
    return df

def get_basic_info(df):
    info = {
        'total_songs': len(df),
        'total_genres': df['genre'].nunique(),
        'total_artists': df['artists'].nunique(),
        'total_albums': df['album'].nunique(),
        'explicit_songs': df['explicit'].sum(),
        'avg_popularity': df['popularity'].mean(),
        'avg_duration_min': df['duration_min'].mean()
    }
    return info