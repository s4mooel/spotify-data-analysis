import pandas as pd

def calculate_statistics(df):
    stats = {
        'popularity_stats': {
            'max': df['popularity'].max(),
            'min': df['popularity'].min(),
            'mean': df['popularity'].mean(),
            'median': df['popularity'].median()
        },
        'duration_stats': {
            'longest_min': df['duration_min'].max(),
            'shortest_min': df['duration_min'].min(),
            'avg_min': df['duration_min'].mean()
        },
        'explicit_stats': {
            'explicit_count': df['explicit'].sum(),
            'explicit_percentage': (df['explicit'].sum() / len(df)) * 100
        }
    }
    return stats

def top_genres_analysis(df, top_n=10):
    genre_analysis = df.groupby('genre').agg({
        'popularity': ['mean', 'count'],
        'duration_min': 'mean',
        'explicit': 'mean'
    }).round(2)
    
    genre_analysis.columns = ['avg_popularity', 'song_count', 'avg_duration_min', 'explicit_ratio']
    top_genres = genre_analysis.sort_values('avg_popularity', ascending=False).head(top_n)
    
    return top_genres

def top_artists_analysis(df, top_n=10):
    artist_analysis = df.groupby('artists').agg({
        'popularity': ['mean', 'count'],
        'duration_min': 'mean'
    }).round(2)
    
    artist_analysis.columns = ['avg_popularity', 'song_count', 'avg_duration_min']
    top_artists = artist_analysis.sort_values('avg_popularity', ascending=False).head(top_n)
    
    return top_artists