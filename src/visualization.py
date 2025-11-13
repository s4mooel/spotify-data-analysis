import matplotlib.pyplot as plt
import seaborn as sns
import os

def setup_visualization_style():
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.set_palette("viridis")
    plt.rcParams['figure.figsize'] = (12, 8)

def create_popularity_charts(df):
    setup_visualization_style()
    
    # Asegurar que existe la carpeta images
    os.makedirs('../images', exist_ok=True)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle(' Análisis de Popularidad - Spotify Data', fontsize=16, fontweight='bold')
    
    # Top géneros por popularidad
    top_genres = df.groupby('genre')['popularity'].mean().sort_values(ascending=False).head(10)
    axes[0,0].barh(range(len(top_genres)), top_genres.values, color='#1DB954')
    axes[0,0].set_yticks(range(len(top_genres)))
    axes[0,0].set_yticklabels(top_genres.index)
    axes[0,0].set_xlabel('Popularidad Promedio')
    axes[0,0].set_title(' Top 10 Géneros Más Populares')
    axes[0,0].grid(axis='x', alpha=0.3)
    
    # Distribución de popularidad
    axes[0,1].hist(df['popularity'], bins=30, alpha=0.7, color='#1DB954')
    axes[0,1].set_xlabel('Popularidad')
    axes[0,1].set_ylabel('Frecuencia')
    axes[0,1].set_title(' Distribución de Popularidad')
    axes[0,1].grid(alpha=0.3)
    
    # Boxplot de popularidad por género (top 5)
    top_5_genres = top_genres.head(5).index
    top_genres_df = df[df['genre'].isin(top_5_genres)]
    sns.boxplot(data=top_genres_df, x='popularity', y='genre', ax=axes[1,0])
    axes[1,0].set_title(' Popularidad por Género (Top 5)')
    axes[1,0].set_xlabel('Popularidad')
    
    # Conteo de canciones por género
    genre_counts = df['genre'].value_counts().head(10)
    axes[1,1].bar(range(len(genre_counts)), genre_counts.values, color='#FF6B6B')
    axes[1,1].set_xticks(range(len(genre_counts)))
    axes[1,1].set_xticklabels(genre_counts.index, rotation=45)
    axes[1,1].set_ylabel('Número de Canciones')
    axes[1,1].set_title(' Canciones por Género (Top 10)')
    axes[1,1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../images/popularity_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_duration_analysis(df):
    setup_visualization_style()
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('⏱ Análisis de Duración - Spotify Data', fontsize=16, fontweight='bold')
    
    # Duración por género (top 10)
    duration_by_genre = df.groupby('genre')['duration_min'].mean().sort_values(ascending=False).head(10)
    axes[0].bar(range(len(duration_by_genre)), duration_by_genre.values, color='#4ECDC4')
    axes[0].set_xticks(range(len(duration_by_genre)))
    axes[0].set_xticklabels(duration_by_genre.index, rotation=45)
    axes[0].set_ylabel('Duración (minutos)')
    axes[0].set_title(' Duración Promedio por Género (Top 10)')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Scatter plot: Duración vs Popularidad
    axes[1].scatter(df['duration_min'], df['popularity'], alpha=0.6, color='#FFD93D')
    axes[1].set_xlabel('Duración (minutos)')
    axes[1].set_ylabel('Popularidad')
    axes[1].set_title(' Relación: Duración vs Popularidad')
    axes[1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../images/duration_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_artist_analysis(df):
    setup_visualization_style()
    
    from analysis import top_artists_analysis
    
    top_artists = top_artists_analysis(df, 10)
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle(' Análisis de Artistas - Spotify Data', fontsize=16, fontweight='bold')
    
    # Top artistas por popularidad
    axes[0].barh(range(len(top_artists)), top_artists['avg_popularity'].values, color='#A78BFA')
    axes[0].set_yticks(range(len(top_artists)))
    axes[0].set_yticklabels([artist[:20] + '...' if len(artist) > 20 else artist for artist in top_artists.index])
    axes[0].set_xlabel('Popularidad Promedio')
    axes[0].set_title(' Top 10 Artistas Más Populares')
    axes[0].grid(axis='x', alpha=0.3)
    
    # Artistas con más canciones
    artist_song_counts = df['artists'].value_counts().head(10)
    axes[1].bar(range(len(artist_song_counts)), artist_song_counts.values, color='#F472B6')
    axes[1].set_xticks(range(len(artist_song_counts)))
    axes[1].set_xticklabels([artist[:15] + '...' if len(artist) > 15 else artist for artist in artist_song_counts.index], rotation=45)
    axes[1].set_ylabel('Número de Canciones')
    axes[1].set_title(' Artistas con Más Canciones')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../images/artist_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()