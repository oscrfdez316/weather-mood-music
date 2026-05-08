# Rainy Day Playlist: Predicting Musical Mood from Weather Conditions

A data science project that investigates whether weather conditions influence musical mood preferences, using Spotify audio features and historical weather data.

## Research Question
Do weather conditions (rain, sun, clouds, etc.) correlate with the emotional tone of music people listen to?

## Datasets
- **Spotify Mood Dataset (Moodify):** 278k labeled songs with audio features (valence, energy, danceability, tempo, acousticness) — [Kaggle](https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset)
- **Historical Hourly Weather Data 2012-2017:** Hourly weather readings across 36 cities (temperature, humidity, weather description) — [Kaggle](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data)

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/oscrfdez316/weather-mood-music.git
cd weather-mood-music
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Download the datasets from Kaggle and place CSVs in:
   - data/raw/spotify_real/ — Spotify mood dataset
   - data/raw/weather_real/ — Historical weather dataset

4. Run notebooks in order:
```bash
jupyter notebook
```
Open and run 01_eda.ipynb through 04_clustering.ipynb in sequence.

## Key Findings
- Clear weather is the strongest positive predictor of musical valence (happiness)
- Rainy and stormy conditions correlate with lower valence (sadder music)
- KMeans clustering (k=4 selected via elbow method) reveals four distinct weather-mood profiles
- Ridge regression outperforms the baseline but R2=0.08 suggests weather is one of many factors influencing music mood

## Methods
- **Preprocessing:** Multi-dataset merge, weather category simplification, one-hot encoding, StandardScaler normalization, 80/20 train/test split
- **Regression:** Baseline (mean), Linear Regression, Ridge Regression — evaluated with MSE and R2
- **Clustering:** KMeans (k=4 selected via elbow method), PCA for 2D visualization

## Requirements
See requirements.txt
